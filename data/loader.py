"""
TradeMind AI — Data Loader
============================
CRITICAL FIX: All date arithmetic uses only timedelta on tz-naive pd.Timestamp.
Models receive plain numpy arrays (RangeIndex), never DatetimeIndex.
This eliminates EVERY variant of the int+datetime / Timestamp+int error.
"""
import warnings; warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import yfinance as yf
import streamlit as st
from datetime import timedelta
from typing import Optional, Tuple


def safe_last_date(df: pd.DataFrame) -> pd.Timestamp:
    """
    Always returns tz-naive pd.Timestamp at midnight.
    Handles: tz-aware, tz-naive, numpy datetime64, python datetime.
    This is the ONLY way to get the last date — used by every model.
    """
    raw = df["Date"].max()
    ts  = pd.Timestamp(raw)
    if ts.tzinfo is not None:
        ts = ts.tz_convert("UTC").tz_localize(None)
    return ts.normalize()


def future_dates(df: pd.DataFrame, horizon: int) -> pd.DatetimeIndex:
    """Build future date range — the ONLY place we create forecast dates."""
    last = safe_last_date(df)
    return pd.date_range(start=last + timedelta(days=1), periods=horizon, freq="D")


@st.cache_data(show_spinner=False, ttl=300)
def fetch_ohlcv(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    """Download from Yahoo Finance. Returns empty DataFrame on failure."""
    try:
        df = yf.download(ticker, period=period, interval=interval,
                         progress=False, auto_adjust=True)
        if df is None or df.empty:
            return pd.DataFrame()
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [c[0] for c in df.columns]
        df.reset_index(inplace=True)
        return df
    except Exception as e:
        print(f"[Loader] fetch error {ticker}: {e}")
        return pd.DataFrame()


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize columns, parse dates, strip timezone, sort, drop nulls.
    After this: Date column is always tz-naive datetime64[us].
    """
    if df is None or df.empty:
        return pd.DataFrame()

    df = df.copy()

    # Normalize date column name
    for alias in ["Datetime", "datetime", "index", "Timestamp", "timestamp"]:
        if alias in df.columns and "Date" not in df.columns:
            df = df.rename(columns={alias: "Date"})

    if "Date" not in df.columns or "Close" not in df.columns:
        return pd.DataFrame()

    wanted = ["Date","Open","High","Low","Close","Volume"]
    df = df[[c for c in wanted if c in df.columns]].copy()

    # Parse and STRIP timezone — this is critical for hourly/minute data
    df["Date"] = pd.to_datetime(df["Date"])
    if df["Date"].dt.tz is not None:
        df["Date"] = df["Date"].dt.tz_convert("UTC").dt.tz_localize(None)
    df["Date"] = df["Date"].dt.normalize()  # strip HH:MM:SS

    df.sort_values("Date", inplace=True)
    df.drop_duplicates("Date", keep="last", inplace=True)
    df.reset_index(drop=True, inplace=True)

    for col in ["Open","High","Low","Close","Volume"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df.dropna(subset=["Close"], inplace=True)
    return df


def load_asset(ticker: str, period: str, interval: str) -> pd.DataFrame:
    """One-call pipeline: fetch → preprocess."""
    raw = fetch_ohlcv(ticker, period, interval)
    if raw.empty:
        return pd.DataFrame()
    return preprocess(raw)


def fetch_live_price(ticker: str) -> Tuple[Optional[float], Optional[float]]:
    """Returns (price, pct_change). Both None on failure."""
    try:
        data = yf.Ticker(ticker).history(period="1d", interval="1m")
        if data.empty:
            return None, None
        price = float(data["Close"].iloc[-1])
        open_ = float(data["Open"].iloc[0])
        return price, (price - open_) / open_ * 100
    except Exception:
        return None, None

"""
TradeMind AI — LSTM Model
===========================
Scaled training → normalized RMSE/MAE near 0-1.
Future dates from future_dates() only — no date arithmetic in model.
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from data.loader import future_dates
from utils.evaluation import compute_metrics_normalized
from config.settings import MIN_LSTM, LOOKBACK, EPOCHS, LSTM_UNITS

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense, Dropout
    from tensorflow.keras.callbacks import EarlyStopping
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False


def _make_sequences(data: np.ndarray, lookback: int):
    X, y = [], []
    for i in range(len(data) - lookback):
        X.append(data[i: i + lookback, 0])
        y.append(data[i + lookback, 0])
    return np.array(X), np.array(y)


def forecast(df: pd.DataFrame, horizon: int) -> dict:
    if not TF_AVAILABLE:
        raise ImportError("Run: pip install tensorflow")
    if len(df) < MIN_LSTM:
        raise ValueError(f"Need ≥{MIN_LSTM} rows. Got {len(df)}.")

    close  = df["Close"].values.astype(float).reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(close)

    X, y   = _make_sequences(scaled, LOOKBACK)
    split  = int(len(X) * 0.8)
    Xtr, Xte = X[:split].reshape(-1, LOOKBACK, 1), X[split:].reshape(-1, LOOKBACK, 1)
    ytr, yte  = y[:split], y[split:]

    model = Sequential([
        LSTM(LSTM_UNITS, return_sequences=True, input_shape=(LOOKBACK, 1)),
        Dropout(0.2),
        LSTM(LSTM_UNITS // 2),
        Dropout(0.2),
        Dense(1),
    ])
    model.compile(optimizer="adam", loss="huber")  # Huber loss → more robust
    model.fit(Xtr, ytr, epochs=EPOCHS, batch_size=32,
              validation_data=(Xte, yte), verbose=0,
              callbacks=[EarlyStopping(patience=3, restore_best_weights=True)])

    # Eval on test
    pred_te = model.predict(Xte, verbose=0).flatten()
    metrics = compute_metrics_normalized(yte, pred_te)

    # Multi-step future
    seq = scaled[-LOOKBACK:].reshape(1, LOOKBACK, 1)
    preds_sc = []
    for _ in range(horizon):
        nv = float(model.predict(seq, verbose=0)[0][0])
        preds_sc.append(nv)
        seq = np.append(seq[:, 1:, :], [[[nv]]], axis=1)

    fc_prices = scaler.inverse_transform(
        np.array(preds_sc).reshape(-1, 1)
    ).flatten()

    fdates = future_dates(df, horizon)

    return {
        "forecast_df": pd.DataFrame({"Date": fdates, "Forecast": fc_prices}),
        "metrics":     metrics,
        "model_name":  "LSTM",
        "available":   True,
    }

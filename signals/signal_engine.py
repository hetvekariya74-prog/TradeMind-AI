"""TradeMind AI — Signal Engine + WHY Explainer"""
import numpy as np
import pandas as pd
from typing import Optional


def _rsi(rsi):
    if np.isnan(rsi): return 0, 0, None, None
    if rsi < 30: return 25, +1, f"RSI {rsi:.0f} — oversold, potential reversal up", None
    if rsi > 70: return 25, -1, f"RSI {rsi:.0f} — overbought, pullback likely", "High RSI risk"
    return 8,  0, f"RSI {rsi:.0f} — neutral", None


def _macd(macd, sig, hist):
    if any(np.isnan(v) for v in [macd,sig,hist]): return 0, 0, None, None
    if macd > sig and hist > 0: return 25, +1, "MACD bullish crossover — momentum up", None
    if macd < sig and hist < 0: return 25, -1, "MACD bearish crossover — momentum down", "Bearish momentum"
    return 5, 0, "MACD near signal line", None


def _bb(close, upper, lower, pct):
    if any(np.isnan(v) for v in [close,upper,lower]): return 0, 0, None, None
    if close < lower: return 20, +1, "Price below lower Bollinger — near support", None
    if close > upper: return 20, -1, "Price above upper Bollinger — stretched", "Extended above bands"
    if pct < 0.2:     return 10, +1, "Price in lower 20% of bands — mild bullish", None
    if pct > 0.8:     return 10, -1, "Price in upper 80% of bands — mild bearish", None
    return 5, 0, f"Price mid-band ({pct*100:.0f}%)", None


def _sma(s7, s30):
    if any(np.isnan(v) for v in [s7,s30]): return 0, 0, None, None
    diff = (s7-s30)/s30*100
    if s7 > s30: return 15, +1, f"Golden cross — SMA{int(s7)} > SMA{int(s30)} (+{diff:.1f}%)", None
    return 15, -1, f"Death cross — SMA below long average ({diff:.1f}%)", "Downtrend in MAs"


def _stoch(k, d):
    if any(np.isnan(v) for v in [k,d]): return 0, 0, None, None
    if k < 20 and k > d: return 10, +1, f"Stochastic {k:.0f} — oversold, %K crossing up", None
    if k > 80 and k < d: return 10, -1, f"Stochastic {k:.0f} — overbought, %K crossing down", "Overbought stochastic"
    return 3, 0, f"Stochastic {k:.0f} — neutral", None


def _vol(v7, v30):
    if any(np.isnan(v) for v in [v7,v30]) or v30 == 0: return 0, None
    r = v7/v30
    if r > 1.5: return -12, f"Volatility spike: {r:.1f}x above average — caution"
    if r > 1.2: return -6,  f"Elevated volatility ({r:.1f}x average)"
    return 0, None


def _fcast(fdf, price):
    if fdf is None or fdf.empty or np.isnan(price): return 0, 0, None, None
    end = float(fdf["Forecast"].iloc[-1])
    mid = float(fdf["Forecast"].iloc[len(fdf)//2])
    pct = (end - price) / price * 100
    if pct >  5: return 15, +1, f"AI forecast: +{pct:.1f}% projected — strong uptrend", None
    if pct >  2: return 10, +1, f"AI forecast: +{pct:.1f}% — moderate upside", None
    if pct < -5: return 15, -1, f"AI forecast: {pct:.1f}% — strong downtrend", "Model projects downside"
    if pct < -2: return 10, -1, f"AI forecast: {pct:.1f}% — moderate downside", None
    return 5, 0,  f"AI forecast: {pct:.1f}% — roughly flat", None


def generate(df_feat: pd.DataFrame,
             forecast_df: Optional[pd.DataFrame] = None,
             sentiment: float = 0.0) -> dict:
    """
    Generate BUY/SELL/HOLD signal with full WHY explanation.

    Returns:
        signal, confidence (%), why (list), risks (list),
        tech_score (0-100), final_score (0-100), components (dict)
    """
    last = df_feat.dropna(subset=["Close"]).iloc[-1]
    g    = lambda c: float(last[c]) if c in last.index and not pd.isna(last[c]) else np.nan

    rs,  rd,  rw,  rr  = _rsi(g("RSI"))
    ms,  md,  mw,  mr  = _macd(g("MACD"), g("MACD_sig"), g("MACD_hist"))
    bs,  bd,  bw,  br  = _bb(g("Close"), g("BB_upper"), g("BB_lower"), g("BB_pct"))
    ss,  sd,  sw,  sr  = _sma(g("SMA7"),  g("SMA30"))
    sts, std, stw, str_ = _stoch(g("Stoch_K"), g("Stoch_D"))
    fs,  fd,  fw,  fr  = _fcast(forecast_df, g("Close"))
    vpen, vr            = _vol(g("Vol7"),  g("Vol30"))

    total_w = rs+ms+bs+ss+sts+fs or 1
    dir_score = (rd*rs + md*ms + bd*bs + sd*ss + std*sts + fd*fs) / total_w

    # Technical score 0-100
    bull = sum(s for s,d in [(rs,rd),(ms,md),(bs,bd),(ss,sd),(sts,std),(fs,fd)] if d>0)
    bear = sum(s for s,d in [(rs,rd),(ms,md),(bs,bd),(ss,sd),(sts,std),(fs,fd)] if d<0)
    tech_score = int((bull - bear) / total_w * 50 + 50)

    raw_conf   = int(abs(dir_score) * 100) + vpen
    confidence = max(5, min(99, raw_conf))

    # Multi-factor final score
    sent_score = int((sentiment + 1) / 2 * 100)
    final_score = int(tech_score * 0.55 + sent_score * 0.20 + confidence * 0.25)
    final_score = max(0, min(100, final_score))

    if dir_score > 0.12:   signal, emoji = "BUY",  "🟢"
    elif dir_score < -0.12: signal, emoji = "SELL", "🔴"
    else:                   signal, emoji = "HOLD", "🟡"

    why   = [w for w in [rw,mw,bw,sw,stw,fw] if w]
    risks = [r for r in [rr,mr,br,sr,str_,fr,vr] if r]

    return {
        "signal":     signal,
        "emoji":      emoji,
        "confidence": confidence,
        "why":        why,
        "risks":      risks,
        "tech_score": tech_score,
        "final_score":final_score,
        "dir_score":  round(dir_score, 3),
        "components": {
            "RSI":      {"score":rs,  "dir":rd},
            "MACD":     {"score":ms,  "dir":md},
            "Bollinger":{"score":bs,  "dir":bd},
            "SMA":      {"score":ss,  "dir":sd},
            "Stoch":    {"score":sts, "dir":std},
            "Forecast": {"score":fs,  "dir":fd},
        },
    }

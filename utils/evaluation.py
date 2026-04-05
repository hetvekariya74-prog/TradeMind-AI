"""TradeMind AI — Evaluation Metrics"""
import numpy as np
import math
from sklearn.metrics import mean_squared_error, mean_absolute_error


def compute_rmse_mae(y_true, y_pred):
    """Returns (rmse, mae) on raw values."""
    y_true = np.array(y_true).flatten()
    y_pred = np.array(y_pred).flatten()
    n = min(len(y_true), len(y_pred))
    if n == 0:
        return 0.0, 0.0
    rmse = math.sqrt(mean_squared_error(y_true[-n:], y_pred[-n:]))
    mae  = mean_absolute_error(y_true[-n:], y_pred[-n:])
    return round(rmse, 6), round(mae, 6)


def compute_metrics_normalized(y_true, y_pred):
    """
    Returns normalized metrics where RMSE/MAE are close to 0-1 range.
    Uses MinMax-scaled values so metrics are scale-independent.
    Also returns MAPE (%) which is the most useful for financial data.
    """
    y_true = np.array(y_true).flatten()
    y_pred = np.array(y_pred).flatten()
    n = min(len(y_true), len(y_pred))
    y_true, y_pred = y_true[-n:], y_pred[-n:]

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    yt_scaled = scaler.fit_transform(y_true.reshape(-1,1)).flatten()
    yp_scaled = scaler.transform(y_pred.reshape(-1,1)).flatten()

    rmse_n = math.sqrt(mean_squared_error(yt_scaled, yp_scaled))
    mae_n  = mean_absolute_error(yt_scaled, yp_scaled)

    # MAPE
    mask = y_true != 0
    mape = float(np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100) if mask.any() else 0.0

    return {
        "RMSE (norm)": round(rmse_n, 4),
        "MAE (norm)":  round(mae_n,  4),
        "MAPE (%)":    round(mape,   2),
    }

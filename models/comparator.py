"""
TradeMind AI — Model Comparison Engine
========================================
Runs all available models, picks the best by RMSE.
"""

import pandas as pd
from typing import Dict, Any

from models import arima as arima_model
from models import prophet as prophet_model
from models import lstm as lstm_model
from config.settings import ENABLE_LSTM, ENABLE_PROPHET


def run_all_models(df: pd.DataFrame, horizon: int) -> Dict[str, Any]:
    """
    Run ARIMA (always), Prophet (if enabled/installed), LSTM (if enabled/installed).
    Returns:
        results    : {model_name: result_dict}
        errors     : {model_name: error_string}
        best_model : name with lowest RMSE
        comparison : pd.DataFrame sorted by RMSE
    """
    results, errors = {}, {}

    for name, mod, enabled in [
        ("ARIMA",   arima_model,   True),
        ("Prophet", prophet_model, ENABLE_PROPHET),
        ("LSTM",    lstm_model,    ENABLE_LSTM),
    ]:
        if not enabled:
            continue
        try:
            results[name] = mod.forecast(df, horizon)
        except Exception as e:
            errors[name] = str(e)

    rows = [{"Model": n, "RMSE": round(r.get("RMSE (norm)", 99.0),4), "MAE": round(r.get("MAE (norm)", 99.0),4)}
            for n, r in results.items()]
    comparison = pd.DataFrame(rows).sort_values("RMSE").reset_index(drop=True) if rows else pd.DataFrame()
    best_model = comparison.iloc[0]["Model"] if not comparison.empty else None

    return {
        "results":    results,
        "errors":     errors,
        "best_model": best_model,
        "comparison": comparison,
    }

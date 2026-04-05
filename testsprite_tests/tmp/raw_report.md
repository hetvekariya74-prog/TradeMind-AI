
# TestSprite AI Testing Report(MCP)

---

## 1️⃣ Document Metadata
- **Project Name:** files (4)
- **Date:** 2026-04-04
- **Prepared by:** TestSprite AI Team

---

## 2️⃣ Requirement Validation Summary

#### Test TC001 Load a valid asset and see Overview metrics plus Neon Quant chart
- **Test Code:** [TC001_Load_a_valid_asset_and_see_Overview_metrics_plus_Neon_Quant_chart.py](./TC001_Load_a_valid_asset_and_see_Overview_metrics_plus_Neon_Quant_chart.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/12f5c968-81e2-4bf8-b1a2-210f11ed5d84
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC002 Switching between multiple tabs does not break the base chart session
- **Test Code:** [TC002_Switching_between_multiple_tabs_does_not_break_the_base_chart_session.py](./TC002_Switching_between_multiple_tabs_does_not_break_the_base_chart_session.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/8cddbfe5-0b11-4459-a418-9033629a709b
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC003 View Raw Data table after loading an asset
- **Test Code:** [TC003_View_Raw_Data_table_after_loading_an_asset.py](./TC003_View_Raw_Data_table_after_loading_an_asset.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/21711bc8-3894-4e47-a713-bc51ea317907
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC004 Run an ARIMA forecast and see dashed overlay plus horizon metrics
- **Test Code:** [TC004_Run_an_ARIMA_forecast_and_see_dashed_overlay_plus_horizon_metrics.py](./TC004_Run_an_ARIMA_forecast_and_see_dashed_overlay_plus_horizon_metrics.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/c83b6dfb-bf8c-4239-9065-11b2d5c4fede
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC005 Run RSI backtest and see metrics plus equity curve vs Buy & Hold
- **Test Code:** [TC005_Run_RSI_backtest_and_see_metrics_plus_equity_curve_vs_Buy__Hold.py](./TC005_Run_RSI_backtest_and_see_metrics_plus_equity_curve_vs_Buy__Hold.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/e2895c76-353e-4cd1-a8b4-62549915f5aa
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC006 Compare all forecast models and see multiple distinct overlays
- **Test Code:** [TC006_Compare_all_forecast_models_and_see_multiple_distinct_overlays.py](./TC006_Compare_all_forecast_models_and_see_multiple_distinct_overlays.py)
- **Test Error:** TEST FAILURE

Running the 'Compare All Models' action did not produce the forecast overlays or comparison outputs because the app crashed with a KeyError.

Observations:
- The page shows a KeyError: 'rmse' traceback originating from models/comparator.py when running the comparison.
- No dashed-line forecast overlays or comparison result outputs/tables were rendered after clicking 'Compare All Models'.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/41e6692f-84e9-46f4-a266-f71dc5995ffb
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC007 Selected asset context persists when switching tabs
- **Test Code:** [TC007_Selected_asset_context_persists_when_switching_tabs.py](./TC007_Selected_asset_context_persists_when_switching_tabs.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/06a108bb-5240-4ef4-99ba-88a477972a36
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC008 Reloading with a different asset updates the primary chart
- **Test Code:** [TC008_Reloading_with_a_different_asset_updates_the_primary_chart.py](./TC008_Reloading_with_a_different_asset_updates_the_primary_chart.py)
- **Test Error:** TEST BLOCKED

The feature could not be reached — the app did not render and interactive controls are unavailable.

Observations:
- The page shows Streamlit loading skeletons and no usable controls.
- Only a single <section> element is interactive; no sidebar, market selector, asset selector, or chart controls are present.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/2a68ad43-f53e-42bb-9c50-9f6ea6cd9685
- **Status:** BLOCKED
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC009 Switch to Mean Reversion strategy and see outputs update
- **Test Code:** [TC009_Switch_to_Mean_Reversion_strategy_and_see_outputs_update.py](./TC009_Switch_to_Mean_Reversion_strategy_and_see_outputs_update.py)
- **Test Error:** TEST BLOCKED

The app did not finish rendering so the test cannot reach the Backtest features.

Observations:
- The page shows only loading skeleton placeholders and a single non-functional <section /> element.
- No interactive controls (market selector, tabs, buttons) were available after waiting.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/31a54ba8-590b-4418-91b9-ca255449f366
- **Status:** BLOCKED
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC010 Analyze pasted headlines to get per-item sentiment and aggregated news pulse
- **Test Code:** [TC010_Analyze_pasted_headlines_to_get_per_item_sentiment_and_aggregated_news_pulse.py](./TC010_Analyze_pasted_headlines_to_get_per_item_sentiment_and_aggregated_news_pulse.py)
- **Test Error:** TEST BLOCKED

The Streamlit app did not finish loading, so the Sentiment feature could not be reached.

Observations:
- The page shows skeleton placeholders instead of the application UI.
- Only one interactive element (<section>) is present and no tabs, text area, or sentiment controls are available.

- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/ffc3bce4-0969-4356-a9ea-dd0797991663
- **Status:** BLOCKED
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC011 Fetch and analyze recent headlines to render sentiment trend and news pulse
- **Test Code:** [TC011_Fetch_and_analyze_recent_headlines_to_render_sentiment_trend_and_news_pulse.py](./TC011_Fetch_and_analyze_recent_headlines_to_render_sentiment_trend_and_news_pulse.py)
- **Test Error:** TEST FAILURE

Fetching headlines and running analysis completed successfully and the News Pulse section is visible, but the aggregated sentiment trend visualization expected on the Sentiment tab was not found.

Observations:
- The 'Fetch & Analyze' action completed and the 'News Pulse' sub-tab shows the search input ("Bitcoin") and the 'Fetch & Analyze' button.
- No chart or heading labeled 'Sentiment Trend', 'Daily Sentiment', or similar was present on the Sentiment tab.
- The UI contains other chart-like sections (e.g., Indicator Snapshot, Price History) but none explicitly represent an aggregated sentiment trend.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/4a9b3647-745d-41f2-a5e5-c322ef1f2f13
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC012 Re-run sentiment analysis after editing pasted headlines updates results
- **Test Code:** [TC012_Re_run_sentiment_analysis_after_editing_pasted_headlines_updates_results.py](./TC012_Re_run_sentiment_analysis_after_editing_pasted_headlines_updates_results.py)
- **Test Error:** TEST BLOCKED

The app UI did not load so the sentiment feature could not be reached.

Observations:
- The page displays Streamlit loading skeleton placeholders instead of the Sentiment UI.
- Only one interactive element (<section>) was present; there were no input area, Run button, or tabs available.
- Two wait attempts (3s and 5s) were performed and the UI still did not finish loading.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/a7ef55c1-f070-476f-b26d-0cfcc2f4c05f
- **Status:** BLOCKED
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC013 Recover from empty-input validation by providing text and successfully analyzing
- **Test Code:** [TC013_Recover_from_empty_input_validation_by_providing_text_and_successfully_analyzing.py](./TC013_Recover_from_empty_input_validation_by_providing_text_and_successfully_analyzing.py)
- **Test Error:** TEST BLOCKED

The Sentiment/News analysis feature required by the test is not available on this page, so the empty-input validation and re-run steps cannot be executed.

Observations:
- No Sentiment or News tab, textarea, or analysis controls were found in the UI.
- The app shows the TradeMind AI forecasting interface (assets, time settings, 'Load & Analyze', and ARIMA/Prophet/LSTM mention) rather than a Sentiment/News analysis feature.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/84c54b12-8bee-4de6-9dff-44547a820bb6
- **Status:** BLOCKED
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC014 Invalid custom ticker shows validation error and avoids stale outputs
- **Test Code:** [TC014_Invalid_custom_ticker_shows_validation_error_and_avoids_stale_outputs.py](./TC014_Invalid_custom_ticker_shows_validation_error_and_avoids_stale_outputs.py)
- **Test Error:** TEST FAILURE

Loading an invalid custom ticker did not produce a validation error, and the app still shows the previously loaded BTC-USD metrics as if the invalid ticker had been ignored.

Observations:
- No validation/error message appeared after clicking '🚀  Load & Analyze' for the invalid ticker 'INVALIDTICKER123'.
- The main metrics area remains populated with BTC-USD values (Last Price $67,323.0859; 52W High $124,752.53; 52W Low $62,702.10; Ann. Volatility 36.7%; Data Points 366).
- The UI displays '✅ 1 asset(s) ready!' indicating the previous asset remains loaded.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/052aba27-662d-48f5-860d-3567b29f2774
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC015 Insufficient historical data for a model shows validation error
- **Test Code:** [TC015_Insufficient_historical_data_for_a_model_shows_validation_error.py](./TC015_Insufficient_historical_data_for_a_model_shows_validation_error.py)
- **Test Error:** TEST FAILURE

Running the forecast with a very small historical window did not show a validation error and produced forecast outputs instead.

Observations:
- After clicking 'Run Forecast' the page displays numerical forecast metrics (RMSE, MAE, MAPE).
- No "insufficient data" or similar validation error message is visible on the page.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/d3caada0-470b-4a2e-8afb-b06236e0ab9d/ceaac029-311a-461c-a3e1-da9b6f01dd6e
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---


## 3️⃣ Coverage & Matching Metrics

- **40.00** of tests passed

| Requirement        | Total Tests | ✅ Passed | ❌ Failed  |
|--------------------|-------------|-----------|------------|
| ...                | ...         | ...       | ...        |
---


## 4️⃣ Key Gaps / Risks
{AI_GNERATED_KET_GAPS_AND_RISKS}
---
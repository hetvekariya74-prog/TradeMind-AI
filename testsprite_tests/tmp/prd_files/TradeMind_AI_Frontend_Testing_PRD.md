# Frontend Testing PRD: TradeMind AI (Neon Quant Edition)

## 1. Product Overview
TradeMind AI is a professional financial analysis platform providing AI-driven trading signals, forecasts, and portfolio management. The current version features the **Neon Quant** design system—a glassmorphism, high-contrast dark aesthetic built with Streamlit and Plotly.

## 2. Testing Objectives
- Ensure the **Neon Quant** UI renders correctly without visual glitches.
- Verify that financial data loads successfully across different markets (Crypto, US Stocks, Nifty 50, Forex).
- Validate the core forecasting and backtesting workflows.
- Confirm that the pre-existing bugs (import names and timestamp arithmetic) remain fixed.

## 3. Scope of Testing

### 3.1. Visual & UI (Neon Quant Design System)
| Feature | Expected Behavior |
| :--- | :--- |
| **Global Theme** | Deep-space background (#0b0e14) with Space Grotesk/Inter typography. |
| **Glassmorphism Cards** | Floating cards with subtle borders and backdrop blur. |
| **Responsive Sidebar** | Logo renders correctly; selectboxes and sliders are functional. |
| **Chart Consistency** | Plotly charts must use the Neon Quant theme (dark background, minimal gridlines). |

### 3.2. Functional Modules
#### A. Asset Selection & Loading
- **Select Asset**: User can select multiple assets from pre-defined markets or enter custom tickers.
- **Load & Analyze**: Clicking the button fetches data via `yfinance` and populates the `Overview` and `Raw Data` tabs.
- **Progress Visibility**: A progress bar and status indicator (#10B981) should show loading state.

#### B. Technical Indicators
- **Tabs**: Line/Candlestick toggle functions.
- **Indicators**: RSI, MACD, and Bollinger Bands should render accurately with Neon Quant color encoding.

#### C. AI Forecasting (Critical Path)
- **Single Model**: ARIMA, Prophet, and LSTM models should run and produce a dashed-line forecast on the chart.
- **Model Comparison**: Clicking "Compare All Models" must run all three without the "run_all_models" name error.
- **Error Handling**: Failed forecasts should display a Streamlit error message with debug info.

#### D. Backtesting
- **Execution**: Selecting a strategy and clicking "Run Backtest" generates a metrics dashboard.
- **Equity Curve**: The curve should show performance comparison against Buy & Hold.

#### E. Sentiment Analysis
- **Text Area**: User can paste news; "Analyze Sentiment" returns polarity and subjectivity.
- **News Pulse**: Fetches real-time headlines and performs bulk sentiment analysis.

### 3.3. Technical Edge Cases (Regression)
- **Timestamp Arithmetic**: Forecasting charts must not crash with "Timestamp + integer" TypeError (Fixed: converted to str).
- **Function Names**: `run_all_models` call in `app.py` is verified (Fixed: from `run_all`).

## 4. Test Environment
- **Browser**: Chrome/Edge/Firefox (Modern versions).
- **Screen Size**: Desktop (Main focus) and Tablet.
- **Local Port**: 8501 (Streamlit Default).

## 5. Success Criteria
- ✅ 100% pass rate on "Load & Analyze" for major tickers (BTC-USD, AAPL).
- ✅ Forecasting functionality verified for ARIMA and Prophet.
- ✅ No visual overlap or CSS breaking in Neon Quant cards.
- ✅ All Plotly charts maintain the dark `CT` dictionary configuration.

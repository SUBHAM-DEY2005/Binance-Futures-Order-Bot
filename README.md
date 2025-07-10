# Binance-Futures-Order-Bot
Objective  Develop a CLI-based trading bot for Binance USDT-M Futures that supports multiple order types  with robust logging, validation, and documentation. 
Key Responsibilities
 1. Core Orders (Mandatory)
  MarketOrders
  LimitOrders
 2. Advanced Orders (Bonus– Higher Priority in Evaluation)
  Stop-Limit Orders (e.g., trigger a limit order when a stop price is hit)
  OCO(One-Cancels-the-Other) (e.g., place a take-profit and stop-loss simultaneously)
  TWAP(Time-WeightedAverage Price) (e.g., split large orders into smaller chunks over time)
  GridOrders(e.g., automated buy-low/sell-high within a price range)
 3. Validation & Logging
  Validate inputs (symbol, quantity, price thresholds).
  Logallactions (order placement, errors, executions) in a structured log file

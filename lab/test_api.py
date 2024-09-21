"""
## Stock market API

1. Pricing - Free, API call limits
2. Data coverage - Stock(price, volume), Company financials, News, Historical data
3. (near) Real-time data
4. Documentation (Support), Policies


https://medium.com/coinmonks/best-stock-market-apis-ae1efb739ac4

A.

Yahoo Finance API - Free
https://developer.yahoo.com/api/

IEX Cloud API - 100call/day
https://iexcloud.io/docs/api/


B.

Polygon.io  - Free, 5call/min
https://polygon.io/pricing

Tiingo API - Free, 1000call/day
https://www.tiingo.com/


C.

Alpha Vantage API - 500call/day
https://www.alphavantage.co/

Quandl API - 500call/day
https://data.nasdaq.com/publishers/QDL


"""

# A. Yahoo Finance API
# pip install yfinance


import yfinance as yf
from datetime import datetime

ticker = "AAPL"

# Daily
result = yf.Ticker(ticker)
# print(result.info)

# period: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max (optional, default is '1mo')
# interval: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo(optional, default is '1d')
apple = yf.download(tickers="AAPL", period="5d", interval="1m")

start = datetime(2024, 8, 1, 9, 30, 0)
end = datetime(2024, 8, 1, 11, 30, 0)

filtered = apple[start: end]


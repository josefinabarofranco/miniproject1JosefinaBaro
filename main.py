## NF601 - Advanced Programming in Python
## Josefina Baro
## Mini Project 1

import pprint
import yfinance as yf

mytickers = ["SNAP" , "GOOGL" , "LYFT" , "ROKU" , "META"]
mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    print(f"Ticker: {ticker} \tDay High: {result.info['dayHigh']}")

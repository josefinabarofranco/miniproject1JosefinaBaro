## NF601 - Advanced Programming in Python
## Josefina Baro
## Mini Project 1

import pprint
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import copy

today = datetime.now()
##(5/5 points) Initial comments with your name, class and project at the top of your .py file.
##(5/5 points) Proper import of packages used.
##(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
##(10/10 points) Store this information in a list that you will convert to an array in NumPy.
##(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
##(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
##(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
##(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
##(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

ten_days_ago = today - timedelta(days=15)
mytickers = ["SNAP" , "GOOGL" , "LYFT" , "ROKU" , "META"]
mytickers.sort()

for ticker in mytickers:
    result = yf.Ticker(ticker)
    history = result.history(start = ten_days_ago, end = datetime.now())

    closingList = []

    for date in history["Close"][:11]:
        closingList.append(date)
    stockarray = np.array(closingList)
    maxprice = stockarray.max() + (stockarray.max()*.05)
    minprice = stockarray.min() - (stockarray.min() * .05)
    plt.plot(stockarray)
    plt.title(f"{ticker} Stock Closing Price - Last 10 Days")
    plt.xlabel("Days Ago")
    plt.ylabel("Closing Price")
    plt.axis((9,0, minprice, maxprice))
    plt.show()
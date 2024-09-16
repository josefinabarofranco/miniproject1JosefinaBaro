## NF601 - Advanced Programming in Python
## Josefina Baro
## Mini Project 1

import pprint
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

##(5/5 points) Initial comments with your name, class and project at the top of your .py file.
##(5/5 points) Proper import of packages used.
##(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
##(10/10 points) Store this information in a list that you will convert to an array in NumPy.
##(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
##(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
##(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
##(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
##(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

mytickers = ["SNAP" , "GOOGL" , "LYFT" , "ROKU" , "META"]
mytickers.sort()

for ticker in mytickers:
    result = yf.Ticker(ticker)
    history = result.history(period="5d")

    closingList = []

    for price in history["Close"]:
        closingList.append(price)
    print(closingList)

    stockarray = np.array(closingList)

    plt.plot(stockarray)
    plt.title(f"{ticker} Stock Closing Prices")
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    plt.show()
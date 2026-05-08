import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

stocks = {
    "RELIANCE.NS": [10, 2500],
    "TCS.NS": [5, 3200]
}

data_list = []

for stock in stocks:

    ticker = yf.Ticker(stock)

    current_price = ticker.info["currentPrice"]

    shares = stocks[stock][0]
    buy_price = stocks[stock][1]

    invested = shares * buy_price
    current_value = shares * current_price

    profit = current_value - invested

    return_percent = (profit / invested) * 100

    data_list.append([
        stock,
        invested,
        current_value,
        profit,
        return_percent
    ])

df = pd.DataFrame(data_list, columns=[
    "Stock",
    "Invested",
    "Current Value",
    "Profit",
    "Return %"
])

print(df)

total_investment = df["Invested"].sum()
total_value = df["Current Value"].sum()

print("\nTotal Investment:", total_investment)
print("Current Value:", total_value)

overall_return = ((total_value - total_investment) / total_investment) * 100

print("Portfolio Return:", round(overall_return, 2), "%")

plt.bar(df["Stock"], df["Profit"])

plt.title("Profit/Loss of Stocks")

plt.xlabel("Stocks")
plt.ylabel("Profit")

plt.show()

# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock = input(f"Enter stock {i+1} name: ").upper()
    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

print("\nPortfolio Summary")
print("-" * 30)

for stock, quantity in portfolio.items():
    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"{stock}: {quantity} x ${stock_prices[stock]} = ${value}")
    else:
        print(f"{stock}: Price not available")

print("-" * 30)
print(f"Total Investment Value = ${total_investment}")

with open("portfolio_summary.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-" * 30 + "\n")
    for stock, quantity in portfolio.items():
        if stock in stock_prices:
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} x ${stock_prices[stock]} = ${value}\n")
        else:
            file.write(f"{stock}: Price not available\n")
    file.write("-" * 30 + "\n")
    file.write(f"Total Investment Value = ${total_investment}\n")

print("Summary saved to portfolio_summary.txt")

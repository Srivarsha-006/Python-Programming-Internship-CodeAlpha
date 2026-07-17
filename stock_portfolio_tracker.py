# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 410
}

# Step 2: Show available stocks to the user
print("Available stocks and prices:")
for stock in stock_prices:
    print(stock, "-", stock_prices[stock])

# Step 3: Ask user how many different stocks they want to enter
num_stocks = int(input("\nHow many different stocks do you want to enter? "))

# Step 4: Create an empty dictionary to store user's stocks and quantity
my_portfolio = {}

# Step 5: Take input from user in a loop
for i in range(num_stocks):
    name = input("Enter stock symbol: ").upper()
    if name in stock_prices:
        qty = int(input("Enter quantity: "))
        my_portfolio[name] = qty
    else:
        print("Sorry, we don't have the price for", name)

# Step 6: Calculate total investment
total = 0
print("\n----- YOUR PORTFOLIO -----")
for stock in my_portfolio:
    qty = my_portfolio[stock]
    price = stock_prices[stock]
    value = qty * price
    total = total + value
    print(stock, ":", qty, "shares x $", price, "= $", value)
print("---------------------------")
print("TOTAL INVESTMENT VALUE: $", total)

# Step 7: Ask if user wants to save the result to a file
save = input("\nDo you want to save this to a file? (y/n): ")
if save == "y":
    file = open("portfolio.txt", "w")
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("-------------------------\n")

    for stock in my_portfolio:
        qty = my_portfolio[stock]
        price = stock_prices[stock]
        value = qty * price
        file.write(stock + ": " + str(qty) + " shares x $" + str(price) + " = $" + str(value) + "\n")

    file.write("-------------------------\n")
    file.write("TOTAL INVESTMENT VALUE: $" + str(total) + "\n")
    file.close()
    print("Saved to portfolio.txt")
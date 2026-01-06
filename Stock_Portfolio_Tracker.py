# Advanced Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 310
}

# Simulated current market prices
current_prices = {
    "AAPL": 195,
    "TSLA": 230,
    "GOOGL": 150,
    "MSFT": 320
}

portfolio = {}

def show_stocks():
    print("\n📈 Available Stocks")
    for stock, price in stock_prices.items():
        print(f"{stock} → Buy Price: ${price}")

def buy_stock():
    stock = input("Enter stock name: ").upper()
    if stock not in stock_prices:
        print("❌ Stock not available!")
        return

    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("⚠ Quantity must be positive!")
            return
    except ValueError:
        print("⚠ Enter a valid number!")
        return

    if stock in portfolio:
        portfolio[stock]["quantity"] += qty
    else:
        portfolio[stock] = {
            "quantity": qty,
            "buy_price": stock_prices[stock]
        }

    print(f"✅ Bought {qty} shares of {stock}")

def view_portfolio():
    if not portfolio:
        print("📭 Portfolio is empty")
        return

    print("\n📊 Portfolio Summary")
    total_investment = 0
    total_current_value = 0

    for stock, data in portfolio.items():
        qty = data["quantity"]
        buy = data["buy_price"]
        current = current_prices[stock]

        invested = qty * buy
        current_value = qty * current
        profit_loss = current_value - invested

        total_investment += invested
        total_current_value += current_value

        print(f"{stock} | Qty: {qty} | P/L: ${profit_loss}")

    print("\n💰 Total Invested:", total_investment)
    print("📈 Current Value:", total_current_value)
    print("📊 Net P/L:", total_current_value - total_investment)

def save_to_file():
    with open("portfolio.txt", "w") as file:
        file.write("Advanced Portfolio Report\n\n")
        for stock, data in portfolio.items():
            file.write(f"{stock} - {data['quantity']} shares\n")
    print("📁 Portfolio saved successfully!")

while True:
    print("""
========= MENU =========
1. Show Available Stocks
2. Buy Stock
3. View Portfolio & Profit/Loss
4. Save Portfolio
5. Exit
========================
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_stocks()
    elif choice == "2":
        buy_stock()
    elif choice == "3":
        view_portfolio()
    elif choice == "4":
        save_to_file()
    elif choice == "5":
        print("👋 Thank you for using Portfolio Tracker")
        break
    else:
        print("❌ Invalid choice!")
        

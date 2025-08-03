def stock_portfolio_tracker():
    # Hardcoded stock prices (symbol: price)
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "MSFT": 300.25,
        "AMZN": 120.80,
        "GOOGL": 135.40
    }
    
    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    portfolio = {}
    while True:
        print("\n1. Add stock to portfolio")
        print("2. View portfolio and total value")
        print("3. Save portfolio to file")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            # Add stock to portfolio
            stock_symbol = input("Enter stock symbol: ").upper()
            
            if stock_symbol not in stock_prices:
                print("Invalid stock symbol. Available stocks are:", ", ".join(stock_prices.keys()))
                continue
                
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                    
                portfolio[stock_symbol] = portfolio.get(stock_symbol, 0) + quantity
                print(f"Added {quantity} shares of {stock_symbol} to portfolio.")
                
            except ValueError:
                print("Please enter a valid number for quantity.")
                
        elif choice == "2":
            # View portfolio and calculate total value
            if not portfolio:
                print("Your portfolio is empty.")
                continue
                
            total_value = 0
            print("\nYour Portfolio:")
            print("-" * 30)
            print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Value':<10}")
            print("-" * 30)
            
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = qty * price
                total_value += value
                print(f"{stock:<10}{qty:<10}${price:<10.2f}${value:<10.2f}")
                
            print("-" * 30)
            print(f"Total Portfolio Value: ${total_value:.2f}")
            
        elif choice == "3":
            # Save portfolio to file
            if not portfolio:
                print("Portfolio is empty. Nothing to save.")
                continue
                
            filename = input("Enter filename to save (e.g., portfolio.txt): ")
            try:
                with open(filename, 'w') as f:
                    f.write("Stock,Quantity,Price,Value\n")
                    total_value = 0
                    for stock, qty in portfolio.items():
                        price = stock_prices[stock]
                        value = qty * price
                        total_value += value
                        f.write(f"{stock},{qty},{price:.2f},{value:.2f}\n")
                    f.write(f"Total Value,{total_value:.2f}\n")
                print(f"Portfolio saved to {filename}")
            except IOError:
                print("Error saving file.")
                
        elif choice == "4":
            # Exit
            print("Exiting portfolio tracker.")
            break
            
        else:
            print("Invalid choice. Please enter 1-4.")

# Start the tracker
stock_portfolio_tracker()
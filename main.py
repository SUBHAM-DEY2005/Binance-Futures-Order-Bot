from bot import BasicBot

# Use your Testnet API credentials here
API_KEY = "UfIdUecN79r2aAfxKhQJyfvmEj5YOAK0a2dtubERa3nCxhZsvpkcSM5CHfFNSgci"
API_SECRET = "XhOAK0xBdcuN9UvAlCU20e6z5S4B9mMYDIl4nFczgD65lsN0T3YxG7ZWvHLHURgA"

# Initialize bot
bot = BasicBot(API_KEY, API_SECRET)

def main():
    print("="*50)
    print("🚀 Welcome to the Binance Futures Trading Bot")
    print("="*50)

    try:
        symbol = input("Enter trading symbol (e.g., BTCUSDT): ").upper()
        order_type = input("Enter order type (market / limit / stop-limit): ").lower()
        side = input("Enter side (buy / sell): ").lower()
        quantity = float(input("Enter quantity: "))

        result = None

        if order_type == "market":
            result = bot.place_market_order(symbol, side, quantity)

        elif order_type == "limit":
            price = float(input("Enter limit price: "))
            result = bot.place_limit_order(symbol, side, quantity, price)

        elif order_type == "stop-limit":
            stop_price = float(input("Enter stop price: "))
            price = float(input("Enter limit price: (can be same as stop price): "))
            result = bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)

        else:
            print("❌ Invalid order type")
            return

        print("\n📦 Order Result:")
        if "error" in result:
            print("⚠️ API Error:", result["error"])
        else:
            print("✅ Order placed successfully!")
            print(result)

    except Exception as e:
        print("❌ Something went wrong:", e)

if __name__ == "__main__":
    main()

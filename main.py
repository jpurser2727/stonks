from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import requests

trading_client = TradingClient('PKMQGYGTKMC12SFWTN3I', 'F76bIs9ivEObpks1gcb6wHa00AqxsEfXTcMZmDkC', paper=True)


# Define the ISS location API endpoint
def get_iss_longitude():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    return float(data['iss_position']['longitude'])

# Initialize a dictionary to keep track of stock holdings
myDict = {
    "LMT": (-10000, -40),  
    "HD": (-40, 20),    
    "LMT": (20, 10000) 
}
def main():
    iss_longitude = get_iss_longitude()
    print(get_iss_longitude())

    if -60 <= iss_longitude <= -40:
        # Buy 5 shares of Lockheed Martin stock
        print("working")
        market_order_data = MarketOrderRequest(
            symbol="LMT",
            qty=5,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY
        )
        market_order = trading_client.submit_order(
            order_data=market_order_data
        )

    elif -40 < iss_longitude <= -20:
        # sell 2 shares of Lockheed Martin stock
        print("working")
        market_order_data = MarketOrderRequest(
            symbol="LMT",
            qty=2,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY
        )
        market_order = trading_client.submit_order(
            order_data=market_order_data
        )

    elif -20 < iss_longitude <= 0:
        print("working")
        # Buy 5 shares of Lockheed Martin stock
        print("working")
        market_order_data = MarketOrderRequest(
            symbol="HD",
            qty=5,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY
        )
        market_order = trading_client.submit_order(
            order_data=market_order_data
        )

    elif 0 < iss_longitude <= 20:
        print("working")
        # Buy 5 shares of Lockheed Martin stock
        print("working")
        market_order_data = MarketOrderRequest(
            symbol="LMT",
            qty=2,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY
        )
        market_order = trading_client.submit_order(
            order_data=market_order_data
        )

    elif 20 < iss_longitude <= 100:
        print("working")
        # Buy 5 shares of Lockheed Martin stock
        market_order_data = MarketOrderRequest(
            symbol="LMT",
            qty=2,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY
        )
        market_order = trading_client.submit_order(
            order_data=market_order_data
        )
    elif iss_longitude <= -60:
        print("working")
        # Buy 2 shares of Lockheed Martin stock
        print("working")
        market_order_data = MarketOrderRequest(
            symbol="LMT",
            qty=2,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY
        )
        market_order = trading_client.submit_order(
            order_data=market_order_data
        )
    elif iss_longitude >=100:
        print("working")
        # Buy 2 shares of Lockheed Martin stock
        print("working")
        market_order_data = MarketOrderRequest(
            symbol="LMT",
            qty=2,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY
        )
        market_order = trading_client.submit_order(
            order_data=market_order_data
        )

if __name__ == '__main__':
    main()

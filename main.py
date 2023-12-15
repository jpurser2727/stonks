import requests
from alpaca.trading.client import TradingClient

# Set up your Alpaca API credentials
ALPACA_API_KEY = 'PKZ9FFDTB1MJGB2J8BT3'
ALPACA_SECRET_KEY = 'KOP9jOMhyfwrs5dKlPrD9yM9knBbkmfldW8kVK1O'

# Initialize the Alpaca trading client for paper trading
trading_client = TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY, paper=True)

# Define the ISS location API endpoint
def get_iss_longitude():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    return float(data['iss_position']['longitude'])

# Initialize a dictionary to keep track of stock holdings
myDict = {
    'LMT': 0,  
    'HD': 0    
}

def main():
    while True:
        iss_longitude = get_iss_longitude()
        
        
        if -60 <= iss_longitude <= -40:
            # Buy 5 shares of Lockheed Martin stock
            print("working")
            trading_client.submit_order(
                symbol='LMT',
                qty=5,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            myDict['LMT'] += 5
        elif -40 < iss_longitude <= -20:
            # Sell 2 shares of Lockheed Martin stock
            if myDict['LMT'] >= 2:
                trading_client.submit_order(
                    symbol='LMT',
                    qty=2,
                    side='sell',
                    type='market',
                    time_in_force='gtc'
                )
                myDict['LMT'] -= 2
        elif -20 < iss_longitude <= 0:
            # Buy 5 shares of Home Depot stock
            trading_client.submit_order(
                symbol='HD',
                qty=5,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            myDict['HD'] += 5
        elif 0 < iss_longitude <= 20:
            # Sell 2 shares of Home Depot stock
            if myDict['HD'] >= 2:
                trading_client.submit_order(
                    symbol='HD',
                    qty=2,
                    side='sell',
                    type='market',
                    time_in_force='gtc'
                )
                myDict['HD'] -= 2
        elif 20 < iss_longitude <= 100:
            
            print("working")
            trading_client.submit_order(
                symbol='LMT',
                qty=2,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            myDict['LMT'] += 2

if __name__ == '__main__':
    main()

"""alpaca_api_key = 'PKZ9FFDTB1MJGB2J8BT3'
alpaca_secret_key = 'KOP9jOMhyfwrs5dKlPrD9yM9knBbkmfldW8kVK1O'
"""

from datetime import datetime, timedelta
from alpaca.trading.client import TradingClient

import requests

# API endpoint for current ISS location
url = "http://api.open-notify.org/iss-now.json"

# Send a GET request to the API
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract latitude and longitude
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

# Print the current ISS location
print(f"Current ISS Location: Latitude {latitude}, Longitude {longitude}")



"""alpaca_api_key = 'PKZ9FFDTB1MJGB2J8BT3'
alpaca_secret_key = 'KOP9jOMhyfwrs5dKlPrD9yM9knBbkmfldW8kVK1O'
"""
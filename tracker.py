import requests
import time
from datetime import datetime

# Telegram API token and chat ID
token = 'your telegram token'
chat_id = 'your telegram chat id'

# Coinmarketcap API endpoint
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Coinmarketcap API parameters
params = {
    'symbol': 'BTC',
    'convert': 'USD'
}

headers = {
    'X-CMC_PRO_API_KEY': 'Your API code'
}

while True:
    # Make API request
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    price = data['data']['BTC']['quote']['USD']['price']

    # Send Telegram message
    message = f'Bitcoin price is ${price:.2f} as of {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}')

    # Sleep for 5 minutes
    time.sleep(300)
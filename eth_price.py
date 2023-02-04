import requests
from bs4 import BeautifulSoup
import json


cmc = requests.get(f"https://coinmarketcap.com/currencies/ethereum")
soup = BeautifulSoup(cmc.content, 'html.parser')
data = soup.find('script', id="__NEXT_DATA__", type="application/json")
coin_data = json.loads(data.contents[0])

info = coin_data['props']['quotesLatestData']
eth_data = next(item for item in info if item["symbol"] == "ETH")
price = eth_data['p']

print("The current price of ethereum is " + str(price))

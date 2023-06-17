Query Parameters
import requests as r
url='https://api.coinbase.com/v2/exchange-rates?currency=btc'
resp = r.get(url)
resp.json()['data']['rates']['USD']

url = 'https://api.coinbase.com/v2/exchange-rates'
params = {'currency':'BTC'}
resp = r.get(url,params=params)
resp.json()['data']['rates']['USD']

import requests as r
from bs4 import  BeautifulSoup
# def get_price_information(ticket,exchange):
proxy={'schema' : 'http', 'address' :'167.172.96.117:38295'}
url = (f'https://www.google.com/finance/quote/MSFT:NASDAQ')
resp = r.get(url,proxies=proxy)
soup = BeautifulSoup(resp.content,'html.parser')
price_div = soup.find('div',attrs = {'data-last-price': True})
print(soup)

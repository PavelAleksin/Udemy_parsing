import requests as r
from bs4 import  BeautifulSoup

def get_price_information(ticket,exchange):
    proxy={86.98.0.231:8080}
    url = f'https://www.google.com/finance/quote/{ticket}:{exchange}'
    resp = r.get(url,proxies=)
    resp.status_code
    soup = BeautifulSoup(resp.content,'html.parser')

    price_div = soup.find('div',attrs = {'data-last-price': True})
    return price_div,url

print(get_price_information('MSFT','NASDAQ'))

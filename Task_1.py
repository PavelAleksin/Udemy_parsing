import requests as r
from bs4 import BeautifulSoup
import re
resp = r.get('https://books.toscrape.com/')
soup = BeautifulSoup(resp.content) 
print(f'Статус запроса:{resp.status_code}')
len(soup.find_all())

#1 вариант очистка от символа валюты и перевод во Float
def clean_price(price):
    return float(''.join([char for char in price if char.isdigit() or char == '.']))

#2 вариант(cost) очистка от символа валюты и перевод во Float
def clean_price2(price):
    return float(re.sub('[^0-9.]','',price))

def convert_rating(ratings):
    rating={
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }
    return rating[ratings]


def extract_book(book):
    title = book.find('h3').find('a')['title']
    price = book.find('p',attrs={'class':'price_color'}).text #replace('£','')
    stats = book.find('p',attrs={'class':f'star-rating'})['class'][-1]
    return {
            'title':title,
            'price':clean_price(price),
            'stats':convert_rating(stats)
    }

books = soup.find_all('article',attrs={'class':'product_pod'})
books_data = [extract_book(books) for books in books]

books_data
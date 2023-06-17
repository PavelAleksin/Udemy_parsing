import requests as r
from bs4 import BeautifulSoup
resp = r.get('https://books.toscrape.com/')
resp.content
soup = BeautifulSoup(resp.content) #lxml
# type(soup)
# soup.title
# print(soup.prettify())
# soup.name
#------------------------------------------
# soup.h1
# first_div = soup.div
# first_div.find
# soup.div
# soup.ul
# print(soup.ul.prettify())
# list(soup.ul.children)
# from bs4.element import NavigableString
# list(filter(lambda x: type(x) != NavigableString,soup.ul.children))
# def no_nav_strings(iterable):
#     return list(filter(lambda x: type(x) != NavigableString,iterable))
# no_nav_strings(soup.ul.children)
# list(soup.ul.descendants)
# desc = no_nav_strings(soup.ul.descendants)
# desc[0]
# desc[0].parent
#---------------------------------------------
# soup.ul.li
# soup.ul.li\
#         .next_sibling\
#             .next_sibling\
#                 .previous_sibling
# soup.a
# soup.a.get_text()
# soup.a.string
# soup.a.text
# soup.ul.get_text()
# soup.ul.string
# soup.ul.text
# print(soup.a.text,'of type',type(soup.a.text))
# print(soup.a.get_text(),'of type',type(soup.a.get_text()))
# print(soup.a.string,'of type',type(soup.a.string))
#soup.ul.get_text(separator=',',strip=True)
# soup.stripped_strings
# all_string = list(soup.stripped_strings)
# len(all_string)
# len(list(soup.strings))
# list(soup.strings)[:5]
#--------------------------------------------find--find_all---------------------------
# soup.find_all()
# len(soup.find_all())
# soup.find_all('a')
# len(soup.find_all('a'))
# len(soup.find_all(['a','p']))
#-------------------------------------------------
# tag_name: p
# attr:class=price_color
# price_tags = soup.find_all('p',attrs={'class':'price_color'})
# [price.get_text() for price in price_tags]
# price_tags = soup.find_all('p',class_='price_color')
# [price.get_text() for price in price_tags]
# add_buttons = soup.find_all('button',attrs={'data-loading-text':'Adding...'})
# len(add_buttons)
# add_buttons = soup.find_all('button',
#                             attrs={'data-loading-text':lambda x: 'add' in x.lower() or 'remove' in x.lower()})
# len(add_buttons)


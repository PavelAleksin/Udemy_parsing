import requests as r
from bs4 import BeautifulSoup
resp = r.get('https://books.toscrape.com/')
resp.content
soup = BeautifulSoup(resp.content) #lxml
type(soup)
soup.title
print(soup.prettify())
soup.name
------------------------------------------
soup.h1
first_div = soup.div
first_div.find
soup.div
soup.ul
print(soup.ul.prettify())
list(soup.ul.children)
from bs4.element import NavigableString
list(filter(lambda x: type(x) != NavigableString,soup.ul.children))
def no_nav_strings(iterable):
    return list(filter(lambda x: type(x) != NavigableString,iterable))
no_nav_strings(soup.ul.children)
list(soup.ul.descendants)
desc = no_nav_strings(soup.ul.descendants)
desc[0]
desc[0].parent
---------------------------------------------
soup.ul.li
soup.ul.li\
        .next_sibling\
            .next_sibling\
                .previous_sibling
soup.a
soup.a.get_text()
soup.a.string
soup.a.text
soup.ul.get_text()
soup.ul.string
soup.ul.text
print(soup.a.text,'of type',type(soup.a.text))
print(soup.a.get_text(),'of type',type(soup.a.get_text()))
print(soup.a.string,'of type',type(soup.a.string))
soup.ul.get_text(separator=',',strip=True)

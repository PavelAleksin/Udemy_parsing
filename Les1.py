# URLLIB
from urllib.request import  urlopen
url = 'https://quotes.toscrape.com/'
resp = urlopen(url)
# print(resp)
resp.status
content = resp.read()
# print(content)
# print(content.decode('utf-8'))
with urlopen(url) as resp:
    content = resp.read()
    print(content.decode('utf-8'))
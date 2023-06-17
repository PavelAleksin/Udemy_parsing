#SEARCH TO CSS

books_tags = soup.find_all('article', attrs={'class':'product_pod'})
titles=[]
for tag in books_tags:
    title = tag.find('h3').find('a')['title']
    titles.append(title)
titles

--------------------------------------------------------------------------

title_tags = soup.select('article.product_pod>h3>a')
titles = [tag['title'] for tag in title_tags]
titles

soup.select('[title]')
soup.select('[title*=Human]')
soup.select('button.btn-primary[data-loading-text][class*=primary]')
len(soup.select('button.btn-primary[data-loading-text][class*=primary]'))
soup.select('button')
-----------------------------------------------------------------------------------

#find_all() vs find() / select() vs select_one()

soup.find_all('a',limit=1)
soup.find('a')
soup.find_all('a',limit=1)[0] is soup.find('a') # True

soup.select('a',limit=1)
soup.select_one('a')
soup.select('a',limit=1)[0] is soup.select_one('a') #True
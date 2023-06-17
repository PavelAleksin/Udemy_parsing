soup.find_all(id='messages')
len(soup.find_all(attrs={'id':lambda x: x is not None}))
len(soup.find_all(id = lambda x: x is not None))
len(soup.find_all(lambda x : x.has_attr('id')))
soup.find_all(lambda x : x.has_attr('id'))
def fiction_category_anchor(tag):
    return tag.name == 'a' and 'category' in tag['href'] and 'Fiction' in tag.text

soup.find_all(fiction_category_anchor)
soup.find_all(id='messages')
len(soup.find_all(attrs={'id':lambda x: x is not None}))
len(soup.find_all(id = lambda x: x is not None))
len(soup.find_all(lambda x : x.has_attr('id')))
soup.find_all(lambda x : x.has_attr('id'))
def fiction_category_anchor(tag):
    return tag.name == 'a' and 'category' in tag['href'] and 'Fiction' in tag.text

soup.find_all(fiction_category_anchor)
len(soup.find_all(fiction_category_anchor))
# PANDAS
sum([books['price'] for books in books_data])/len(books_data)
# цена меньше 20 долларов
[books['title'] for books in books_data if books['price'] < 20] 

import pandas as pd

df = pd.DataFrame(books_data)
df.price.mean() # среднее значение
df[df.price < 20] # цена меньше 20$
df.to_csv('book.csv',index=False) #запись в CSV
df.to_json('books.json',orient= 'records')

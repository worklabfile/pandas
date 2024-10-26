import pandas as pd

# В данных  которые я получил на Яндекс Вордстате https://ya.ru/ https://wordstat.yandex.ru/ разделитель ; а не ,

books = pd.read_csv('data/book_top_search.csv',delimiter=';') # указываем дополнительно разделитель delimiter

print(books.shape)
print(books)







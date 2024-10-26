import pandas as pd

# В данных  которые я получил на Яндекс Вордстате https://ya.ru/ https://wordstat.yandex.ru/ разделитель ; а не ,

books = pd.read_csv('data/book_top_search.csv',delimiter=';') # указываем дополнительно разделитель delimiter

print(books.shape)
print(books)

books.head().to_csv('data/five_books.csv') #записали первые пять строк в csv файл

# print(books.iloc[0][0]) #получение формулировки самого популярного запроса
# print(books.loc[:,'Число запросов']) #получение всех строк для столбца Число запросов
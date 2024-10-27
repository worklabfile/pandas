import pandas as pd 

wines = pd.read_csv('data/wine.csv', index_col=0)

columns = ['country','province','region_1', 'region_2']

indeces = [0,1,10,100]

top_oceania_wines = wines.loc[(wines.points>=95) & (wines.country.isin(['Australia','New Zealand']))]

mean_point = wines.points.mean()

# def remean_points(row):
#     row.points = row.points - mean_point
#     return row

# x = wines.apply(remean_points, axis = 'columns')

# print(x.points) 

maxbargain = (wines.points/wines.price).idxmax()
bargain_wine = wines.loc[maxbargain,'title']

print(bargain_wine)

fruity_count = wines.description.map(lambda d: 'fruity' in d).sum()
tropical_count = wines.description.map(lambda d: 'tropical' in d).sum()

x = pd.Series([tropical_count,fruity_count],index = ['tropical','fruity'])

print(x)

# Оценка 95 или выше + Канада засчитывается как 3 звезды,
# оценка не менее 85, но менее 95 - 2 звезды. Любая другая оценка - 1 звезда.

# def stars(row):
#     if(row.points>=95 or row.country == 'Canada'):
#         return 3
#     elif(row.points>=85):
#         return 2
#     else:
#         return 1

# x = wines.apply(stars, axis='columns')

# print(x)

x = wines.groupby('points').points.count()

x = wines.groupby('points').price.max()

x = wines.groupby('winery').apply(lambda df: df.iloc[0].title)

x = wines.groupby(['points','country']).price.min()

x = wines.groupby(['points','country']).apply(lambda df: df.loc[df.points.idxmax()])

x = wines.groupby('points').price.agg([len,min,max])

x = wines.sort_values(by='price', ascending=False)

x = wines.groupby('taster_twitter_handle').size()

# Какое вино самое лучшее, которое я могу купить за данную сумму денег?
# Создайте серию, индексом которой будут цены на вина, а значениями - максимальное количество баллов,
# которое было присвоено в обзоре вину стоимостью столько-то. Отсортируйте значения по цене по возрастанию
# (так, чтобы вверху было 4,0 доллара, а внизу - 3300,0 доллара).

# x = wines.groupby('price').points.max()

# x = wines.groupby('variety').price.agg([min,max])

# x = wines.groupby(['country','variety']).size().sort_values(ascending=False)

# x = wines[pd.isnull(wines.country)]

# print(x)

# x.country = x.country.fillna('Неизвестно')

# print(x)

x = wines.country.replace('France','Russia')


wines.region_1 = wines.region_1.fillna('Unknown')

x = wines.groupby('region_1').size().sort_values(ascending=False)

x = wines.rename(columns={'country':'страна'})


print(x)
import pandas as pd 

wines = pd.read_csv('data/wine.csv', index_col=0)

columns = ['country','province','region_1', 'region_2']

indeces = [0,1,10,100]

top_oceania_wines = wines.loc[(wines.points>=95) & (wines.country.isin(['Australia','New Zealand']))]

mean_point = wines.points.mean()

def remean_points(row):
    row.points = row.points - mean_point
    return row

x = wines.apply(remean_points, axis = 'columns')

print(x.points) 


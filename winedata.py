import pandas as pd 

wines = pd.read_csv('data/wine.csv', index_col=0)

print(wines)
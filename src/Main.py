# encoding=utf-8
import pandas as pd

df= pd.read_csv('Daily_2018_03_12.csv')
print(type(df))
#print(df.shape[0])
print(df.index)
#print(df.columns)
#print( df['MTX    '])
MTX=df[df['MTX    ']=='MTX    ']
print(MTX.columns)
print(MTX.iloc[:,4:6])

pd.read_html
pd.read_json()
pd.read_html()

import numpy as np
import pandas as pd
s=[10,40,50,44,90,21]
print(s.head())
print(s.tail())
print(s.sample(3))#sample
# s.value_counts()
s.sort_values(ascending=False)
B=[10,30,60,77,98]
s2=pd.Series(B)
# s2.sort_index(ascending=False)
print(s2.sort_values().head(1).values[0])
#customized index
Score=[87,43,56,78,31]
Name=['a','c','d','e','z']
S=pd.Series(Score,index=Name)
print(S)
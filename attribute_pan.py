import numpy as np
import pandas as pd
A=[200,98,67,5,43,23,56,7,8,3]
B=["sun","mon","tue"]
A
S=pd.Series(A)
S1=pd.Series(B,name="Cybrom")
print(S.size)
print(S.dtype)
print(S1.dtype)
print(S1.name)
print(S.is_unique)
print(S.index)
print(S.values)
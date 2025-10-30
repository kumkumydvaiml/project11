import numpy as np
identity_arr=np.eye(3)
print(identity_arr)


k=[10,3,4,5]
b=np.array(k)
# to find dimensional
b.ndim
# how many are there
b.shape
# to find datatype
b.dtype
k[1]=60
print(k[1]+k[3])
# print(x=k[1]+k[3])
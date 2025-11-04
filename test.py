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

# mul d to 1d 
# d/b ravel and flatten
n=np.array([[10,34],[3,4],[7,9],[43,23]])
r=n.ravel()
r
r[1]=900
print(r)
print(n)
v=n.flatten()
v.ndim
n.ndim
print(v)
print(n)

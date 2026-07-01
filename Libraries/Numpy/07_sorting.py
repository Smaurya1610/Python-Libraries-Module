# --------------------------------
# /Sorting   
# --------------------------------
'''
1 -- np.sort()    [return a sorted copy of array]
2 -- np.argsort()  [return an indices that would sort an array]
3 --  ndarray.sort()   [use arrayname and sort it in   in-place]
'''
#  For 1 D array

import numpy as np
value=[3,6,4,9,8]
x=np.array(value)
# 1
y=np.sort(x)[::-1]  # now it will print in decending order
print(y)
print(x)

# 2
z=np.argsort(x)
print(z)
print(x)

# 3
x.sort()
print(x)


#  for 2 D array
a=[[2,5,3],[5,4,8],[9,6,4]]
b=np.array(a)
# bydefault it sort in row wise
# 1
c=np.sort(b)
print(b)
print(c)

# 2
c1=np.argsort(b)
print(b)
print(c1)

# 3
c.sort()
print(c)

#  Whaat if we want sort in column wise 
# 1
c=np.sort(b,axis=0)
print(b)
print(c)

# 2
c1=np.argsort(b,axis=0)
print(b)
print(c1)

# # 3
b.sort(axis=0)
print(b)

'''  For column wise     axis=0
for row wise   axis=1'''
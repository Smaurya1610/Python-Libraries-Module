# --------------------------------
#  to create 1 D   array in python
# --------------------------------

import numpy as np
list1=[10,12,13,14,15]
array1=np.array(list1)
print(array1,type(array1))
#  agar list integer pass karege toh array integer m bnega
# but agar list m koi element float pass kiye toh   array m sab float m ho jayega

list2=[12,23,34.4,23]
array2=np.array(list2)
print(array2,type(array2))


# agar koi element string aa gy toh array m sabko string m convert krr dega
list3=[12,23,34.4,23]
array3=np.array(list3,dtype='U32')
print(array3)

# =============
# Dtype
# ============
'''dtype = int
dtype = float
dtype = 'u32' for char
'''

# -------------------------------------
#  To create 2 D array in python
# -------------------------------------

list4=[[1,2,3],[4,5,6],[7,8,9]]
array4=np.array(list4,dtype=float)
print(array4)

'''[1  ,   2   ,   3]  --- 0 Row
   [4  ,   5   ,   6]  --- 1 Row
   [7  ,   8   ,   9]  --- 2 Row
   0       1        2  -----Column'''

# --------------------------------------
#  create array using range 
# --------------------------------------
array5=np.arange(1,9)  # 1 D array
print(array5)

array6=np.arange(1,9).reshape(4,2) # 2 D array    here 4=row  2=column
print(array6)

# -------------------------------------
# create zero matrix
# ------------------------------------
array7=np.zeros(6,dtype=int)# 1D array
print(array7)

array8=np.zeros(8,dtype=int).reshape(2,4) # 2D array
array9=np.zeros((2,4),dtype=int)
print(array8)
print(array9)

# ------------------------------------
# create ones matrix
# -----------------------------------
array10=np.ones(5)# 1 D array
print(array10)
# default value float

array11=np.ones((2,3)) # 2 D array
print(array11)
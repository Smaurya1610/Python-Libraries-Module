# ==============================
# Indexing in numpy
# =============================
'''Indexing ka use kisi ek element ko access karne ke liye hota hai.'''
import numpy as np
array=np.array([1,2,3,4,5,6,7,8])# For 1 D array
print(array[0])
print(array[2])
print(array[7])
print(array[-8])
print(array[-1])

# For 2 D array
array1=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(array1[1,2])
print(array1[0,:])
print(array1[:,1])
# in 2 D   index start from (0,0)
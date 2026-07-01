# ======================
# Attributes of NumPy Array
# ======================

'''
ndim     -> Array ki dimension batata hai
            (1D, 2D, 3D, ...)

shape    -> Har dimension me kitne elements hain,
            tuple ke form me batata hai

size     -> Array me total elements ki sankhya

dtype    -> Array ke elements ka data type
            (int32, float64, etc.)

itemsize -> Ek element kitne bytes memory leta hai
'''

import numpy as np
# list=[12,13,14,15,16]
# array=np.array(list)# 1 D array
# print(array)
# print(array.ndim)
# print(array.shape)
# print(array.size)
# print(array.dtype)
# print(array.itemsize)


array1=np.arange(0,6).reshape(2,3)# 2 D array
print(array1)
print(array1.ndim)
print(array1.shape)
print(array1.size)
print(array1.dtype)
print(array1.itemsize)

# array2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])# 3 D array
# print(array2)
# print(array2.ndim)
# print(array2.shape)
# print(array2.size)
# print(array2.dtype)
# print(array2.itemsize)

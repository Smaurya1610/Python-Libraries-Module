# ==========================
# Slicing in numpy array
# ==========================
'''Slicing ka use array ke multiple elements (subarray) ko access karne ke liye hota hai.
array[start : stop : step]
'''

# # for 1 D array
import numpy as np
array=np.array([1,2,3,4,5,6,7,8])
print(array[1:3])
print(array[1:6:2])
print(array[-1:-3:-1])
print(array[::-1])
print(array[::2])

#  For 2 D array
 
import numpy as np
array1= np.array([[12,34,12],[12,23,34,]])
print(array1)
print(array1[1,])
print(array1[:,1])
print(array1[1:3,1:3])



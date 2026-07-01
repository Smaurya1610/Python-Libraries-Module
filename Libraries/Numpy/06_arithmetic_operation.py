import numpy as np
x=np.array([[1,2],
            [3,4]])
y=np.array([[5,6],
            [7,8]])
z=x+y
print(z)
# in all arithmetic operation{+,-,*,/,//,%,**}  size of both array must be same
z1=y-x
print(z1)

z2=x*y  # normal multiplication   means simple element by element
print(z2)

z4=y/x
print(z4)

z5=y//x
print(z5)

z6=y**x
print(z6)

z3=x@y  # for matrix multiplication
print(z3)
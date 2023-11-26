import numpy as np 


x = []

for i in range(1, 17):
    ele = int(input(f'enter the {i} number : \t'))
    x.append(i) 


arr1 = np.array(x).reshape((4,4))

arr2 = np.array(x).reshape((2,2,2,2))


print(f'this is arr1 with {arr1.ndim} and matrix :\n {arr1}\n\n')
print(f'this is arr2 with {arr2.ndim} and matrix :\n {arr2}\n\n')

# import numpy as np 

x = []          # A list of integers
k = 0

for i in range(1, 11):
    y = int(input('enter number :\n'))
    x.append(y)


# w = np.array(x)


for i in x:
    if i % 2 != 0:          # checking the integer type
        k += 1              # if this true add up k by one


print('\n')
print(f"Ther are {k} odd number in the X.\n\n\n")
print("the number of odd digits in the X : ")
print(k)

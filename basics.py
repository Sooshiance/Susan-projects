# import numpy as np 


################################################### Find even and odd numbers ###################################################


# x = []          # A list of integers
# k = 0

# for i in range(1, 11):
#     y = int(input('enter number :\n'))
#     x.append(y)


# # w = np.array(x)


# for i in x:
#     if i % 2 != 0:          # checking the integer type
#         k += 1              # if this true add up k by one


# print('\n')
# print(f"Ther are {k} odd number in the X.\n\n\n")
# print("the number of odd digits in the X : ")
# print(k)


################################################### 2nd greate ###################################################


# n = int(input('Enter the amount of number that you want comparsion'))
# a = int(input('enter one the number of sequence'))
# b = int(input('enter one the number of sequence'))

# if a > b:
#     first = a
#     second = b
# else:
#     first = b 
#     second = a

# for i in range(3, n+1):
#     c = int(input('enter the 3rd number of sequence'))
#     if c > first:
#         second = first 
#         first = c
#     if c < first and c > second:
#         second = c
#     if c < second:
#         pass


# print(f'the first number is {first} and the second number is {second}')


################################################### Upper & Lower ###################################################


l = []

for i in range(1, 11, 1):
    element = int(input(f'enter the element {i} : \t'))
    l.append(element)

l.sort()

print(l[0])
print(l[9])

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


# l = []

# for i in range(1, 11, 1):
#     element = int(input(f'enter the element {i} : \t'))
#     l.append(element)

# l.sort()

# print(l[0])
# print(l[9])


################################################### swaping numbers ###################################################


a = 10
b = 50

print(f"{a}")
print(f"{b}")


b, a = a, b

print(f"new a is {a}")
print(f"new b is {b}")


################################################### Lists ###################################################


l = []

for i in range(1, 10):
    e = int(input(f'enter the element {i} : \t'))
    l.append(e)

first_l = l[:4]
last_l = l[:-3]
l_reverse = l[::-1]

print(f'the 4 elements from the first position of list are {first_l}\n')
print(f'the 3 elements from the last position of list are {last_l}\n')
print(f'the revert of the list is {l_reverse}\n')


list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 = list1 + [1, 2, 3, 4]

# Contents of list1 are same as above 
# program, but contents of list2 are
# different.
print(list1)
print(list2)
print(list2)



################################################### sets ###################################################


myset = {1,2,4,4,5,8,9,9,10}  
print("Return set with unique elements:", myset) 


# join two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# Keep ONLY the Duplicates
z = x.intersection(y)

# Return a set that contains the items that exist in both set x, and set y
x.intersection_update(y)

print(z)
print(x)


# Keep All, But NOT the Duplicates
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}

a.symmetric_difference_update(b)

print(a)


# Return a set that contains all items from both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


# The values True and 1 are considered the same
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)

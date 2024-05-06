# Arrays list should be defined datatype
# i --> integer
# l --> long
# u --> character
# f --> float
from array import *

import numpy as np

# var = array('i', [1,2,3,4,5])

# var.pop()
# print(var)

# for i in var:
#     print(i)

# var1 = array(var.typecode, (a for a in var))
# print(var1)

# var = array('i', [])
#
# len = int(input("Enter the length of the array u need to create : "))
#
# for i in range(len):
#     x = int(input("Enter the numbers: "))
#     var.append(x)
#
# print(var)
#
# searchVal = int(input("Enter the no to check for "))
# i = 0
# for i in var:
#     if i==searchVal:
#         print("Enter number is available",i)
#         break
#         i+=1
# else:
#     print("Enter number search number is not present")

# var1 = np.array([9,4,6,0,5,8])
# var2 = np.array([7,3,1,2,9,0,6])
#
# makeelement = np.intersect1d(var1, var2)
#
# unmatched_ele_var1 = np.setdiff1d(var1, var2)
# unmatched_ele_var2 = np.setdiff1d(var2, var1)
#
# unmatched element = np.concatenate((unmatched_ele_var1, unmatched_ele_var2))
#
# print("Matched Elements : ", makeelement)
# print("Unmatched Elements :", unmatched element)

# var = array('i', [7,3,1,2,9,0,6,4,5])
#
# ascending_array = np.sort(var)
# print("Ascending Array : ", ascending_array)
#
# descending_array = np.sort(var)[::-1]
# print("Descending Array : ", descending_array)
#
#
# my_array = [1, 2, 3, 4]
# my_array = my_array + [10, 20, 30]
# print(my_array)

first = [2, 3, 4, 5, 6]
second = first
print(first)
# second = second + [7]
second.append(7)
print(first)
print(second)

lst1 = ['Om', 'is', 'in', 'vi']
lst2 = ['kar', 'in', 'ter', 'ew']

lst3 = [x + y for x, y in zip(lst1, lst2)]

print(lst3)

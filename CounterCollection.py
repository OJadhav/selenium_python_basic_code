import collections
from collections import*

# #sequence of items
# print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'A']))
#
# #Dictionary
# print(Counter({'A':3, 'B':5, 'C':10}))
#
# #keywords
# print(Counter(A=3, B=5, C=10))

########## Oredered Dictionary #############

# a={}
# a['a']=1
# a['b']=2
# a['c']=3
# a['d']=4
#
# for key, value in a.items():
#     print(key, value)

########## Defulate Dictionary ###########

# d = defaultdict(int)
#
# list = [1,2,3,4,5,6,7,8,9]
#
# for i in list:
#     d[i] += 1
#
# print(d)

########## ChainMap Dictionary #########

# d1 = {'a':1, 'b':2, 'c':3}
# d2 = {'d':10, 'e':20, 'f':30}
# d3 = {'g':40, 'h':50, 'i':60}

# c = ChainMap(d1,d2,d3)
# print(c)
# print(c.keys())
# print(c.values())

# chain = collections.ChainMap(d1,d2)
# print(chain)
#
# chain1 = chain.new_child(d3)
# print(chain1)

########## Namedtuples ###############

s = namedtuple('Student',['name', 'age', 'id'])

String = s('Omkar', 35, 2487454)

li = ['Vijay', '35', '2783937']

dict = {'name':"Suvarna", 'age': 35, 'id': 568445}

print(String._asdict())









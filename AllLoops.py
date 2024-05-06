######### While ###########
#Tipe - Always while loop executed

# count = 3
# while(count < 3):
#     count = count + 1
#     print("Simple", count)
# else:
#     print("Dummy")

############## For ############
#
# a = 4
# for i in range(1, a):
#     print(i)
#
# print("New Function")
# count = 5
# for i in  range(0, count-1):
#     print(i)

# names = ["Ovi", "Suvarna", "Omkar", "Jadhav"]
# for j in names:
#     print(j)
#
# string = "Omkar"
#
# for i in string:
#     print(i)

# d = dict()
# d['abc'] = 123
# d['def'] = 456
#
# for i in d:
#     print("%s %d" %(i, d[i]))
#
# list = ['Ovi', 'Suvarna', 'Omkar', 'Jadhav']
# for i in list:
#     print(i)
# else:
#     print('Dummy')
#
# for i in range(1, 4):
#     for j in range(i):
#         print(i, end='')
#         print()

# for text in "monday":
#     if text == 'n' or text == 'd':
#         break
#     print("Current alphabet ",text)

# for sample in "Omkar":
#     pass
# print("Current alphabet ", sample)

################ Try & Catch ##################

# sample = ['Ovi', 'Suvarna', 'Omkar', 'Jadhav']
# a = iter(sample)
#
# while True:
#     try:
#         sample=next(a)
#         print(sample)
#     except StopIteration:
#         break
#

############## if statement ###########

# i = 100
#
# if(i>200):
#     print("smaller then 200")
# else:
#     print("greater")
#
# print("not either in if or else")
#
# i = 10
#
# if(i==10):
#     print("is equals")
#     if(i<15):
#         print("is less then 15")
#     if(i<12):
#         print("is less then 12")
# else:
#     print("else for 10")

################# Nested if #####################

i = 14
if(i==10):
    print("equals 10")
elif(i==15):
    print("equals 15")
elif(i==20):
    print(" equals to 20")
else:
    print("no condition matches")


i = 10
print(True) if i > 15 else print(False)
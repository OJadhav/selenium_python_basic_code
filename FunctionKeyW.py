
# def nameofFunction(name, **mydetails):
#     print(name)
#     print(mydetails)
#     for i,j in mydetails.items():
#         print(i,j)
#
# nameofFunction(name='Omkar', age=35, place ='Pune', mobileno=8275038166)

def sample(list):
    print(list)
    even = 0
    odd = 0

    for i in list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = sample(list)
print(even)
print(odd)



var = "Ovi Omkar Jadhav"

str_list = list(var.lower())

print(str_list)

n = len(str_list)

print(n)

for i in range(n):
    for j in range(0, n-i-1):
        if str_list[j] > str_list[j+1]:
            str_list[j], str_list[j+1] = str_list[j+1], str_list[j]


sorted_string = ''.join(str_list)

print(sorted_string)
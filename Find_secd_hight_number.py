#Secound highest number
var = [10,10,9,7,9,10,5,7,5,3,9,-1.7]
unique_data = list(set(var))
print(unique_data)

unique_data.sort(reverse=True)

if len(unique_data) < 2:
    print("There are no duplicates")
else:
    print("Second highest number", unique_data[1])
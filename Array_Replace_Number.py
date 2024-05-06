from array import array

input_num = input("Enter the number from 0 to 9 \n")
input_list = list(map(int, input_num.split(',')))
print(input_list)

if len(input_list) != 10:
    print("Enter the number from 0 to 9")
elif 6 in input_list:
    index_of_six = input_list.index(6)
    input_list[index_of_six] = 10
    input_list.insert(index_of_six+1, 15)


output_num_array = ','.join(map(str, input_list))

print("Input ", input_num)
print("Output ", output_num_array)

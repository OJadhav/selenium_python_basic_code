# var = "Repaper"
# change_case = var.lower()
# last_str = change_case.split()
#
# reverse_str = ''.join(word[::-1] for word in last_str)
# print(reverse_str)
#
# if change_case == reverse_str:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")


str = "Madam"
new_str = str.lower()
print(new_str)
rev = reversed(new_str)

if list(new_str) == list(rev):
    print("String is palindrome")
else:
    print("String is not palindrome")
str = "DeMoTeStInG"

converted_str =''

for char in str:
    if char.isupper():
        converted_str += char.lower()
    else:
        converted_str += char.upper()

print(converted_str)


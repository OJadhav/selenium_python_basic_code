str = "I Love India"

words = str.split()
reversed_str = str[::-1]

print("Orignal String: ", str)
print("Reverse String: ", reversed_str)

same_position = ' '.join(word[::-1] for word in words)

print("Same Position word reversed : ", same_position)


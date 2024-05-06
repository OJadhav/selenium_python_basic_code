# str = "geeksforgeeks"
#
# char_counts = { }
#
# for char in str:
#     char_counts[char] = char_counts.get(char, 0) + 1
#
#
# for char, count in char_counts.items():
#     print(f"{char}: {count}")
#

var = "Object oriented programminge"
print("Number of characters ", len(var))

var = var.replace( " ", "")
char_count = {}

for char in var:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1


max_count = max(char_count.values())
max_chars = [char for char, count in char_count.items() if count == max_count]

print("Number of characters ", len(var))
print("charters with the highest number: ", max_chars)
print("Highest count ", max_count)
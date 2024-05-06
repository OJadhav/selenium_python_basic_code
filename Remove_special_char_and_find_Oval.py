
text = "H?i:: Om&^kar** ho$w are \\you?"
ovals = "aeiouAEIOU"

# Remove all special characters
filter_text = "".join(char for char in text if char.isalnum() or char.isspace())

# Find all positions of the oval "o" (case-sensitive)
oval_positions = [i for i, char in enumerate(filter_text) if char in ovals]

print("Filter text ", filter_text)
print("Oval positions: ", oval_positions)

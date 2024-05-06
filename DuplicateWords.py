str = "i love automation testing and i love india"

words = str.split()

unique_words = set()
duplicate_words = set()

for word in words:
    if word in unique_words:
        duplicate_words.add(word)
    else:
        unique_words.add(word)

print("Duplicate words: ", duplicate_words)
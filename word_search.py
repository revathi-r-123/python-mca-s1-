# Read a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of words
print("Number of words:", len(words))

# Ask the user for a word to search
search_word = input("Enter a word to search: ")

# Search for the word exactly as entered
if search_word in words:
    print(f"The word '{search_word}' was found in the sentence.")
else:
    print(f"The word '{search_word}' was NOT found in the sentence.")

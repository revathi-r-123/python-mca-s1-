#vowels
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
vowel_list = []

for i in word:
    if i in vowels:
        vowel_list.append(i)

print("Vowels in the word:", vowel_list)


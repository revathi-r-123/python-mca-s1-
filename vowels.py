#vowels
word=input("Enter a word:")
vowels="aeiouAEIOU"
for i in word:
    if i in vowels:
        print(i,end=" ")

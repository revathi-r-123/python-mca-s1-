str1=input("Enter a string:")
if str1:
    char=str1[0]
    str1=str1.replace(char,'$')
    str1=char+str1[1:]
    print("String:",str1)
else:
    print("Empty string eneterd!")



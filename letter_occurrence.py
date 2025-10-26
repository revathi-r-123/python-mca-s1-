names = []
count = int(input("Total number of names want to enter:"))
for name in range(count):
    name = input("Enter name:")
    names.append(name)
a_count = 0
for name in names:
    a_count += name.count('a')
    a_count += name.count('A')
print("List of names:",names)
print("Total occurrences of 'a':",a_count)

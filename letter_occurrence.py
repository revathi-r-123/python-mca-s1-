
# Get first names from the user
names = input("Enter first name: ")
letter=names.split()

# Initialize counter
count_a = 0

# Loop through each name and each character
for name in names:
    for char in name:
        if char == 'a':
            count_a += 1

# Display the result
print("Total occurrences of 'a':", count_a)

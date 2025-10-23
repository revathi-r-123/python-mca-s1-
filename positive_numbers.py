# Given list of integers
numbers = [-10, 15, -3, 8, 0, -7, 22, -1]

# Generate list of positive numbers
positive_numbers = []

for num in numbers:
    if num > 0:
        positive_numbers.append(num)

print("Positive numbers:", positive_numbers)

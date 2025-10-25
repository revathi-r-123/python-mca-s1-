count = int(input("Enter total number of elements:"))
num_list = []
for i in range(count):
    num = int(input("Enter number:"))
    if num>100:
        num_list.append('over')
    else:
        num_list.append(num)
print("List of integers:",num_list)

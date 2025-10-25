size1 = int(input("Enter number of elements in list1:"))
list1 = []
for i in range(size1):
    num1 = int(input("Enter element:"))
    list1.append(num1)

size2 = int(input("Enter number of elements in list2:"))
list2 = []
for i in range(size2):
    num2 = int(input("Enter element:"))
    list2.append(num2)

while True:
    print("\n__________MENU________")
    print("1.Check if lists are of same length")
    print("2.Check if lists sum to same value")
    print("3.Check if any value occurs in both lists")
    print("4.Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        if len(list1) == len(list2):
            print("Lists are of same length.")
        else:
            print("Lists are of different length.")
    elif choice == 2:
        if sum(list1) == sum(list2):
            print("Lists sum to the same value.")
        else:
            print("Lists do not sum to the same value.")
    elif choice == 3:
        common = []
        for i in list1:
            if i in list2 and i not in common:
                common.append(i)
        if common:
            print("Common values found:",common)
        else:
            print("No common values found.")
    elif choice == 4:
        print("Exiting program..")
        break
    else:
        print("Invalid choice. Please enter 1 to 4")

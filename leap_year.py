current_year = int(input("Enter the current year: "))
final_year = int(input("Enter the final year: "))

if final_year == current_year:
    print("You entered the current year. No future leap years to display.")
elif final_year < current_year:
    print("Please enter a year greater than the current year.")
else:
    print(f"Leap years from {current_year} to {final_year} are:")
    while current_year <= final_year:
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            print(current_year)
        current_year += 1

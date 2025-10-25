student = {
    "name":"John","roll_number":32,"register_number":20230045,
    "department":"Computer Science","semester":5
    }


print(student)
total_mark = int(input("Enter total mark:"))
student["total_mark"] = total_mark

if total_mark >= 90:
    grade = "A"
elif total_mark >= 82:
    grade = "B"
elif total_mark >= 75:
    grade = "c"
elif total_mark >= 60:
    grade = "D"
elif total_mark >= 50:
    grade = "P"
else:
    grade = "F"

student["grade"] = grade

del student["roll_number"]
print(student)



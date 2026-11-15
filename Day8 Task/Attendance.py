name = input("Enter student name: ")

file = open("attendance.txt", "a")
file.write(name + "\n")
file.close()

print("Attendance saved successfully")
file = open("attendance.txt", "r")

content = file.read()

print("Student Attendance Records:")
print(content)

file.close()

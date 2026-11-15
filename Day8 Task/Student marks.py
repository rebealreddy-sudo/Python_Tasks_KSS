file = open("marks.txt", "w")

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    file.write(name + " " + str(marks) + "\n")

file.close()

print("Student marks saved successfully")
file = open("marks.txt", "r")

total = 0
count = 0

print("Student Records:")

for line in file:
    name, marks = line.split()

    marks = int(marks)

    print(name, marks)

    total = total + marks
    count = count + 1

if count > 0:
    average = total / count
    print("Average Marks:", average)
else:
    print("No student records found")

file.close()


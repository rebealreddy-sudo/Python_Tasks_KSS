name = input("Enter employee name: ")
salary = int(input("Enter employee salary: "))

file = open("employees.txt", "a")

file.write(name + " " + str(salary) + "\n")

file.close()

print("Employee record added successfully")
file = open("employees.txt", "r")

highest_salary = 0
highest_employee = ""

print("Employee Details:")

for line in file:
    name, salary = line.split()

    salary = int(salary)

    print("Name:", name, "Salary:", salary)

    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name

print("\nHighest Salary Employee:")
print("Name:", highest_employee)
print("Salary:", highest_salary)

file.close()

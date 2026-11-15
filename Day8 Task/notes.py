notes = input("Enter your daily notes: ")

file = open("notes.txt", "w")
file.write(notes)
file.close()

print("Notes saved successfully")
file = open("notes.txt", "r")

content = file.read()

print("Daily Notes:")
print(content)

file.close()

file = open("grocery.txt", "w")

while True:
    item = input("Enter grocery item (or stop): ")

    if item.lower() == "stop":
        break

    file.write(item + "\n")

file.close()

print("Grocery items saved successfully")
file = open("grocery.txt", "r")

content = file.read()

print("Grocery List:")
print(content)

file.close()

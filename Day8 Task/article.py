article = input("Enter your article: ")

file = open("article.txt", "w")
file.write(article)
file.close()

print("Article saved successfully")
file = open("article.txt", "r")

content = file.read()

words = len(content.split())
lines = len(content.splitlines())
characters = len(content)

print("Number of Words:", words)
print("Number of Lines:", lines)
print("Number of Characters:", characters)

file.close()

file = open("file-process/bear.txt")
content = file.read()
first = content[:90]

with open("file-process/first.txt", "w") as myfile:
    myfile.write(first)


#simple code
with open("bear.txt") as file:
    content = file.read()

with open("first.txt", "w") as file:
    file.write(content[:90])
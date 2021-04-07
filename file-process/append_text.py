#write then read
with open("file-process/fruits.txt", "a+") as myfile:
    myfile.write("\nMango")
    myfile.seek(0)
    content = myfile.read()

print(content)


#read and append
with open("bear1.txt") as file:
    content = file.read()

with open("bear2.txt", "a") as file:
    file.write(content)
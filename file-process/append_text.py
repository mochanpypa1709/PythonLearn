#write then read
with open("file-process/fruits.txt", "a+") as myfile:
    myfile.write("\nMango")
    myfile.seek(0)
    content = myfile.read()

print(content)
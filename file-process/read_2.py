file = open("file-process/bear.txt")
content = file.read()
file.close()

#print out first 90 characters
print(content[:90])
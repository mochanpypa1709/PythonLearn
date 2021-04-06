def foo(character, filepath="file-process/bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

print(foo('is'))
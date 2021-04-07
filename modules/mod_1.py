import time

#exec print after 10sec
while True:
    with open("file-process/vegetables.txt") as file:
        print(file.read())
        time.sleep(10)
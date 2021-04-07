import time
import os

#exec print after 10sec
while True:
    if os.path.exists("file-process/vegetables.txt"):
        with open("file-process/vegetables.txt") as file:
            print(file.read())
    else:
         print("File does not exist")
    time.sleep(10)
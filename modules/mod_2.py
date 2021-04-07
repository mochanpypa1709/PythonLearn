import time
import os
import pandas

#exec print after 10sec
while True:
    if os.path.exists("file-process/temps_today.csv"):
        data = pandas.read_csv("file-process/temps_today.csv")
        #print(data.mean())
        print(data.mean()["st1"])
    else:
         print("File does not exist")
    time.sleep(10)
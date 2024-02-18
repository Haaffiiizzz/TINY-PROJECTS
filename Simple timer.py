import time
import os

timeNeeded = int(input("Input how many seconds timer you need:\n"))

for i in (range(timeNeeded+1)):
    os.system("cls")
    print(i)
    time.sleep(0.98)
    

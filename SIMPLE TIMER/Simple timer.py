from playsound import playsound
import time
import os


timeNeeded = int(input("Input how many seconds timer you need:\n"))

for i in (range(timeNeeded+1)):
    os.system("cls")
    print(f"{i:0>2}")
    time.sleep(0.98)
           


os.system("cls")    
print("Time Up!")
playsound("SIMPLE TIMER\Alarm beep.mp3")
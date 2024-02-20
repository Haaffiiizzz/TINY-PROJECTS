import schedule
from win10toast import ToastNotifier
from playsound import playsound
import time

def getScheduleInfo() -> list[dict]:
    print("Hello and welcome to this simple schedule maker!\n")
    time.sleep(1)

    allTasks = []
    addTask = True
    while addTask:
        task = {}
        task["taskName"] = input("What task do you want to add?:\n")
        time.sleep(1)
        task["taskFreq"] = input("What frequency do you want for this task? \
(Days, Hours, Minutes, Seconds, Once?):\n").upper()
        
        if task["taskFreq"][0] == "D":
            task["taskFreq"] = "day"
            haveExactTime = input("Do you have an exact day interval \
for this task?(Yes/No)").upper()
            time.sleep(0.5)
            if haveExactTime[0] == "Y":
                task["taskFreq"] = "days"
                task["exactTime"] = int(input("Type in the day interval you want:\n"))

        elif task["taskFreq"][0] == "H":
            task["taskFreq"] = "hour"
            haveExactInterval = input("Do you have an exact hour interval for this task?:\n").upper()
            time.sleep(0.5)
            if haveExactInterval[0] == "Y":
                task["taskFreq"] = "hours"
                task["exactTime"] = int(input("Type in the hour interval you want:\n"))

        elif task["taskFreq"][0] == "M":
            task["taskFreq"] = "minute"
            haveExactInterval = input("Do you have an exact minutes interval for this task?:\n").upper()
            time.sleep(0.5)
            if haveExactInterval[0] == "Y":
                task["taskFreq"] = "minutes"
                task["exactTime"] = int(input("Type in the minute interval you want:\n"))

        elif task["taskFreq"][0] == "S":
            task["taskFreq"] = "second"
            haveExactInterval = input("Do you have an exact seconds interval for this task?:\n").upper()
            time.sleep(0.5)
            if haveExactInterval[0] == "Y":
                task["taskFreq"] = "minutes"
                task["exactTime"] = int(input("Type in the seconds interval you want:\n"))
        
        elif task["taskFreq"][0] == "O":
            task["taskFreq"] = "once"

        allTasks.append(task)
        time.sleep(1)
        addMoreTasks = input("Do you want to add anymore tasks? (Yes/No):\n").upper()
        if addMoreTasks[0] == "N":
            addTask = False

    return(allTasks)

def displaySchedule(task):
    message = ToastNotifier()
    task = task["taskName"]
    message.show_toast("Schedule", task, duration = 3, threaded = False)

def createSchedule(scheduleInfo: list):
    for event in scheduleInfo:
        if event["taskFreq"] == "second" or "seconds":
            exactTime = event.get("exactTime", 1)
            schedule.every(exactTime).seconds.do(displaySchedule, task=event)
    
def main():
    scheduleInfo = getScheduleInfo()
    createSchedule(scheduleInfo)
if __name__ == "__main__":
    main()    

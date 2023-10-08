# Gretting according to current time
import time
timestamp = time.strftime('%H:%M:%S:%p')
print(timestamp)
timestamp = int(time.strftime('%H'))
if(timestamp>=0 and timestamp<12):
    print("Good Morning Sir, it's"' ->',timestamp,'<- '"o'clock")
elif(timestamp>=12 and timestamp<16):
    print("Good Afternoon Sir, it's"' ->',timestamp,'<- '"o'clock")
elif(timestamp>=16 and timestamp<20):
    print("Good Evening Sir, it's"' ->',timestamp,'<- '"o'clock")
else:
    print("Good Night Sir, it's"' ->',timestamp,'<- '"o'clock")
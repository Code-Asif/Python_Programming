# Exercise 11 Drink water reminder

import time
from plyer import notification
import pyttsx3


def notif(title, msg):
  notification.notify(
    title=title,
    message=msg,
    timeout=5,
  )

  engine = pyttsx3.init()
  engine.say("Hey Aashif, Please Drink Water")
  engine.runAndWait()


title = "DRINK WATER"
msg = "please drink water"

while True:
  notif(title, msg)
  time.sleep(3600)

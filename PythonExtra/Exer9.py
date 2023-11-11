# Shoutout to everyone exercise
import time
import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")
list = ["Aashif", "Nikhat", "Kaamraan", "Alam", "Shabana"]
    
for name in list:
    names = name.split()
    print(f"Hello to {name}")
    shoutout = f"Hello {names[0]}"
    speaker.Speak(shoutout)
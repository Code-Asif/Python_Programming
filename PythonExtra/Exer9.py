# Shoutout to everyone exercise

import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")
list = ["Aashif", "Nikhat", "Kaamraan", "Aalam", "Shaabaanaa"]
    
for name in list:
    names = name.split()
    print(f"Hello to {name}")
    speaker.Speak(f"Hello {names[0]}")
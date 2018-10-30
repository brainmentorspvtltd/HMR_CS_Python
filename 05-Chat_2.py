from datetime import datetime
import webbrowser
import os, random

helloIntent = ['hello', 'hi', 'hey', 'howdy', 'hey there']
byeIntent = ['bye', 'see you', 'take care', 'catch you later']

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    
    if msg in helloIntent:
        print("Hello")
    elif msg in byeIntent:
        print("Bye")
        chat = False
    elif msg == 'date please':
        date = datetime.now().date()
        print("Date is",date)
    elif msg == 'time please':
        time = datetime.now().time()
        print("Time is",time)
    elif msg.startswith('open'):
        website = msg.split()[-1]
        webbrowser.open(website+'.com')
    elif msg == 'play music':
        path = r'C:\Users\asus\Music'
        os.chdir(path)
        songs = os.listdir()
        song = random.choice(songs)
        os.startfile(song)
    else:
        print("I Don't Understand")

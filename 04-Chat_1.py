helloIntent = ['hello', 'hi', 'hey', 'howdy', 'hey there']

chat = True
while chat:
    msg = input("Enter your message : ")
    
    if msg == 'hello':
        print("Hello")
    elif msg == 'bye':
        print("Bye")
        chat = False
    else:
        print("I Don't Understand")

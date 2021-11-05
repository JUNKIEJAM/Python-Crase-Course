command=""

while True:
    command=input("> ")

    if command.lower()=="start":
        print("car started")

    elif command.lower()=="stop":
         print("car stopped")  

    elif command=="quit":
         break

    else:    
        print("didn't understand")


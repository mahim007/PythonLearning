start = "start"
stop = "stop"
quit = "quit"
lastStatus = ""

while True:
    command = input("Enter Command: ").lower()
    if command == start:
        if lastStatus == start:
           print("Car already started")
        else:
             print("Car Started")
        lastStatus = command
    elif command == stop:
        if lastStatus == stop:
           print("Car already stopped")
        else:
            print("Car stopped")
        lastStatus = command
    elif command.lower() == quit:
        break
    else:
        print("Sorry not understood")
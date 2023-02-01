def mysum(*args):
    runningSum = 0
    print("Input numbers to sum one-by-one, input 'stop' to finish")
    while True:
        tempNumber = input("")
        if tempNumber == 'stop':
            break
        else:
            try: 
                runningSum += float(tempNumber)
            except ValueError:
                print("Please enter a valid number")
                continue
        print("Please enter next number")
    print("Total is " + str(runningSum))
mysum()

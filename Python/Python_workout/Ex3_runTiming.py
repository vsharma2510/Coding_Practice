def run_timing():
    inputTime = 0.0
    numInputs = 0
    while True:
        tempInputTime = input("Enter 10 km run time \n")
        if tempInputTime == '':
            break
        try:
            inputTime += float(tempInputTime)
        except ValueError:
            print("Please enter a number!")
        numInputs += 1
    print(f"Average of {inputTime}/{numInputs}, over {numInputs} runs")

run_timing()
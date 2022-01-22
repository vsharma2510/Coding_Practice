import pyinputplus as pyip
import random, time

numberOfQuestions = 10
timeLimit = 5
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    prompt = 'Question number %s. What is %s multiplied by %s?' %(questionNumber, number1, number2)

    try:
        #Right answers are handled by allowRegexes.
        #Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' %(number1*number2)], blockRegexes=[('.*','Incorrect!')], timeout=20, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        #This block runs if no exceptions were raised in the try block.
        print('Correct!')
    correctAnswers+=1
    time.sleep(2) #Brief pause to let user see the result.
    print('Score: %s / %s' %(correctAnswers, numberOfQuestions))

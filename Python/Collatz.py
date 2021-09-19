import sys
def Collatz(number):
    if(number==1):
        print('Entering 1 is not allowed')
        sys.exit()
    if(number%2):
        return (3*number+1)
    else:
        return (number//2)

print('Enter number')
number_string = input()
try:
    number = int(number_string)
except ValueError:
    print('!!!!! Please enter an integer !!!!!')
    print('Executing the program with default value 3')
    number=3
while(number!=1):
    temp=Collatz(number)
    print(str(temp)+'\n')
    number=temp
if(number==1):
    print('Sequence finished')
else:
    print('Something went wrong!')

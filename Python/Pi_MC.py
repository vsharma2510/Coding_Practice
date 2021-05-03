#Estimating pi using MC
from random import random,uniform,seed
square=0
circle=0
N=100000000
for x in range(N):
    a=uniform(-1,1)
    b=uniform(-1,1)
    c=(a**2)+(b**2)
    #print(c)
    if c>1:
        square=square+1
    elif c<1:
        circle=circle+1

print('Squares were ' + repr(square) + '\n')
print('Circles were ' + repr(circle) + '\n')

print('The value of pi is ' + repr((4*circle/N)))

#seed(2)
#print(random(),random(),random())


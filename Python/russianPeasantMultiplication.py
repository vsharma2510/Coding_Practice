import math
import pandas as pd

n1 = input('Enter first number')
n2 = input('Enter second number')

halving = [n1]

while(min(halving) > 1):
    halving.append(math.floor(min(halving)/2))
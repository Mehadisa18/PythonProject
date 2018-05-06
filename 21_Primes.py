# A program to check if an number is a prime number

import math
import time

def isprime(n):

    if(n==1 or n<1):
        return False
    elif(n==2):
        return True
    elif(n!=0 and n%2 == 0):
        return False
    else:
        maxdivisor = math.floor(math.sqrt(n))
        for i in range(3,1+maxdivisor,2):
            if(n%i == 0):
                return False
        return True


for i in range(1,1000000):
    print(i,"  " ,isprime(i))
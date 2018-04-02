# lets write a program for fibonacci series
from functools import lru_cache

@lru_cache(maxsize =1000) # def : 128
def fibonacci(n): # nth fibonacci number
    if(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


#for n in range(1,101):  # This is slow as we calculate the same values again and again
 #   print(n," : ",fibonacci(n))

fib_dict ={}

def fibonacci1(n):
    if n in fib_dict:
        return fib_dict[n]
    elif(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        cachevalue = fibonacci1(n-1)+fibonacci1(n-2)
        fib_dict[n]=cachevalue
        return cachevalue


for n in range(1,101):   # This will take less time as a dictionary is used 
   print(n," : ",fibonacci1(n))

   # we can as well use Lru_cache 
for n in range(1,101):   # This will take less time as lru cache is used 
   print("***", n," : ",fibonacci(n))



    



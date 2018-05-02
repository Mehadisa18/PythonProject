# Now we step into randomness
"""
|_|_|_|_|_
|_|_|_|_|_
|_|_|_|_|_
|
starting point
 
 If we consider the above figure, we can see the grid and a starting point.
let us consider the starting point as home. Now given a number of blocks, we must be able to list some random
walks which if taken the distance will be less than the number of blocks mentioned.
"""
import random

def random_walk(n): # here n denoted the number of blocks permitted
    x,y=0,0 
    for i in range(n):
     dx,dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
     x += dx # python considers shortcut operator as a new assignement and we cannot use x without declaring it so it is very much
             # necessary to define both x and y inside the function definition
     y += dy
    return (x,y)

for i in range(20):
 new_place=random_walk(10)
 distance = abs(new_place[0])+abs(new_place[1])
 print("new place : ", new_place," distance : ",distance)

"""
Now if below 4 blocks we need not take a cab back to home
if we consider all the random walks, lets find out the percentage of time 
we need not take a cab back
"""
""" lets analyse the avg for about 10000 walks"""

number_of_walks = 20000
number_of_blocks = 30

for i in range(1,31):
    no_transport =0
    for j in range(number_of_walks): # as number of blocks is 30
        (a,b) = random_walk(i)
        distance = abs(a)+abs(b)
        if (distance < 4):
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("walk size: ",i,"percentage: ",no_transport_percentage*100)
        







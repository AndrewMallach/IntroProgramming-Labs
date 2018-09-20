#Andrew Mallach
#CMPT 120
#Professor Johnson
#Lab Activity 4

import math


def pi():

    count = int(input("Enter a number  "))
    answer=4
    denominator=3
    minus=True

    for x in range(count):
        if minus==True: 
            answer-=4/denominator
            denominator+=2
            minus=False
        else:
            answer+=4/denominator
            denominator+=2
            minus=True
    print(answer)

pi()
            
        

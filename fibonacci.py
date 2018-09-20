#Andrew Mallach
#CMPT 120
#Professor Johnson
#Lab Activity 4


def fib():

    count= int(input("Enter a number  "))
    
    n1 = 0
    n2 = 1

    for x in range(count):
        n3= n1+n2
        n1=n2
        n2=n3

    print(n3)
 
   

     
fib()

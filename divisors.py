#Perlix Soco
#07.02.2024
#divisors.py

#Add a function below called divisors(num) which takes one argument of type integer
#and returns a list of all the divisors(factors) of that that number -
#A divisor or factor is a number which divides evenly leaving no remainder

#define the funciton header called divisors expecting one argument

    #set up an empty list to hold your result
    
    #loop i from 1 to the number you are checking (take care not to include the number itself)

        #if the remainder when dividing the number by i is equal to zero then i is a divisor so...
        
            #apend i to the list you set up
            
 
    #return the list
    
def divisors(num):

    myList = []

    for i in range(1, num):
        if num % i == 0:

            myList.append(i)
    return myList

print(divisors(30))

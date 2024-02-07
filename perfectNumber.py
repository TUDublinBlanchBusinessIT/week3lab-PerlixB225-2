#Perlix Soco
#07.02.2024
#PerfectNumber.py

#A perfect number is one for which all the divisors of the number add up to the
#number itself. For example the divisors of 28 are 1,2,4,7,14 which added together gives 28
#write a function below called perfectNumber(x) which checks to see if x is a perfect number
#The function should return True if the number is perfect and False if it is not

from divisors import divisors

def perfectNumber(x):


    result = False
    if sum(divisors(x)) == x:
        result=True 
    return result
         
    
            



print(perfectNumber(20))



#define the function header called perfectNumber expecting one argument

    #set a result variable to False by default
    
    #if the sum of all the divisors of the number is equal to the test number

        #set the result variable to be True

    #return the result variable

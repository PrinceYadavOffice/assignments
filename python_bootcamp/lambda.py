#1.Suppose you have a list of numbers. Using a lambda function, increase each number by 5%?.
num=[4,5,6,7,8,9]
num = list(map( lambda x: x+(x*5)/100 ,num))
print(num)


#2.create a filter which filters out all the prime numbers from a given list of integers

num1 = range(2, 50)
primes = filter(lambda x: x == 2 or x % 2, num1)
print (list(primes))

#3.print the following pattern without using any loops. The input will be length of pattern to be printed: 0, 2, 6, 12, 20, 30, 42, 56, 72, 90.
#import pdb

num2 = map(lambda x:  x*(x-1) ,range(1,11))
#pdb.set_trace()
print(list(num2))

#5.Write a function which takes list of natural numbers as input. Create a dictionary to group the odd and even numbers separately(in a dict). The function should have proper exception handling.

def fun1(l):
    d={}
    try:
        for i in l:
            if type(i) is int:
                if i%2==0:
                    d[i]="even"
                else:
                    d[i]="odd"
            else:
                raise ValueError
    except ValueError:
        print("Please pass only natural number")
    return d

print(fun1([1,2,3,4,5,6,7,'8',9,10]))

#Q6.Create a function "divide" which takes inputs as 2 whole numbers. The function should raise exceptions if denominator is 0, or the passed numbers are not whole numbers.

def divide(num1,num2):
    try:
        raise num1/num2
    except TypeError:
        print("Please pass whole number")
    except ZeroDivisionError:
        print("Denominator should not be zero")
    pass

divide(4,'hello')

#q7.Write a script that repeatedly asks the user to input an integer, displaying a message to “try again” by catching the ValueError that is raised if the user did not enter an integer.
#Once the user enters an integer, the program should display the number back to the user and end without crashing

def user_input():
    print("\n")
    while True:
        try:
            num = int(input("Enter integer: "))
            if type(num) == int:
                return num
            raise ValueError
        except :
            print("Please Enter integer")

print(user_input())

#q8.

def display(str,no):
    try:
        if  not str[int(no)] :
            raise IndexError
        if type(int(no)) != int:
            raise ValueError
        else:
            return str[no]
    except IndexError as err:
        print("Error: ",err)
    except ValueError as err:
        print("Error: ",err)

str = input("Enter String :")
no = input("Enter Index :")
display(str,no)


#Q9.Write a script that simulates 10,000 rolls of a fair dice and displaysthe average number rolled.
import random
def roll(times):
    total = 0
    for i in range(times):
        num = random.randint(1, 6)
        total = total + num
    average = total / times
    return average

print(roll(10000))






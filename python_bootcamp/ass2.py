
#List

l =[2,3,4,5,6,7]
for i in l:#iterating list elements one by one
	print(i)	

#String
str1="My Name is Prince"
for i in str1:#iterate each character one by one
	print(i)

#range

for i in range(1,10): 
	print(i)	#print no from 1 to 10
	
	
	
#WAP to find the count of all even numbers in a list and then find the sum of all those even #numbers.

lst=[1,2,3,4,5,6,7,8,9,10]

count=0
total=0

for i in lst:
	if i%2==0:
		count+=1
		total+=i
		
print("List :",lst)		
print(f"Count of Even numbers in list is {count}")
print(f"Sum of Even number is {total}")		

#WAP to extract integer values from a tuple containing mixed data type values.

tuple1=(1,'hi',5,7.5,3,7,'hello','fruits')

lst1=[]

for i in tuple1:
	if type(i) == int:
		lst1.append(i)
		
print("Tuple of mixed data type: ",tuple1)		
print("integer value list: ",lst1)	

#Create a dictionary with name of products as key and their price as it's value, include fruits and stationary objects in the products and then filter out name of all the fruits from the dictionary in a separate list.

products ={
'fruits':{'mango':'100','apple':'150','grapes':'60','kiwi':'500'},
'stationary':{'pen':'10','notebook':'30','eraser':'5','register':'50'}
}

fruit_lst=list(products['fruits'].keys())
print("Products: ",products)
print("Fruits List :",fruit_lst)	


print("\n \n \n")
#Iterate thorugh the sentence "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." and find the number of occurances of each character and list the character with most number of occurances.

sentence ="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

dic={}

for i in sentence:
	if i in dic:
		dic[i]+=1
	else:
		dic[i]=1
		
print("dictonary: ",dic)	

k=list(dic.keys())
v=list(dic.values())	

character= k[v.index(max(v))]
print("Character with most no of occurances is : ",character," No of occurances :",max(v))


#Accept three sides of a triangle from a user and identify whether it's an equilateral, isosceles or scalene triangle.

side1 =int(input("Enter Side 1: "))
side2 =int(input("Enter Side 1: "))
side3 =int(input("Enter Side 1: "))

if side1 ==side2 and side2==side3 and side1==side3:
	print("Equilateral Triangle")
elif side1==side2 or side2==side3 or side1==side3:
	print("Isosceles Triangle")
else:
	print("scalene Triangle")
	
	
#Rock Paper secissor game


turns = int(input())
awin, bwin=0,0
for i in range(turns):
    player_A = input("Player A, make your move: ").lower()
    player_B = input("Player B, make your move: ").lower()
    if player_A == player_B:
        print("DRAW")
    elif player_A == "r":
        if player_B == "s":
            print("A WINS")
            awin += 1

        else:
            print("B WINS")
            bwin += 1
    elif player_A == "p":
        if player_B == "r":
            print("A WIN")
            awin += 1
        else:
            print("B WIN")
            bwin += 1
    elif player_A == "s":
        if player_B == "p":
            print("A WIN")
            awin += 1
        else:
            print("B WIN")
            bwin += 1
    else:
        print("Please enter a valid move!")

if awin>bwin:
    print("A WINS TOURNAMENT")
else:
    print("B WINS TOURNAMENT")







#Create a number guessing game in which we accept a random input between 1-50 from the user and run the script until the user guesses the correct number. You can also give hints to the user if the guessed number is more/less than the actual number.

import random 

computer_value = random.randint(1,50)

while True:
	user_input=int(input("Enter No :"))
	if user_input == computer_value:
		print("Correct")
		break
	elif user_input <computer_value:
		print("you guessed less no than actual no")
	elif user_input > computer_value:
		print("you guessed more no than the actual no")
	
	else:
		print("Try Again")			 			
	
			



#Suppose passing marks of a subject is 35. Take input of marks from user and check whether it is greater than passing marks or not.

passign_marks=35

user_input=int(input("Enter Marks: "))

if user_input < passign_marks:
	print("Your marks is less than Passing Marks\n")

else:
	print("Your marks is greater than  Passing Marks ")
	
	
#Take two number and check whether the sum is greater than 5, less than 5 or equal to 5.

number1=int(input("Enter NO 1 :"))
number2=int(input("Enter No 2 :"))

total = number1+number2

if total==5:
	print("Total of 2 numbers is equal to 5")
elif total<5:
	print("Total of 2 numbers is less than 5")				

else:
	print("Total of 2 numbers is greater than 5")
































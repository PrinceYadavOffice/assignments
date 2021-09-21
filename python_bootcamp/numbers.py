number1 =3
number2 =5
floor = number1//number2
ceil = number1//number2+1
print("Floor :",floor)
print("Ceil :", ceil)


my_str="Hello Python!"
my_str = my_str[::-1] #reversing using slicing
print(my_str) 
#accesing ! using indexing

print(my_str[0])

#print("i have {} apples".format(number5))
print(f"i have {number1} apples")

number = input() #enter 3 digit number only
result = int(number[0])+int(number[1])+int(number[2])
print("sum of 3 digits:",result)


my_str2 ="hello_how_are__you"
new_str=""
for i in my_str2:
    if i =='_':
        new_str+='+'
    else:
        new_str+=i
print("Original String :",my_str2)
print("updated string: ",new_str)






#write a program to reverse the list of strings in reverse order.

strings =["zebra","Lion","Tiger","Elephant"]

strings=strings[::-1]
print("Reversed Strings List :",strings)


#Name two ways to build a list containing five integer zeroes.

lst =[]

for i in range(5): # for loop method
	lst.append(0)


print("For loop Method",lst)

# list comprehensive method

lst1=[0 for i in range(5)]
print("List comprehensive method :", lst1)


#write a Python program to find the second largest number in a given list.

lst2=[10,12,8,4,9,6]
lst2.sort()
second_largest=lst2[-2]
print("Lst2 :", lst2)
print("Second Largest element: ",second_largest)

#question no 6

colors=['black','white']
sizes=['S','M','L']
res = [(a, b) for a in colors for b in sizes]
print("Cartesian Product: ",res)

#WAP to create a list of one million integers using
import time

start = time.time()
lst3=[]
for i in range(1000000):
	lst3.append(i)
	
timetaken = (time.time() - start)	
print("Time taken by lsit :",timetaken)
	
#lst4=[i for i in range(1000000)]

#Use Python’s list comprehension syntax to produce
#the list [ a , b , c , ..., z ], but without having to type all 26 characters.

lst5=[chr(x) for x in range(ord('a'), ord('z')+1)]
print("List :",lst5)

#write a program to generate a list of all the common characters in the two strings using list comprehension.Expected output ['s', 'a', 'm']

seq1 = "spam"
seq2 = "scam"

output=[i for i in seq1 if i in seq2]
print("Output: ",output)

#Use Python’s list comprehension syntax to produce
#the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

lst6=[x*(x + 1) for x in range(10)]
print("List: ",lst6)












	




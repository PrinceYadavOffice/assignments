#Q3.Using Dictionary Comprehension, remove null items from the following dictionary.
dictionary = {'language': 'python', 'version': '3.8', 'app':None, 'ide': None}
print(dictionary)
dictionary1 = { k:v for k,v in dictionary.items() if v is not None }
print(dictionary1)

#Q4
a = {'a':1,'b':2,'c':3}
#print (a['a','b'])

tup = (1,1,1,1)
#tup[0] = tup[0] * 3
print(tup)

#Q5.Create a Dictionary 'chars' such that chars[1] = 'a', chars[2] = 'b' ..... chars[26] = 'z'.
#Given the following string l = '0abcdefghijklmnopqrstuvwxyz' and using only dictionary comprehension.

l = '0abcdefghijklmnopqrstuvwxyz'

chars = { i:l[i] for i in range(1,len(l))}
print(chars)

#Q6.
tup = ('python')
print(tup*3)

tup = 1
tup = (tup,)*4
print(tup)


#Q7.tup = [(0, 1), (1, 2), (2, 3)]

tup = [(0, 1), (1, 2), (2, 3)]
output = sum(i[1] for i in tup)
print(output)

#Given a list of tuples, tup = [(0, 1), (1, 2), (2, 3)]. Write a Dictionary Comprehension such that the key of the dictionary
#is the value of the tuple and the values are the sum of the tuple keys. Ex: print(d[(2,3)] returns 5.

tup = [(0, 1), (1, 2), (2, 3)]
dic1 = { (i):i[0]+i[1] for i in tup}
print(dic1)
print(dic1[(2,3)])

#Q9
def oldAge(d):
    age=50
    if "age" in d:
        age+=d.get('age')
    print(age)

oldAge({"name": "Aayush", "age": 24}) # prints 74
oldAge({"name": "Aayush"}) # prints 50

#Q10.
d1 = {'1': 1, '2': 2, '3': 3}
d2 = {'4': 4, '5': 5, '6': 6}
d2.update(d1) #update method
d3=dict(d1, **d2)
print(d3)




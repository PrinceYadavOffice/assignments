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




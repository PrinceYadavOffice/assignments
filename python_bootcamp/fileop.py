#Q1
import pickle

with open('demo.txt') as file: #read mode
    print(file.read())

with open('demo.txt',"w") as file:# writing in file (it will replace with the new content)
    file.write("Hi , My name is Prince")

with open('demo.txt','a') as file:# append content to the file
    file.write("\nMy Compentency is Python")

with open('demo.txt','r+') as file:# file is open in the read write mode
    print(file.read())
    file.write("Append mode is used")


import jsonpickle


class Student:
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course

s1=Student('Prince',25,'Python')
s2=Student('Shubham',54,'Feen')
s3=Student('Ashutosh',5,'Devops')
s4=Student('Aman',3,'CloudOps')

# with open('demo.pickle','wb') as file:
#     pickle.dump(object,file)

#Q2

def saveStudentFile(*args):

    with open('student.txt','w') as file:
        for i in args:
            student = jsonpickle.encode(i)
            file.write(str([student])+"\n")

saveStudentFile(s1,s2,s3,s4)

#Q3
def readStudent():
    with open('student.txt','r') as file:
        reader=file.read()
        for i in reader.split('[]\n'):
            print(i)

readStudent()
#Q4
def readStudentGenerator():
    with open('student.txt','r') as file:
        reader=file.read()
        for i in reader.split('[]\n'):
            yield i

result=readStudentGenerator()
print("///////using generator///////")
for i in result:
    print(i)

#Q5

def replace_text(filepath, search_term, new_term, replace_all=False):
    with open(filepath,'r') as file:
        reader = file.read()
    with open(filepath,'w') as file:
        print(reader)
        if replace_all==False:
            new_data = reader.replace(search_term,new_term,1)
            file.write(new_data)
        else:
            new_data=reader.replace(search_term,new_term)
            file.write(new_data)

replace_text('demo2.txt','prince','Prince Yadav',replace_all=True)

#Q6
def replace_text_extened(filepath, search_term, new_term, replace_all=False):
    with open(filepath, 'r') as file:
        reader = file.read()

    count = 0
    with open(filepath, "w") as file:
        if replace_all==False:
            new_data = reader.replace(search_term,new_term,1)
            file.write(new_data)
            count+=1
            return f"word replaced {count}"
        else:
            new_data= reader.replace(search_term,new_term)
            count = new_data.count(new_term)
            file.write(new_data)
            return f"word replaced {count}"

result=replace_text_extened('demo2.txt','prince','Prince Yadav',replace_all=True)
print(result)


7
import datetime
from csv import DictWriter
def logger(func):
    def inner(a,b):
        ct = datetime.datetime.now()
        print("current time:-", ct)
        print(f"({a},{b})")
        result = func(a,b)
        with open('sum.log','r+') as file:
            strng = {'timestamp':ct,'input_params':(a,b),'result':result}
            healderlist=['timestamp','input_params','result']
            csv_writer=DictWriter(file, fieldnames=healderlist)
            print(type(csv_writer))
            csv_writer.writeheader()
            csv_writer.writerow(strng)
        return
    return inner
@logger
def sum2(a, b):
	return a + b
sum2(2,4)


#q8
import os
def rename_all(dir_path, pattern, suffix):
    path='/home/prince/assign/python_bootcamp/'+f'{dir_path}'
    for count,filename in enumerate(os.listdir(path)):
        print(filename)
        dst = pattern+str(count+1) + suffix+'.txt'
        src = path+str(filename)
        dst =path+dst
        os.rename(src, dst)

rename_all('folder1/folder2/','Test_file_', '_renamed')


#Q9

def list_files(dir_path, nested=True):
    path='/home/prince/assign/python_bootcamp/'+f'{dir_path}'
    if nested==False:
        for count, filename in enumerate(os.listdir(path)):
            if filename.endswith(".txt"):
                print(filename)
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    print(file)
list_files('folder1')









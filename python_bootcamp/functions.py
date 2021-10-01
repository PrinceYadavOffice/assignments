#Q1 cube()
def cube(num):
    return num*num*num
print(cube(9))
print(cube(2))
print(cube(5))

#Q2.
def convert_cel_to_far(c):
    f = c * 9 / 5 + 32
    return f"{c} degrees C = {f:.2f} degrees F"

def convert_far_to_cel(f):
    c = (f - 32) * 5 / 9
    return f"{f} degrees F = {c:.2f} degrees C"

f = int(input("Enter a temperature in degrees F: "))
print(convert_far_to_cel(f))
c = int(input("Enter a temperature in degrees C: "))
print(convert_cel_to_far(c))


#Q3
def func1(*args):
    print("Printing Values :")
    for i in args:
        print(i)

func1(20,40,60)
func1(80,100)

#Q4
def calculation(a, b):
    return (a+b,a-b)

res = calculation(40, 10)
print(res)


#Q5
def show_employee(name, salary=9000):
    return f"Name :{name} salary:{salary}"

print(show_employee("Ben",12000))
print(show_employee("Jessa"))

#Q6
def func2(**kargs):
    print("No of kargs :",len(kargs))
    print("Keys  and values in kargs: ")
    for k,v in kargs.items():
        print(f" Key :{k}, Value: {v}")

d={'name':'prince','age':25,'country':'India','role':'software Engineer'}
func2(**d)


#Q7.

def add(a, b, c="sum of two numbers"):

    return a + b

def catch(*agrs,**kwargs):
    print("args : ",agrs)
    print("kwargs: ",kwargs)
    result=agrs[0](agrs[1],agrs[2],kwargs.get('c'))
    print(f"Result: {kwargs.get('c')} {result}")

catch(add, 1, 2, c="this is sum")



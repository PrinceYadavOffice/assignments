class Multiple:
    def __init__(self,l):
        self.l=l
        self.i=-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i==len(self.l)-1:
            raise StopIteration
        self.i=self.i+1
        return self.l[self.i]*2

m=Multiple([2,6,7,8])
for i in m:
    print(i)


def is_iterable(parameter):
    try:
        iter(parameter)
        return True
    except TypeError:
        return False

print(f"Is Iterable:{is_iterable([1,1,2,3,3,4])}")

def multiple(l):
    for i in l:
        yield i*2

l=[2,6,7,8]
double = multiple(l)
for i in double:
    print(i)


# q2 using generator
print("/// Using Generator//////")

l=[2,6,7,8]
double=(i*2 for i in l)
for i in double:
    print(i)


# decorators with higher order function
def hod(func):
    def wrapper():
        print("Inside the Decorator")
        print(func())
        print("Execution Ended")
    return wrapper

def my_details():
    return "Hi My Name Is Prince"

my_deatils = hod(my_details)
my_deatils()

#Q9

def dec1(func):
    def wrapper():
        result = func()
        result = result.replace(" ","_")
        return result
    return wrapper

def dec2(func):
    def wrapper():
        result = func()
        result = result.upper()
        return result
    return wrapper
def greet():
    return 'Welcome to Python'

add_Underscore = dec1(greet)
convert_Upperase = dec2(greet)
print(add_Underscore())
print(convert_Upperase())

#10
def newlist(number):
    return number%10
numbers = [77, 88, 44, 33]
result = map(newlist, numbers) #using map
print(list(result))
#using list comprehenion
result1 = [i%10 for i in numbers]
print(result1)
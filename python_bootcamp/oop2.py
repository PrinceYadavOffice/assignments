#Q1.Create a class Employee with first_name, last_name and salary attributes. Add an attribute email_Id which should always be first_name.last_name@tothenew.com.

class Employee:
    raise_percentage = 10
    def __init__(self, first_name,last_name,salary=0):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary

    def addEmail(self):
        self.email = self.first_name+"."+self.last_name+"@tothenew.com"
        return f"Email added succesfully {self.email}"

    def raise_salary(self):
        self.salary += (self.salary * Employee.raise_percentage//100)
        return self.salary

    @classmethod
    def raise_percent(cls,percentage):
        Employee.raise_percentage+=percentage
        return Employee.raise_percentage

e1 = Employee('amit','dubey',100000)
print(e1.addEmail())
print(f"New salary {e1.raise_salary()}")
print(f"New salary {e1.raise_salary()}")



#Q4.

class Vehicle:
    def __init__(self, make, mileage, capacity):
        self.make=make
        self.mileage=mileage
        self.capacity=capacity
    def get_fare(self):
        pass
class Car(Vehicle):
    def __init__(self, make,mileage,capacity):
        super(Car, self).__init__(make,mileage,capacity)
    def get_fare(self):
        fare = (self.mileage * self.capacity) + 15 / 100
        return fare
class Bus(Vehicle):
    def __init__(self, make, mileage, capacity):
        super(Bus,self).__init__(make,mileage,capacity)
    def get_fare(self):
        fare = (self.mileage * self.capacity) + 25/100
        return fare
car = Car('Maruti',18,5)
bus= Bus('Volvo',15,100)
print(f" Car Fare : {car.get_fare()}")
print(f" Bus Fare : {bus.get_fare()}")

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y =y

    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)
    def __repr__(self):
        return f"({self.x},{self.y})"
p1 = Point(3,4)
p2 = Point(2,6)
p3 = p1+p2
print(p3)

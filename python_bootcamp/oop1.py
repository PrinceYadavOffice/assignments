class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def display(self):
        print(self.name)
        print(self.__age)

    def getAge(self):
        print(self.__age)

    def setAge(self, age):
        self.__age = age

# prince = Person('Prince',25)
# prince.display()
# prince.getAge()
# prince.setAge(24.5)
# prince.display()


class Vehical:
    def __init__(self,no_of_wheels=0, current_speed=0):
        self.no_of_wheels=no_of_wheels
        self.current_speed=current_speed

    def __repr__(self):
        if self.no_of_wheels==2:
            return f" Bike speed {self.current_speed}"
        if self.no_of_wheels==4:
            return f"Car Speed {self.current_speed}"

    def start(self):
        return "Engine Started"

    def stop(self):
        self.current_speed=0
        return f"Speed {self.current_speed}"

    def accelerate(self):
        self.current_speed+=10
        return f"Speed is {self.current_speed} KMPH"
        pass
    def brake(self):
        self.current_speed-=10
        return f"Speed {self.current_speed}"


Bike = Vehical(2)
Car = Vehical(4)
print(Bike)
print(Bike.start())
print(Bike.accelerate())
print(Bike.accelerate())
print(Bike.brake())
print(Bike.stop())
print(Car)
print(Car.start())
print(Car.accelerate())
print(Car.brake())
print(Car.stop())


class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email

    def __repr__(self):
        return f"{self.email}"

prince= User('Prince','prince.yadav@tothenew.com')
amit = User('Amit Dubey','amit.dubey@tothenew.com')
shubham = User('Shubham','shubham@tothenew.com')
amulya = User('Amulya Sharma','amulya.sharma@tothenew.com')

print("\n",prince,"\n",amit,"\n",shubham,"\n",amulya)


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,l):
        node = Node(l[0])
        self.head=node
        ptr = self.head
        for i in range(1,len(l)):
            node= Node(l[i])
            ptr.next=node
            ptr =ptr.next
    def __repr__(self):
        ptr = self.head
        while ptr:
            if ptr.next:
                print(f"{ptr.data} is pointing to {ptr.next.data}")
            else:
                print(f"{ptr.data} is pointing to {ptr.next}")
            ptr=ptr.next
        return ''

    def is_cyclic(self):
        ptr = self.head
        while ptr:
            if ptr.next == self.head:
                return True
            ptr = ptr.next
        return False

list_1= LinkedList([1,2,3,4])
print(list_1)
print(list_1.is_cyclic())

class CyclicLinkedList:
    def __init__(self,l):
        node = Node(l[0])
        self.head=node
        self.tail=self.head
        ptr = self.head
        for i in range(1,len(l)):
            node= Node(l[i])
            ptr.next=node
            ptr =ptr.next
        self.tail=ptr
        self.tail.next=self.head
    def __repr__(self):
        ptr = self.head
        while ptr:
            if ptr.next:
                print(f"{ptr.data} is pointing to {ptr.next.data}")
            else:
                print(f"{ptr.data} is pointing to {ptr.next}")
            if ptr.next == self.head:
                break
            ptr=ptr.next

        return ''

    def is_cyclic(self):
        ptr = self.head
        while ptr:
            if ptr.next == self.head:
                return True
            ptr = ptr.next
        return False

list2 = CyclicLinkedList([1,2,3,4,5])
print(list2)
print(list_1.is_cyclic())
print(list2.is_cyclic())



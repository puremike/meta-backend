class FirstClass:
    a = 2 * 90
    b = "Hello World!"
    x = 10
    y = 20

    def first_hello(self):
        return self.b

    def multiplyXY(self):
        z = self.x * self.y
        return "Multiplication = {0}".format(z)


first_class = FirstClass()
print(first_class.a)
print(first_class.first_hello())
print(first_class.multiplyXY())

print("\nHOUSE COST EVALUATION")


class House:
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, room_rate, bath_rate):
        room_cost = room_rate * self.num_rooms
        bath_room_cost = bath_rate * self.bathrooms
        print(
            "Cost evaluation for {0} rooms with rate of {1} = {2}".format(
                self.num_rooms, room_rate, room_cost
            )
        )
        print(
            "Cost evaluation for {0} bathrooms with the rate of {1} = {2}".format(
                self.bathrooms, bath_rate, bath_room_cost
            )
        )


house = House()
print(house.cost_evaluation(25, 11))

house.num_rooms = 10  # updated num_rooms
house.bathrooms = 7  # updated bathroom

print(house.cost_evaluation(30, 13))

print("\nINSTANTIATE A CUSTOM OBJECT")


""" "__init__" is a reserved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class."""


class Recipe:
    # using the "__init__" constructor to allow the class initialize the attributes of a class
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        return "The {0} contains {1} and takes {2}min to prepare".format(
            self.dish, self.items, self.time
        )


pizza = Recipe("Pizza", ["Cheese", "Tomatoes", "Chicken"], 30)
pasta = Recipe("Pasta", ["Penne", "Sauce"], 45)

print(pizza.items)
print(pasta.time)
print(pizza.contents())
print(pasta.contents())

print("\nEXERCISE: DEFINE A CLASS")


class MyFirstClass:
    print("Who wrote this?")
    index = "Author:Book"

    def hand_list(self, philosopher, book):
        print(self.index)  # or print(MyFirstClass().index)
        return "{0} wrote the book: {1}".format(philosopher, book)


whodunnit = MyFirstClass()
print(whodunnit.hand_list("Sun Tzu", "The Art of War"))
print(whodunnit.hand_list("Mark Manson", "The Art of Not Giving a Fuck"))


print("\nNATHAN & ROGER PAYSLIPS:")


class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def pay_status(self):
        if self.payment == "yes":
            return self.name + " has been paid " + str(self.amount)
        return self.name + " has not been paid!"


nathan = Payslips("Nathan", "no", 10000)
roger = Payslips("Roger", "no", 15000)

print("...BEFORE PAYMENT...")
print(nathan.pay_status())
print(roger.pay_status())

print("....AFTER PAYMENT...")
# both nathan and roger pay has been updated by calling the pay()
nathan.pay()
roger.pay()
print(nathan.pay_status())
print(roger.pay_status())

print("\nINHERRITANCE")


class Employee:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last


class Supervisors(Employee):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password


class Chefs(Employee):
    def leave_request(self, days):
        return "May I take a leave for {0} days".format(days)


adrian = Supervisors("Adrian", "A", "passmenow")
madam = Chefs(
    "Emily", "A"
)  # we have to pass the name and last argument because Chef is a subclass of Employee and the Employee has two positional arguments of name and last
print(madam.leave_request(30))
print(adrian.name)
print(adrian.password)
print(madam.name)


print("\nEXERCISE: CLASSES AND OBJECT EXPLORATION")


class A:
    def __init__(self, c):
        print("---------Inside class A----------")
        self.c = c

    print("Print inside A.")

    def alpha(self):
        c = self.c + 1
        return c


print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())


class B:
    def __init__(self, a):
        print("---------Inside class B----------")
        self.a = a

    print(a.alpha())
    d = 5
    print(d)
    print(a)


print("Instantiating B..")
b = B(a)
print(a)


print("\nABRACT CLASS:......")
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass


print("\n")
"""METHOD RESOLUTION ORDER: It determines the order in which a given method or attibute passed is searched. The order is called the LINEARIZATION OF A CLASS.
Old styled classes uses Depth-First Search Algorithm (DFS) and C3 Linearization Algorithms

C3 Linearization Algorithm:
    Adheres to Monotonicity
    Follows Inheritance Graph
    Visits super class after local classes
"""


# Example 1
class A:
    def a(self):
        return "Function inside A"


class B:
    def a(self):
        return "Function inside B"


class C(B, A):
    pass


# Driver code
c = C()
print(c.a())

# Class C inherits from classes B and A. When I don't find any function a() inside class C, I should search for classes B and A and its important that I do it in that order.


class A:
    def d(self):
        return "Function inside A"


class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E, D, C):
    pass


f = F()
print(f.d())
print(F.mro())

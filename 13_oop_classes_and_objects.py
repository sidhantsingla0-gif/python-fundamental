'''class Student:
    name = "Sidhant"
    age = 20
    course = "B.Tech in CSE"

student1 = Student()

print("Student Name:", student1.name)
print("Student Age:", student1.age)
print("Student Course:", student1.course)
'''

'''class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Student name:", self.name)

student1 = Student("Sidhant", 20, "B.Tech in CSE")
student2 = Student("Ujla", 19, "B.Tech in CSE")

student1.display()     #Student.display(student1)
print("Student 1 Age:", student1.age)
print("Student 1 Course:", student1.course)


print("Student 2 Name:", student2.name)
print("Student 2 Age:", student2.age)
print("Student 2 Course:", student2.course)'''


'''class Student:

    school = "ABC College"

    def show(self):
        print("Instance method")

    @classmethod
    def school_name(cls):
        print(cls.school)

    @staticmethod
    def welcome():
        print("Welcome students!")


s = Student()

s.show()
Student.school_name()
Student.welcome()'''


'''class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(2000)

print(account.get_balance())

# print(account.__balance)   Attribute error: 'BankAccount' object has no attribute '__balance' 
'''

'''  Inheritance Example
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()'''

"""class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def eat(self):
        super().eat()
        print("Dog is eating")


dog = Dog()
dog.eat()"""

"""class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)"""


'''class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()'''

'''from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()'''

# Practise question
'''
class Student:
    name = "Sidhant"
    marks = 89
    course = "B.Tech in CSE"

student1 = Student()

print("Student Name:", student1.name)
print("Student marks:", student1.marks)
print("Student Course:", student1.course)'''

'''class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount


    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print("Balance of account is",account.get_balance())

account.deposit(2000)
print("Balance after deposit",account.get_balance())

account.withdraw(1000)

print("Balance after withdraw",account.get_balance())
'''


class Machine:
    def __init__(self, name, status="Stopped"):
        self.name = name
        self.status = status

    def start(self):
        self.status = "Running"
        print(f"{self.name}: starting machine -> status is now {self.status}.")

    def show_status(self):
        print(f"{self.name} [{self.status}]")


class Motor(Machine):
    def __init__(self, name, rpm, status="Stopped"):
        super().__init__(name, status)
        self.rpm = rpm

    # Overrides Machine.start()
    def start(self):
        self.status = "Running at full speed"
        print(f"{self.name} (Motor, {self.rpm} RPM): energizing windings -> {self.status}.")


machine = Machine("Pump-01", "Idle")
machine.show_status()  # Pump-01 [Idle]
machine.start()        # Pump-01: starting machine -> status is now Running.

motor = Motor("Induction-Motor-A", rpm=1450)
motor.show_status()    # Induction-Motor-A [Stopped]  (inherited from Machine)
motor.start()          # Induction-Motor-A (Motor, 1450 RPM): energizing windings -> Running at full speed.
motor.show_status()    # Induction-Motor-A [Running at full speed]
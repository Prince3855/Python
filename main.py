"""
1. Class
- Self defined data type
- Bluprint
- Ex. Car
    - Data / attribute / property
        - Ex. color, brand, name, top speed etc
    - Behaviour / method
        - Breaks, start, Accelerate, drive
"""
class Car:
    pass

"""
2. Object
- Instance of class
- Ex. Centro Car 
"""
class Car:
    pass

swift = Car()
print(type(swift))

"""
3. Constructure and data members
- To initialize
- when we create or construct an object of class there is method __init__ which is called known as constructor
- special method - call it self
- used to check and initialize things before starting
    ex. check intent status before starting application
- first argument is reference of object 
"""
class Student:
    def __init__(self, name, rollNumber, marks):
        # print(self)
        print("Constructing student")
        self.name = name
        self.rollNumber = rollNumber
        self.marks = marks

s1 = Student('Prince', 1, 98)
print(s1.rollNumber)


"""
4. Methods
"""
class Student:
    def __init__(self, name, rollNumber, marks):
        # print(self)
        print("Constructing student")
        self.name = name
        self.rollNumber = rollNumber
        self.marks = marks
    def study(self):
        print(f"{self.name} is studying..")
        self.play()
    
    def play(self):
        print(f"{self.name} is playing..")


s1 = Student('Prince', 1, 98)
print(s1.study())


"""
- Print object using __str__ method
"""
class Student:
    def __init__(self, name, rollNumber, marks):
        # print(self)
        print("Constructing student")
        self.name = name
        self.rollNumber = rollNumber
        self.marks = marks

    def __str__(self) -> str:
        return f"{self.name}, {self.rollNumber}, {self.marks}"

s1 = Student('Prince', 1, 98)
print(s1)


"""
- Class level variables VS Instance variables
"""
class Student:
    numberOfStudent = 0
    def __init__(self, name, rollNumber, marks):
        # print(self)
        print("Constructing student")
        self.name = name
        self.rollNumber = rollNumber
        self.marks = marks
        Student.numberOfStudent += 1

    def __str__(self) -> str:
        return f"{self.name}, {self.rollNumber}, {self.marks}"

s1 = Student('Prince', 1, 98)
s2 = Student('Jay', 2, 90)
print(Student.numberOfStudent)


"""
# Encapsulations
## Access modifier : public/private
- Public
    __varName to make it aprivate add __ as name prefix
- Public
    - By default variables are public
"""
class Student:
    numberOfStudent = 0
    def __init__(self, name, rollNumber, marks):
        # print(self)
        print("Constructing student")
        self.__name = name
        self.rollNumber = rollNumber
        self.marks = marks
        Student.numberOfStudent += 1

    def __str__(self) -> str:
        return f"{self.name}, {self.rollNumber}, {self.marks}"
    
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

s1 = Student('Prince', 1, 98)
print(s1.getName())
s1.setName('Foo')
print(s1.getName())


"""
- We can also make method private like variables
- Used for internal method to avoid access from outside the class
- for class variables if we write getter and setter method then that will be static method and noted by @staticmethod decorator
"""
class Student:
    __numberOfStudent = 0
    def __init__(self, name, rollNumber, marks):
        # print(self)
        print("Constructing student")
        self.__name = name
        self.rollNumber = rollNumber
        self.marks = marks
        Student.__numberOfStudent += 1
    
    def setName(self, name, password):
        if password != self.__auth():
            return
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def __auth(self):
        return 'password'
    
    def getNumberOfStudent(self):
        return Student.__numberOfStudent
    
    @staticmethod
    def getTotalNumberOfStudent():
        return Student.__numberOfStudent

s1 = Student('Prince', 1, 98)
print(s1.getName())
s1.setName('Foo', 'password')
print(s1.getName())
print(s1.getNumberOfStudent())
print(Student.getTotalNumberOfStudent())


"""
# Inheritance
- To add additional behavior
- To reuse existing
- To avoid duplication
- Sub class inherits
    - non private attributes
    - non private methods
    - constructor and magic methods
- We can make variables or method protected by adding _ in name still they are simple normal variables we can aceess it from anywhere but for developers they can use it from class and inherited classes
- If method is overridden they it will use method written in class not from paremt class
- Use super method to access methods of parent class can not acess attribute
"""
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def login(self):
        print(f"Logging in as {self.email}")

    def _logout(self):
        print("Logging out")

    def displayDetails(self):
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")

class Student(User):
    def __init__(self, email, password, student_id):
        super().__init__(email, password)
        self.student_id = student_id
    
    def displayDetails(self):
        super().displayDetails()
        print(f"Student ID: {self.student_id}")

    def study(self):
        print("Studying")
        self._logout()


s1 = Student('prince@gmail.com', 'Prince@123', 23)
print(s1.displayDetails())


"""
# Types of Inheritance
1. Simple Inheritance => Parent <- Childe
2. Hierarchical Inheritance => Parent <- Childe1, Childe 2
3. Multilevel Inheritance => Grandparent <- Parent <- Childe1
4. Multiple Inheritance => multiple parent 
    - not allowed in java  (ambiguity)
    - allowed in python
        - Order matter for multiple parent 
        class Father:
        class Mother:
        class Childe(Father, Mother):
        - Child tak details from Father first if avilable
5. Hybrid Inheritance
    mro: A <= B,C <= D then it will call contructor in thi order: D => B => C => A
"""
class GrandParent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def occupetion(self):
        print(f"GrandParent is doctor")


class Parent(GrandParent):
    pass

class Childe(Parent):
    def occupetion(self):
        super().occupetion()


child = Childe('Prince', 23)
print(child.occupetion()) # output: GrandParent is doctor

"""
# Polymorphism
2. Method overriding
- write method with diff logic in child class
1. Method overloading
    - same method name but different number of arguments or different type of arguments
    ex. sum(1,2), sum(1,2,3), sum([1,2], [3,4])
    - We can not achive this directly in python 
    - to achive orvrloading use default value for un passed argument ex. sum(a,b,c=0)
3. Operator overloading
- using methods we can over load operator logic ex. __sum__, __mul__ etc
"""

"""
# Abstraction (hidden)
- Used to hidding important details
- usefull where group of related object which shares same features 
    - same feature but different implementations like area calculate in shape
    - so to create schema or bluprint class it will be abstract class
- so it help to create blueprint
"""

from abc import ABC,abstractmethod
class User(ABC):
    
    @abstractmethod
    def login(self):
        pass

    def logout(self):
        print('logout')

    @abstractmethod
    def auth(self):
        pass


class Buyer(User):
    def login(self):
        print('Buyer logged in')
    
    def auth(self):
        print('Buyer authenticated')

    def checkObject(self, link):
        print(f'Checking object: {link}')

b1 = Buyer()
print(b1.auth())
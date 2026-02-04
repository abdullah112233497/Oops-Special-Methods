# OOPS_special_methods:-
# These are also called Dunder Methods
# __str__
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}" 
a=Student("Abdullah",123)
# a.result()
print(a)  # It points the __str__ method

# __len__
class Payment:
    def __init__(self,owner,payments):
        self.owner=owner
        self.payments=payments
    def __len__(self):
        return len(self.payments)
p=Payment("Abdullah",[123,234,1234])
print(len(p)) #It points the __len__ method


#__repr__
class Developer:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def __repr__(self):
        return f"{self.n1},{self.n2}"
d=Developer(12,23)
print(d) #It points the __repr__ method


#__add__
class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n + other.n
number1=Number(2)
number2=Number(3)
print(number1+number2) #It points the __add__ method

#__eq__
class Eq:
    def __init__(self,q):
        self.q=q
    def __eq__(self,other):
        return self.q ==other.q
eq1=Eq(2)
eq2=Eq(12)
print(eq1==eq2) #Return True/False

#__It__---- For the Less than
#__gt__---- For the Greater than

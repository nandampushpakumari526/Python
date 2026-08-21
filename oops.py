#oops
#syntax

'''class classname():
    #attributes
    name="pushpa"
    age=20
    place="vja"
    def fname(method_name):
        print("statements........")
a=classname()
print(dir(a))
a.fname()'''

#class declaration
'''class Details():
    name="pushpa"
    age=20
    place="vja"
    def names(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.names()'''

#object instantiation
'''class betails():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
    def display(pushpa):
        print(pushpa.name,pushpa.age,pushpa.place)
a=betails()
#print(dir(a))
a.data("pushpa",22,"vja")
a.display()
b=betails()
b.data("devi",30,"hyd")
b.display()'''


'''class Data():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Data("puji",22,"hyd")
print(dir(a))
a.display()'''


'''class Data():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=input()
b=int(input())
c=input()
a=Data(a,b,c)
#print(dir(a))
a.display()'''


'''class Data():
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input()
    def display(self):
        print(self.name,self.age,self.place)
a=Data()
#print(dir(a))
a.display()'''


#diff b\w _ and __
'''class Employee1():
    def __init__(self):
        self.name="pushpa"
        self._mailid="pushpa@codegnan.com"
        self.__salary=10000#private variable
class Employee2():
    def __init__(self):
        self.name="divya"
        self._mailid="divya@codegnan.com"
        self.__salary=20000#private variable
a=Employee1()
#print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee1__salary)
b=Employee2()
#print(dir(b))
print(b.name)
print(b._mailid)
#print(b.__salary)
print(b._Employee2__salary)'''


#operator overloading
'''a=4;b=8
print(a+b)
print(a.__add__(b))
print(a.__sub__(2))
print(a.__mul__(6))
print(a.__pow__(2))
#print(a.__div__(4))
print(a.__eq__(4))
print(a.__le__(8))
print(a.__ge__(10))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(6)
y=B(4)
#x=6
#y=4
print(x+y)'''

#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("product is",a*b)
        else:
            print("program ends....")
a=new()
#a.sum()
#a.sum(3,4,8)
a.sum(4,5)'''

#method overriding
'''class Animal():
    def speak(self):
        print("animal can make a sounds")
class Dog():
    def speak(self):
        print("dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

'''class car():
    def vehical(self):
        print("thar")
class bike():
    def vehical(self):
        print("vespa")
a=car()
b=bike()
a.vehical()
b.vehical()'''

#Inheritance
#single inheritance
'''class RBI():#parent class
    cash=1000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI():#child-1
    pass
class HDFC(RBI):#child-2
    cash=500
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''
#multiple inheritance
'''class Father():#parent class-1
    def f_h(cls):
        print("Father height is 5 ft")
class Mother(Father):#parent class-2
    def m_w(cls):
        print("Mother weight is 50 kg")
class chaild(Father,Mother):#chaild-1
    def c_a(cls):
        print("chaid age is 10 years")
a=chaild()
a.f_h()
a.m_w()
a.c_a()'''
#multilevel inheritance
''''class grandparent():
    def land(self):
        print("1 acar")
class parent(grandparent):
    def house(self):
        print("100 square")
class child(parent):
    def bike(self):
        print("pulsar")
a=child()
a.land()
a.house()
a.bike()'''
#hirarchical inheritance
'''class employee():
    def company(self):
        print("Codegnan")
class trainer(employee):
    def teaching(self):
        print("teaching")
class student(employee):
    def code(self):
        print("learn coding")
a=trainer()
a.company()
a.teaching()
b=student()
b.company()
b.code()'''
#hibrid inheritance
'''class person():#parent
    def details(self):
        print("pushpa kumari")
        print("from mangalagiri")
class trainer(person):#child-1
    def teaching(self):
        print("teaching")
class student(person):#child-2
    def learing(self):
        print("learing course")
class promang(trainer,student):#grand child
    def manage(self):
        print("managing ")
b=promang()
b.details()
b.teaching()
b.learing()
b.manage()'''
#super
'''class parent():#superclass
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):#super class
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("pushpa",28)
print(a.age)
print(a.name)'''
#encapsulation
#publicdata
'''class A():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class B(A):
    def method2(self):
        print(self.publicdata)
obj1=B()
obj1.method1()
obj1.method2()'''
#protecteddata
'''class A():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class B(A):
    def method2(self):
        print(self._protecteddata)
obj1=B()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

#__privatedata
'''class A():
    __privatedata="pushpa"
    def method1(self):
        print(self.__privatedata)
class B(A):
    def method2(self):
        print(self._A__privatedata)
obj1=B()
obj1.method1()
obj1.method2()'''
#abstraction
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method()'''

'''class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A():
    def method1(self):
        print("Python course")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("Data Science")
obj1=A()
obj1.method1()#------it get error bcz abstractmethod we have 2 or more classes'''

from abc import ABC,abstractmethod
class A(ABC):#parent class
    def method1(self):
        pass
    def method2(self):
        print("python course")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("Data science")
    def method3(self):
        print("Java full stack")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()


    



















































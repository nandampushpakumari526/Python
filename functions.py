#functions
'''a=10
b=20
print("the sum is",a+b)
print("the diff is ",a-b)
print("ther product",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is ",a-b)
print("ther product",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is ",a-b)
print("ther product",a*b)
def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is ",a-b)
    print("ther product",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)
def calop(a,b):
    print("the power",a**b)
    print("the divistion",a%b)
    print("the integer div",a//b)
calop(2,1)
calop(4,7)
calop(4,6)
def add(a,b):
    print(a+b)
add(5,4)
while True:
    def add():
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(a+b)
    add()
def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()
add() 
def mul(a,b):
    print(a*b)
mul(4,5)
def mul(a,b):
    return a*b
print(mul(4,6))

def cal (a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(4,3)
def cal (a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(4,3))
def fullname():
    first=input()
    second=input()
    print(first+" "+second)
fullname()'''
'''while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        c=int(input("choose the option \n1.add\n2.differance\n3.product"))
        if c==1:
            print(" sum of a and b=",a+b)
        elif c==2:
            print(" sum of a and b=",a-b)
        elif c==3:
            print(" sum of a and b=",a*b)
    cal()'''
    
'''def cal():
    a=int(input("a value"))
    b=int(input("b value"))
    while True:
        c=int(input("choose the option \n1.add\n2.differance\n3.product"))
        if c==1:
            print(" sum of a and b=",a+b)
        elif c==2:
            print(" sum of a and b=",a-b)
        elif c==3:
            print(" sum of a and b=",a*b)
cal()'''

'''def cal():
    a=int(input("a value"))
    b=int(input("b value"))
    c=int(input("choose the option \n1.add\n2.differance\n3.product"))
    if c==1:
        print(" sum of a and b=",a+b)
    elif c==2:
        print(" sum of a and b=",a-b)
    elif c==3:
        print(" sum of a and b=",a*b)
cal()
def add():
    print("sum of numbers",a+b)
def sun():
    print("differance of numbers",a-b)
def pro():
    print("product of two numbers",a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    c=int(input("choose the option \n1.add\n2.differance\n3.product\n"))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        pro()'''


    




'''print("--------------split bill----------------")
#normal
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
c=b/a #c=b//a
print("ecach per head=",c)
#f string
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
c=b/a #c=b//a
print(f"ecach per head={c}")
#formating string
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
c=b/a #c=b//a
print("ecach per head= {}".format(c))
#using functions
#method 1
def bill():
    a=int(input("enter the how many people u have"))
    b=int(input("enter the total value u have"))
    c=b//a
    return c
print(bill())
#method 2
def bill():
    a=int(input("enter the how many people u have"))
    b=int(input("enter the total value u have"))
    c=b/a
    print("ecach per head=",c)
bill()
#method 3
def bill(a,b):
    c=b//a
    print("ecach per head=",c)
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
bill(a,b)'''
#key word and postinal arguments
'''def detalis(id,name,mail):
    id=10
    name="pushpa"
    mail="pushpa@gmail.com"
    print(id,name,mail)
detalis(id="id",name="name",mail="mail")
def detalis(id,name,mail):
    print(id,name,mail)
detalis(id=20,name="puji",mail="puji@gmail.com")
detalis(id=30,name="teja",mail="teja@gmail.com")
detalis(id=40,name="kusuma",mail="kusuma@gmail.com")
detalis("devi@gmail.com",50,"devi")
detalis(mail="kusuma@gmail.com",name="kusuma",id=40)'''
#default arguments
'''def grocery(item,price):
    print("item is %s "%item)
    print("price is %.2f" %price)
grocery("rice",1500)
def grocery(item="suger",price=100):
    print("item is %s "%item)
    print("price is %.2f" %price)
grocery()
def grocery(item,price=200):
    print("item is %s "%item)
    print("price is %.2f" %price)
grocery("dhal")
def grocery(item="ghee",price):
    #non def arg follows dwf arg
    print("item is %s "%item)
    print("price is %.2f" %price)
grocery(500)'''
#cake ,price,quantiy
'''def cake(cakes,price,quantity):
    print("item is %s "%cakes)
    print("price is %.2f" %price)
    print("quantity is %s "%quantity)   
cake("chocake",1500,"1kg")
def cake(cakes="butcake",price=600,quantity="2kg"):
    print("item is %s "%cakes)
    print("price is %.2f" %price)
    print("quantity is %s " %quantity)   
cake()
def cake(cakes,price,quantity="3kg"):
    print("item is %s "%cakes)
    print("price is %.2f" %price)
    print("quantity is %s " %quantity)
cake("vennela",300)

def cake(item="vennela",price,quantity):
    print("item is %s "%cakes)
    print("price is %.2f" %price)
    print("quantity is %s " %quantity)
cake(300)'''
#* is used to unpack the elements
'''a=[10,20,30,40,50]
print(a)
print(*a)
a=(10,20,30,40,50)
print(a)
print(*a)
a={10,20,30,40,50}
print(a)
print(*a)

a={"year":2026,"month":"july"}
print(a)
print(*a)

a,b,c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)
a,b,c=2,3,4
print(a)
print(b)
print(c)
a,*b,c=2,3,4,5,6,7,8,9
print(a)
print(*b)
print(c)
a="codegnan"
print(a)
print(*a)
a,b,c="codegnan"
print(a)
print(b)
print(c)
a,b,c="cod"
print(a)
print(b)
print(c)
a,b,*c="codegnan"
print(a)
print(b)
print(*c)
#variable length argument
def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[4,5,6,7,8]
check(*b)
c={6,8,9,10}
check(*c)
d={"name":"pushpa","city":"vja"}
check(*d)
def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i)in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(3,4,5.2,3.4)
check1(3,4,2,5,3.6,2.4,"pushpa")
#kwargs(**)
def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],"names":["sai","siva","ravi"],"status":["p","a","p"]}
check(**details)'''
'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
detalils={"idnos":[10,20,30],"names":["sai","siva","ravi"],"status":["p","a","p"]}
check(**detalils)
#both * and** usage
def final(*a,**b):
    d=3#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,3.5,6.2)
final(*data)
detalils={"idnos":[10,20,30],"names":["sai","siva","ravi"],"status":["p","a","p"]}
final(**detalils)
final(*data,**details)
#max(),min(),sum()
print(max(5,7,9,10,20,40))
print(min(5,7,9,10,20,40))
s=5,7,9,10,20,40
print(sum(s))
#marks analysis report
n=int(input("how may stud:"))
score=[]
for i in range(1,n+1):
    s=int(input("student {} marks:".format(i)))
    score.append(s)
    c=sum(score)
    a=c/n
print("total:",n)
print("max",max(score))
print("min",min(score))
print("sum",c)
print(f"avg {a:.2f}")'''

#global and local variables
#first case of global variable
'''a=2
def check1():
    print("the inside value is",a)
check1()
print("outside value is ",a)
#second case of global variable
a=4
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()'''
#third case of both global and local variable
'''a=3
b=8
def check3():
    a=6
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12
    b=b+a
    print("value of b is ",b)
check3()
print("a vale is ",a)
print("b value is ",b)'''
#usage of global key word
#when user want's to create a variable inside
#the function directly carry forword the updated value then we need to use global keyword
#global local(or) scope of variables both are same
'''a=4
def final():
    global a,b
    print("inside value is ",a)
    a=15
    print("update value is ",a)
    b=20
    b=b+a
    print("value of b is ",b)
final()
print("a value is ",a)
print("b value is ",b)'''
#generators
#a=[expr for var in collection/range]
'''a=[i for i in range(16)]
print(a)
print(type(a))
a=(i for i in range(16))
print(*a)
print(type(a))
a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
print(set(a))=
a,b=(int(x) for x in input("values").split(","))
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))#hear * is important bcz when we use the generators we have not getthing the answer it showes the bites code so we use *
a,b=(int(x) for x in input("values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''#yield v/s return
def mygen():
    #return "vija"
    #return "hyd"
    #return "vzg"
    return "vija","hyd","vzg"
print(*mygen())
def mygen():
    yield "python"
    yield "java"
    yield "c"
print(*mygen())
#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))#stop iteration


    


    
    
















    

























    


        
    


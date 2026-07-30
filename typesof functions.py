
print("--------------split bill----------------")
#normal
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
c=b/a #c=b//a
print("each per head=",c)
#f string
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
c=b/a #c=b//a
print(f"each per head={c}")
#formating string
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
c=b/a #c=b//a
print("each per head= {}".format(c))
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
    print("each per head=",c)
bill()
#method 3
def bill(a,b):
    c=b//a
    print("each per head=",c)
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
bill(a,b)
#key word and postinal arguments
def detalis(id,name,mail):
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
detalis(mail="kusuma@gmail.com",name="kusuma",id=40)
#default arguments
def grocery(item,price):
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
grocery(500)
#cake ,price,quantiy
def cake(cakes,price,quantity):
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
cake(300)
#* is used to unpack the elements
a=[10,20,30,40,50]
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
check(**details)
def check(**a):
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
print(f"avg {a:.2f}")


#global and local variables
#first case of global variable
a=2
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
check2()
#third case of both global and local variable
a=3
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
print("b value is ",b)
#usage of global key word
#when user want's to create a variable inside
#the function directly carry forword the updated value then we need to use global keyword
#global local(or) scope of variables both are same
a=4
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
print("b value is ",b)
#generators
#a=[expr for var in collection/range]
a=[i for i in range(16)]
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
print(check(a,b))
#yield v/s return
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

#if condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=15
if a<b:
    print("True")
a=6
b=9
if a>b:
    print("True")
a=12
b=14
if a<b:
    print("True")
a=10
b=15
if a>=b:
    print("True")
a=20
b=40
if a<=b:
    print("True")
a=20
b=40
if a!=b:
    print("not equal")
a=5
b=5
if a==b:
    print("equal")
a=8
if a>3:
    print("greater")
a="python"
if a =="python":
    print("equal")
a="python"
if a!="java":
    print("equal")
a=int(input("a value"))
b=int(input("b value"))
if a<b:
    peint("True")
a=int(input("enter the value"))
if a>40:
    print("greater")
a=input("data")
if a=="python":
    print("true")'''
#if condition by using logical operators
'''a=5
b=7
if a<b and b>a:
    print("true")
a=9
b=11
if a<=b and b>=a:
    print("true")
a=4
b=6
if a!=b and a==b:
    print("False")
a=8
b=12
if a<b or b>a:
    print("true")
a=8
b=12
if a<=b or b>=a:
    print("true")
a=8
b=12
if a!=b or b==a:
    print("true")
a=5
b=9
if not a<b:
    print("less")
a=5
b=9
if not a>b:
    print("less")
a=5
b=9
if not a<b and b>a:
    pr("less")
a=5
b=9
if not a<b or b>a:
    print("less")
a=int(input("enter value"))
b=int(input("enter value"))
if a<b and b>a:
    print("true")'''
#if condition usingidentity operation
#is is not
'''a=7
if type(a) is int:
    print("it is not")
a=9
if type(a) is not int:
    print("false")
a=int(input("a value"))
if type(a) is int:
    print("true")
a=int(input("a value"))
if type(a) is int:
    print("true")
a=float(input("a value"))
if type(a) is float:
    print("true")
a=input("a value")
if type(a) is str:
    print("true")'''
#if condition using membership operation
'''a=2,3,4,5,6,7,8,9,10
if 10 in a:
    print("true")
a=2,3,4,5,6,7,8,9,10
if 10 not in a:
    print("true")
a=2,3,4,5,6,7,8,9,10
if 20 not in a:
    print("true")
a=int(input("a value"))
if 30 in a:
    print("True")#error TypeError: argument of type 'int' is not a container or iterable
a=[1,2,3,4,5,6,7,8,9,10]
b=int(input())
if b in a:
    print("True")'''
# if else condition by using comparision operator
'''a=3
b=6
if a<b:
    print("true")
else:
    print("false")
a=3
b=6
if a>b:
    print("true")
else:
    print("false")
a=3
b=6
if a>=b:
    print("true")
else:
    print("false")
a=3
b=6
if a<=b:
    print("true")
else:
    print("false")
a=3
b=6
if a==b:
    print("true")
else:
    print("false")
a=3
b=6
if a!=b:
    print("less")
else:
    print("true")
a=3
b=6
if a>b and b>a:
    print("true")
else:
    print("false")
a=3
b=6
if a<=b and b>=a:
    print("true")
else:
    print("false")
a=3
b=6
if a==b and b!=a:
    print("true")
else:
    print("false")
a=3
b=6
if a<b or b>a:
    print("true")
else:
    print("false")
a=3
b=6
if a<=b or b>=a:
    print("true")
else:
    print("false")
a=3
b=6
if a==b or b!=a:
    print("true")
else:
    print("false")
a=[1,2,3,4,5,6,7,8,9,10]
b=int(input())
if b in a:
    print("true")
else:
    print("false")
a=[1,2,3,4,5,6,7,8,9,10]
b=int(input())
if b not in a:
    print("true")
else:
    print("false")'''
#if elif condition by using comparition
'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
a=2
b=4
if a==b:
    print("less")
elif b>a:
    print("greate")
elif a!=b:
    print("not equal")
#if-elif-else
a=5
b=10
if a>b:
    print("greate")
elif a!=b:
    print("not equal")
elif a==b:
    print(" equal")
else:
    print("true")
a=5
b=10
if a>b:
    print("greate")
elif a>=b:
    print("not equal")
elif a==b:
    print("equal")
else:
    print("true")
a=5
b=10
if a<b and b>a:
    print("greate")
elif a!=b or a==b:
    print("not equal")
else:
    print("true")
a=int(input())
if type(a) is int:
    print("it is int")
else:
    print("not int")'''
#multiple-if
'''a=9
b=11
if a>b:
    print("less")
if b>a:
    print("greate")
if a!=b:
    print("not equal")
if a==b:
    print("equal")'''
#nested-if
'''a=2
b=4
if a<b:
    print("less")
    if b>a:
        print("greate")
a=2
b=4
if a==b:
    print("less")
    if b>a:
        print("greater")
a=12
b=14
if a<b:
    print("less")
    if b<a:
        print("greate")
a=15
b=20
if a<b:
    print("less")
    if b<a:
        print("greate")
    else:
        print("true")
a=2
b=4
if a==b:
    print("less")
    if b>a:
        print("greater")
else:
    print("true")
a=2
b=4
if a<b:
    print("less")
    if b>a:
        print("greate")
    elif a!=b:
        print("not equal")'''






    

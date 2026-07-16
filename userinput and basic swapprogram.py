a=2
b=4
print(a+b)
print("-----------------------")
a=3
b=8
c=a+b
print(c)
print("-----------------------")
#print(10+10)
#ru_time_input()

a=int(input("enter the first value"))
b=int(input("enter the second value"))
print(a+b)
print("-----------------------")
a=float(input("enter the first value"))
b=float(input("enter the second value"))
print(a+b)

print("-----------------------")
a=complex(input("enter the first value"))
b=complex(input("enter the second value"))
print(a+b)
print("-----------------------")
a=str(input("enter the first name:"))
b=str(input("enter the second name:"))
print(a+b)
print("-----------------------")
a=input("enter the first name:")
b=input("enter the second name:")
print(a+" "+b)
print("-----------------------")
city=input("enter u r city")
print(city)
print("-----------------------")
a=bool(input("enter the a value"))
b=bool(input("enter the b value"))
c=bool(input("enter the c value"))
print(a+b+c)
print("-----------------------")
a=int(input())
b=int(input())
print(a+b)
print("-----------------------")
a=input()
print(a)
print("-----------------------")
a=int(input("a value"))
b=int(input("b value"))
option=int(input(choose the option
                      1.add
                      2.sub
                      3.mul))
print(a+b)
print(a-b)
print(a*b
print("-----------------------")
a=int(input("a value"))
b=int(input("b value"))
option=input("choose the option add sub mul")
print(a+b)
print(a-b)
print(a*b)

print("-----------------------")
print("1st method")#using simple variables
print("-----------------------")
a=int(input())
b=int(input())
a,b=b,a
print(a,b)#using temporary variable
print("-----------------------")
print("2nd method")
print("-----------------------")
a1=int(input())
a2=int(input())
temp=a1
a1=a2
a2=temp
print(a1,a2)
print("-----------------------")
print("3rd method")#using arthametic operator
print("-----------------------")
s=int(input())
t=int(input())
s=s+t
t=a-b
s=s-t
print(s,t)
print("-----------------------")
print("4th method")#using number formating
print("-----------------------")
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print("after swaping a=%d,b=%d" %(a,b))
print("after swaping a=%.2f,b=%.2f" %(a,b))
print("-----------------------")
print("5th method")#using xor
print("-----------------------")
a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print(a,b)
print("-----------------------")

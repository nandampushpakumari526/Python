#list comprehension
a=["python""java","dsa"]
#["PYTHON","JAVA","DSA"]
#print(a.upper())---error
b=str(a)
print(b.upper())
for i in a:
      print(i.upper(),end=" ")
a=[i.upper() for i in a]
print(a)

a=["codegnan","course","python"]
#a=[i.title() for i in a]
a=[i.capitalize() for i in a]
print(a)
a=[1,3,4,5,6,8,12,13]
#a=[i*i for i in a]
a=[i**2 for i in a]
a=[pow(i,2) for i in a]
print(a)
#evern number
a=[i for i in range(21) if i%2==0]
print(a)
#odd numbers
a=[i for i in range(21) if i%2!=0]
print(a)
#even numbers squares
a=[i*i for i in range(21) if i%2==0]
print(a)
a=["apple","banana","mango","dragon","kiwi","berry"]
a=[i for i in a if "a" in i]
a=[i for i in a if "a" not in i]
print(a)
a=[i*2 if i%2==0 else i*5 for i in range(16)]

print(a)
a=[1,2,3,4,5]
b=[5,4,3,2,1]
d=[a[i]+b[i] for i in range(len(a))]
d=[a[i]+b[i] for i in range(5)]
print(d)



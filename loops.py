#loops()
#for,while,range,break,continue,pass
#for loop()
'''a=[10,20,30,40,50,60]
for i in a:
    print(i)
a=[10,20,30,40,50,60]
for i in a:
    print(a)
a=[10,20,30,40,50,60]
for i in a:
    print(i,end=",")
a=[10,20,30,40,50,60]
for i in a:
    print(i)
print(type(a))
print(type(i))

b=(10,20,30,40,50,60)
for i in b:
    print(i)
print(type(b))
print(type(i))
a={3,4,5,6,7,8}
for i in a:
    print(i)
print(type(a))
print(type(i))
a={"name":"pushpa","city":"vja","state":"ap","year":2026}
for i in a:
    print(i)
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))
b="codegnan"
for i in b:
    print(i)
c=[5.6,7.8]
for i in c:
    print(i)
    print(type(a))
    print(type(i))
a=["python","java","dsa"]
#['PYTHON', 'JAVA', 'DSA']
for i in a:
    print(i.upper(),end=" ")

b=[]
for i in a:
    b.append(i.upper())
print(b)

a=["python","java","dsa"]
c=[]
for i in a:
    b=i.upper()
    c.append(b)
print(c)
#while loop()
a=10
while a<1:
    print(a)#empty
    
a=10
while a>1:
    print(a)
a=10
while a>1:
    print(a)
    a=a-1
a=20
while a>2:
    a=a-1
    print(a)

a=30
while a>5:
    print(a)
    a+=1
a=30
while a>5:
    print(a)
    a-=1
a=1
while a<30:
    print(a)
    a+=1
#voting
while True:
    age=int(input("enter the age"))
    if age>18:
        print("eligible for voting")
    else:
        print("not eligible for vot")
    
#range
#start-stop-step
for i in range(11):
    print(i)
print("---------------------------")
for i in range(5,20):
    print(i)
for i in range(1,10,1):
    print(i)

for i in range(0,19,2):
    print(i,end=",")
for i in range(5,46,5):
    print(i,end=",")
for i in range(3,30,3):
    print(i,end=",")


while(True):
    val=int(input("enter u r marks"))
    if val in range(91,101):
        print("Grades-A")
    elif val in range(81,91):
        print("Grades-B")
    elif val in range(71,81):
        print("Grades-C")
    elif val in range(50,71):
        print("Grades-D")
    else:
        print("Fail")
#break
a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break
a=20
while a>1:
    a=a-1
    if a==19:
        break
    print(a)
for i in range(25)
if i==9:
    break
print(i)

a="python"
for i in a:
    if i=="h":
        break
    print(i)
#continue
a=30
while a>5:
    print(a)
    a=a-1
    if a==15:
        continue
a=30
while a>5:
    a=a-1
    if a==15:
        continue
    print(a)
for i in range(15):
    if i==11:
        continue
    print(i)
a="python"
for i in a:
    if i=="h":
        continue
    print(i)
#pass
a=9
while a>2:
    print(a)
    a=a-1
    if a==7:
        pass'''
for i in range(25):
    if i==20:
        pass
    print(i)
    

        
    





    
    






    

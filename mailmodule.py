#import modules
#modules.greeting("pushpa")

#import modules
'''b=modules.d["idno"]
c=modules.d["names"]
print(b)
print(c)
import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,4))
print(math.log(2))
print(math.tan(45))
print(math.sin(60))
print(math.cos(30))
print(math.ceil(2.9))
print(math.ceil(3))
print(math.floor(2.7))
print(math.cbrt(2))
from math import pi,log,sqrt
print(pi)
print(log(10))
print(sqrt(2))'''
'''import sys
print(sys.path)
print(sys.version)'''
#os module
#import os
'''
print(os.path)
print(os.getcwd())
print(os.listdir())'''
'''
print(os.mkdir("oct16"))
print(os.listdir())'''
'''
print(os.chdir("C:\\Users\\lenovo\\Downloads"))
print(os.listdir())'''
#ASCII
'''print(chr(67))
print(chr(65))
print(chr(90))
print(che(93))
print(ord("a"))
print(ord("z"))
#print(ord(97))--->error
print(chr(97))'''
'''for i in range(97,123):
    print(chr(i),end=" ")
for i in range(65,91):
    print(chr(i),end=" ")'''
#write a program convert each character into ascii values
'''a=input()
for i in a:
    print(i,"-",ord(i))'''
#random module
#sample
'''import random
a=random.sample(range(10,50),10)
print(a)
#randint()
import random
a=random.randint(40,50)
print(a)
#choice()
import random
a=[10,40,50,70,80]
b=random.choice(a)
print(b)'''
#task
'''import random

a=random.randint(1,6)
print("roll of dice:",a)
while True:
    op=input("enter the yes or no")
    if op=="yes":
        print("roll of dice:",a)
        continue
    else:
        break'''
'''
import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    op=input("roll again?(y/n)")
    if op=="y":
        continue
    elif op=="n":
        break
    else:
        print("invalid")'''
#calendar
#import calendar
'''year=2026
month=12
print(calendar.month(year,month))'''
'''year=2004
print(calendar.calendar(year))'''
'''a=int(input("enter the year"))
b=int(input("enter the month"))
print(calendar.month(a,b))'''
#date and time
'''from datetime import date
a=date.today()
print(a)'''
'''import datetime
a=datetime.datetime.now()
print(a)'''
#epoch time
'''import time
a=time.time()
print(a)#epoch time
b=time.localtime(a)
print(b)
print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"today date is {b.tm_hour}-{b.tm_min}-{b.tm_sec}")
print(f"today date is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")   
 '''


'''import random,time
a=random.sample(range(1,11),10)
for i in a:
    c=time.sleep(2)
    print(i)

import random,time
for i in range(10):
    a=random.randint(20,40)
    print(a)
    time.sleep(2)'''




#regex(regular expressions)
'''a="codegnan is in vija"
print(a)
a="codegnan \nis\tin\nvja"
print(a)
#rstring
a=r"codegnan\nis\t\nvija"
print(a)
#compile(),search(),findall(),split(),sub
#sequence characters
\w ->it matches alphanumeric
\W ->it matches non-alpha numeric
\d ->it matches any digit
\D ->it matches non digit
\s ->it represents white spaces
\S ->it represents non-white spaces'''
#compile()
import re
#a="map maths cat code cash money mat cup cap monkey"
'''b=re.compile(r"m\w\w\w\w\w\w")#----->it desn't work bcz it not perform any operation
print(b)'''
#search()
'''c=b.search(a)
print(c)
b=re.search(r"m\w+",a)
print(b)'''
#findall()
'''c=re.findall(r"m\w+",a)
print(*c)'''

'''c=re.findall(r"c\w+",a)
print(*c)
#split()
d=re.split(r"m",a)
print(d)
e=re.split(r"\S",a)
print(e)
e=re.split(r"\s",a)
print(e)
#sub()
f=re.sub(r"m","a",a)
print(f)'''
a="1 p 3 4 5 6 s e"
b=re.findall(r"\d+",a)
print(*b)
b=re.findall(r"\D+",a)
print(*b)




    


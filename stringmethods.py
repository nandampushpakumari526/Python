Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#len
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
e="i am in vijawada"
len(e)
16
#count
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
a.count("k")
2
a.count(a)
1
a="pushpa","kumari"
a.count(a)
0
#find a string
a="python"
a[1]
'y'
a.find("h")
3
b="hello"
a.find("l")
-1
b.find("l")
2
b[2:4]
'll'
#escape sequences
#\n->new line
#\t->tap space
a="name:Pushpa\nlocation:mangalagiri\tkuporocolany\nclg:St marys"
print(a)
name:Pushpa
location:mangalagiri	kuporocolany
clg:St marys
a="name:Pushpa\nlocation:mangalagiri\tkuporocolany\nclg:St marys\nbranch:cse"
print(a)
name:Pushpa
location:mangalagiri	kuporocolany
clg:St marys
branch:cse
a="name:Pushpa\nlocation:mangalagiri\tkuporocolany\nclg:St marys\nbranch:cse"
print(a)
name:Pushpa
location:mangalagiri	kuporocolany
clg:St marys
branch:cse
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python"
b.replace("p","c")
'cython'
c="wait wait until you succeed"
c.replace("wait","work",1)
'work wait until you succeed'
#uppercase
a="python"
a.upper()
'PYTHON'
#lower
a="PYTHON"
a.lower()
'python'
c.lower("p")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    c.lower("p")
TypeError: str.lower() takes no arguments (1 given)
#capitalize
a.capitalize()
'Python'
a="i am full stack developer"
a.title()
'I Am Full Stack Developer'
a="code"
a.isupper()
False
a.islower()
True
a="Python"
a.isupper()
False
a.isdigit()
False
a.isalpha()
True
b="code course"
b.isalpha()
False
d=123
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="123"
d.isdigit()
True
a="pushpa@123"
a.isalnum()
False
b="pushpa@123"
a.isalnum()
False
c="pushpa.123"
a.isalnum()
False
a="data science"
a.startswit("d")
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.startswit("d")
AttributeError: 'str' object has no attribute 'startswit'. Did you mean: 'startswith'?
a.startswith("d")
True
a.endswith("e")
True
a.startswith()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.startswith()
TypeError: startswith expected at least 1 argument, got 0
#strip
#using to remove the white spaces
#lstrip()->remove the left space
#rstrip()->remove the right side spaces
a"         python            "
SyntaxError: invalid syntax
a="         python            "
a.strip()
'python'
a="      python"
a.lstrip()
'python'
a="python          "
a.rstrip()
'python'
#split()
a="i love python"
a.split()
['i', 'love', 'python']
#join
b="html","css","js","bs"
"".join(b)
'htmlcssjsbs'
","join(b)
SyntaxError: invalid syntax
",".join(b)
'html,css,js,bs'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
>>> print(a+b)
pythoncourse
>>> print(a+" "b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(a+" "+b)
python course
>>> a="python"
>>> b="course"
>>> print(a+" "+b)
python course
>>> firstname="pushpa"
>>> lastname="nandam"
>>> print(firstname+" "+lastname)
pushpa nandam
>>> print(firstname.title()+" "+lastname.title())
Pushpa Nandam
>>> print((firstname+" "+lastname).title())
Pushpa Nandam
>>> #formating
>>> 
>>> a=5
>>> b=2
>>> print(a+b)
7
>>> print("the sum of a, b is:",a+b)
the sum of a, b is: 7
>>> #format
>>> a="tom"
>>> b="cherry"
>>> print("Hello {} and Hello {}".format(a,b))
Hello tom and Hello cherry
>>> print("Hello {}\nHello {}".format(a,b))
Hello tom
Hello cherry
>>> #fstring
>>> a="sitha"
>>> b="ram"
>>> print(f"Hello {a}\nHello{b}")
Hello sitha
Helloram
>>> print(f"Hello {a} Hello{b}")
Hello sitha Helloram
>>> print(f"Hello {a} Hello {b}")
Hello sitha Hello ram
>>> print(f"Hello {a} {b}")
Hello sitha ram

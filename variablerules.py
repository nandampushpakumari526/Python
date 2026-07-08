Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=10
b=20
print(a+b)
30
a,b=10,20
print(a,b)
10 20
name="pushpa"
print(name)
pushpa
a=1,2,3,4,5,6,7,8,9
print(a)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
#pack
a,b,c=(10,20,30)
print(a,b,c)
10 20 30
a=(10,20,30)
print(a)
(10, 20, 30)
age=20
print(age)
20
print(Age)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(Age)
NameError: name 'Age' is not defined. Did you mean: 'age'?
AGE=20
print(AGE)
20
print(Age)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(Age)
NameError: name 'Age' is not defined. Did you mean: 'age'?
10=20
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
pushpa=20
>>> age="pushpa is"
>>> print(age+pushpa)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(age+pushpa)
TypeError: can only concatenate str (not "int") to str
>>> name=pushpa
>>> from=mangalagiri
SyntaxError: invalid syntax
>>> fro=mangalagiri
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    fro=mangalagiri
NameError: name 'mangalagiri' is not defined
>>> myloc="mangalagiri"
>>> print(name+myloc)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(name+myloc)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> name="pushpa
SyntaxError: unterminated string literal (detected at line 1)
>>> name="pushpa"
>>> myloc="mangalagiri"
>>> print(name+myloc)
pushpamangalagiri
>>> print(name+" "+myloc)
pushpa mangalagiri
>>> @=30
SyntaxError: invalid syntax
>>> %=20
SyntaxError: invalid syntax
>>> _=10
>>> print(_)
10
>>> if=20
SyntaxError: invalid syntax
>>> #unpacking
>>> #using for group of characters
>>> a=10
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined

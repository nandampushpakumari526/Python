Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arithmetic operator
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
print(a%b)
2
#assignment operator
a=2
b=6
a+=b
a
8
a-=b
a
2
a*=b
a
12
a//=b
a
2
a\=b
SyntaxError: unexpected character after line continuation character
a
2
a/=b
a
0.3333333333333333
a**=b
a
0.0013717421124828527
a%=b
a
0.0013717421124828527
#comparition operators
a<b
True
b<a
False
a>b
False
b>a
True
a<=b
True
a>=b
False
a!=b
True
a==b
False
2==2
True
a
0.0013717421124828527
b
6
#logical operators
a=2
b=4
bint(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    bint(a)
NameError: name 'bint' is not defined. Did you mean: 'bin'?
bin(a)
'0b10'
bin(b)
'0b100'
a!=b and a==b
False
a!=b or a==b
True
not True
False
#identify operator
a=1,2
b=1,2
a is b
False
a=1
type(a) is int
True
a="python"
type(a) is str
True
type(a) is not str
False
>>> a=2+3j
>>> type(a) is complex
True
>>> type(a) is not complex
False
>>> #membership operator
>>> s="python"
>>> "p" in s
True
>>> p in s
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    p in s
NameError: name 'p' is not defined
>>> "hon" is s
False
>>> "hon" in s
True
>>> a=1,2,3,4
>>> 3 in a
True
>>> 3 not in a
False
>>> #Bitwise operator
>>> a=2
>>> b=4
>>> a&b
0
>>> bin(a)
'0b10'
>>> bin(b)
'0b100'
>>> a|b
6
>>> a=2
>>> -(a+1)
-3
>>> ~a
-3

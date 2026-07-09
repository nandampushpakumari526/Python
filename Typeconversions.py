Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> int(1)
1
>>> int(23.33)
23
>>> int("python")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
>>> int(3+4j)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(3+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> float(1)
1.0
>>> float(2.3)
2.3
>>> float("python")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
>>> float(True)
1.0
>>> float(False)
0.0
>>> str(1)
'1'
>>> str(2.3)
'2.3'
>>> str("python")
'python'
>>> str(False)
'False'
>>> str(True)
'True'
>>> complex(2)
(2+0j)
>>> complex(2.3)
(2.3+0j)
complex("python")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
complex(False)
0j
complex(True)
(1+0j)
bool(2)
True
bool(2.4)
True
bool("python")
True
bool(3+4j)
True
str(3+5j)
'(3+5j)'
bool(True)
True
bool(False)
False

Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"pooja","year":2026,"month":7}
print(a)
{'name': 'pooja', 'year': 2026, 'month': 7}
print(type(a))
<class 'dict'>
print(a.keys())
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['pooja', 2026, 7])
a.items()
dict_items([('name', 'pooja'), ('year', 2026), ('month', 7)])
a={"year":2026,"month":"july","data":14}
a.update({"time":2})
a.update({"time":2},{"day":"true"})
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.update({"time":2},{"day":"true"})
TypeError: update expected at most 1 argument, got 2
a.update({"time":2,"day":"tue"})
a
{'year': 2026, 'month': 'july', 'data': 14, 'time': 2, 'day': 'tue'}
a={"name":"pooja","city":"vja"}
a.setdefault("mail","pushpa@gmail.com")
'pushpa@gmail.com'
a
{'name': 'pooja', 'city': 'vja', 'mail': 'pushpa@gmail.com'}
a={"state":"ap","country":"india"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("country")
'india'
a
{'state': 'ap'}
a.popitem()
('state', 'ap')
a
{}
a={colour:"black"}
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a={colour:"black"}
NameError: name 'colour' is not defined
a={"colour":"black","food":"biryani"}
>>> a.copy()
{'colour': 'black', 'food': 'biryani'}
>>> b=a.copy()
>>> b
{'colour': 'black', 'food': 'biryani'}
>>> len(a)
2
>>> a={"names":"pooja","city":"vija","name":"pooja"}
>>> print(a)
{'names': 'pooja', 'city': 'vija', 'name': 'pooja'}
>>> a={"names":"pooja","city":"vija","name":"pushpa"}
>>> a
{'names': 'pooja', 'city': 'vija', 'name': 'pushpa'}
>>> print(a)
{'names': 'pooja', 'city': 'vija', 'name': 'pushpa'}
>>> a={"name":"pooja","city":"vija","name":"pushpa"}
>>> print(a)
{'name': 'pushpa', 'city': 'vija'}
>>> a.count("name")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("city")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.index("city")
AttributeError: 'dict' object has no attribute 'index'
>>> a.clear()
>>> a
{}
>>> b={}
>>> b.update({"name":"pushpa"})
>>> b
{'name': 'pushpa'}
>>> a={"idno":[10,20,30],"names":["sai","sonu","suma"],"marks":[60,20,13,15]}
>>> print(a)
{'idno': [10, 20, 30], 'names': ['sai', 'sonu', 'suma'], 'marks': [60, 20, 13, 15]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idno', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['sai', 'sonu', 'suma'], [60, 20, 13, 15]])
>>> a.items()
dict_items([('idno', [10, 20, 30]), ('names', ['sai', 'sonu', 'suma']), ('marks', [60, 20, 13, 15])])

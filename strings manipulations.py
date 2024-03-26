Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

name = "YOUTUBE"
len(name)
7
name[0]
'Y'
name[6]
'E'
name[8]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    name[8]
IndexError: string index out of range
name[-1]
'E'
name[0:2]
'YO'
name[1:4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
name[1:4]
'OUT'
name[1:]
'OUTUBE'
name[:4]
'YOUT'
name[3:10]
'TUBE'
name[0:3]= 'my'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name[0:3]= 'my'
TypeError: 'str' object does not support item assignment
#strings are immutable
>>> "my" + name[3:]
'myTUBE'
>>> myname = "Navin Reddy'
SyntaxError: incomplete input
>>> myname= 'Linda Chi Code Lab'
>>> len(myname)
18
>>> #string concatenation
>>> string_1 = 'Hello'
>>> string 2 = 'World'
SyntaxError: invalid syntax
>>> string_2 = 'World'
>>> result = string_1 + string_2
>>> print(result)
HelloWorld
>>> sentence= "Python Programming"
>>> print(sentence.strip())
Python Programming
>>> name = "Linda"
>>> age = '33'
>>> print(f"my name is {name} and I am {age} years old)
...       
SyntaxError: incomplete input
>>> print(f"my name is {name} and I am {age} years old")
...       
my name is Linda and I am 33 years old

>>> print(sentence.lower())
...       
python programming
>>> print(sentence.upper())
...       
PYTHON PROGRAMMING
>>> print(sentence.replace("",""))
...       
Python Programming
>>> print(sentence.split())
...       
['Python', 'Programming']

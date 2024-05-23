Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:5:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range (100,1000)
...  
SyntaxError: unexpected indent
>>> for i in range (100,10000:
...                 
SyntaxError: invalid syntax
>>> for i in range(100, 1001):  
...     print(i)

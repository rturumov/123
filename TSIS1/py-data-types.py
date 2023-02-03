# Setting the Data Type

x = "Hello World" #str
#display x:
print(x)
#display the data type of x:
print(type(x))

x = 20 #int
print(x)
print(type(x))

x = 20.5 #float
print(x)
print(type(x))

x = 1j	#complex
print(x)
print(type(x))

x = ["apple", "banana", "cherry"]	#list
print(x)
print(type(x))

x = ("apple", "banana", "cherry")	#tuple
print(x)
print(type(x))

x = range(6)	#range
print(x)
print(type(x))

x = {"name" : "John", "age" : 36}	#dict
print(x)
print(type(x))

x = {"apple", "banana", "cherry"}	#set
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"})	#frozenset
print(x)
print(type(x))

x = True	#bool
print(x)
print(type(x))

x = b"Hello"	#bytes
print(x)
print(type(x))

x = bytearray(5)	#bytearray
print(x)
print(type(x))

x = memoryview(bytes(5))	#memoryview
print(x)
print(type(x))

x = None	#NoneType
print(x)
print(type(x))

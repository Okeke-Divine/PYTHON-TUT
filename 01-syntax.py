# Indentation
if 5 > 2:
    print("5 is greater than 2")


# variables
a = "Test"
b = 2
c = False
print(a, b, c)


# comment
"""
Multi-Line Comment
Line 2
Line 3
"""


# casting
x = float(3)
y = str("Mom")
print(x, y)


# variable type
print(type(x), type(y))

a, b, c = "Me", float(2), "they"
d = e = f = "Multiple"
print(a, b, c, d, e, f)


# Unpack a collection
fruits = ['apple', 'banna', 'cherry']
x, y, z = fruits
print(x, y, z)




#GLOBAL VARIABLES
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# //
print("=====================================")
# //

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#GLOBAL SCOPE
def myFun():
   global x
   x = "fantastic"

myFun()
print(x)
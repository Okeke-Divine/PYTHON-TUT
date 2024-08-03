a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("--------")

# //strings are arrays
print(a[2])


#lopping through a string
for x in a:
    print(x)

#string length
print(len(a))


#check a string
print("Lorem" in a)

#check not in
print("Python" not in a)


print("----------")


#slicing
b = " Hello World "
print(b[2:5])

#slice from start
print(b[:5])

#slice to end
print(b[2:])


#negative indexing
print(b[-5:-2])


print("UPPER:", b.upper())
print("LOWER:", b.lower())


#strip
print(b.strip())


#replace a string
c = "i hate python"
print(c.replace("hate","love").upper())

#split a string
print(c.split(" "))


#concatenate string
print(c + " // Example: print('" + b.strip() + "')")


#format
age = 36
city = "Awka"
school = "Unizik"
txt = "My name is Divine, and i'm {}. I live in {} and i attend {}"

print(txt.format(age,city,school))

print("-----")

#format (example 2)
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."

print(myorder.format(quantity,itemno,price))


#ESCAPE
txt = "We're the so called \"Viking\" from north Europe.\n\tNew Line"
print(txt)



print ("================STRING METHODS=================")
a="My New String"
print(a.capitalize())
print(a.casefold())
print(a.center(20,"-"))
print(a.lower().count("m"))

print(">>>ENCODE")

print(a.encode())
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


print(">>>JOIN")
mytuple = ("Python","JavaScript","Golang")
x = "-</>-".join(mytuple)
print(x)
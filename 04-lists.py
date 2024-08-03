mylist = ["apple", "banana", "cherry"]

mylist[0:2] = ['mango','grape','pineapple','guava','strawberry','banna']

if "apple" in mylist:
    print("Yes, 'apple' is in the fruits list")
else:
    print("Apple has been removed from this list")

if "mango" not in mylist:
    print("Mango is not in this list")
else:
    print("Mango is now in this list")

for x in mylist:
    print(x)

print(mylist)

for i in range(len(mylist)):
    print(mylist[i])

print(range(len(mylist)))

i=0
while i < len(mylist):
    print(mylist[i])
    i = i+1

[print(x) for x in mylist]


fruits_with_b = []
for x in mylist:
    if "b" in x:
        fruits_with_b.append(x)

print(fruits_with_b)


print([x for x in mylist if "a" in x])

print("============")
print(mylist,mylist.sort())

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x) # John#Peter#Vicky
print(type(x))  # string

# Dictionaries

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

# Joining a List of Strings

a = ['Hello', 'world', 'from', 'Python']
res = ' '.join(a)
print(res)

a = ['Hello', 'world', 'from', 'Python']
res = '.'.join(a)
print(res)
print(type(res))

# Using join() with set

s = {'Python', 'is', 'fun'}

# Separator "-" is used to join strings
res = '-'.join(s)
print(res)

#Note: Since sets are unordered, the resulting string may appear in any order, such as “fun is Python” or “Python is fun”.


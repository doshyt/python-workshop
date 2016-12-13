# -*- coding: utf-8 -*-
"""
Python basics

"""

print("Python is very flexible")

print("I'm a string")
a1 = "1"
print(a1)

print("I'm a number")
a2 = 1
print(a2)
print("If you compare whether they are equal, the answer would be")
a1 == a2

print("If you need to assign something, use =")
a1 = a2 = a3 = 4

print("If you need to compare something, use ==")
print(a2==4)

print("If you need to do something if the condition is satisified, use if")
print("If you need to do something when condition is NOT satisfied, add else")

if 5>4:
    print("5 is more then 4! True!")
else:
    print("This will never ever ever will be displayed!")    
print("And this will always be shown")

print("Python examines the code indentation to detect what belongs to IF or ELSE")

print("To repeat something many times, use loops")
for i in range(10):
    print(i)    

i = 0
condition = True
while condition == True:
    print(i)
    i = i + 1
    if i > 9:
        condition = False

print("Python is case-sensitive")
PrInT("This will give you an error")        

print("Python loves complex structures, like lists")
a = [1, 2, 3, 4]
print(a)
print("Python counts everything from zero")
print(a[1])
print(a[0])

print("Lists love loops")
for i in range(len(a)):
    a[i] = a[i] + 100
print(a)

print("Python sometimes is confusing")
b = [10, 20, 30, 40]
print(a+b)

c = []
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c)

print("What about list in a list?")
a = [1, 2, 3, [4, 5]]
print(a[0])
print(a[-1])

print("One thing about lists to remember - do not assign them directly")
a = [1, 2, 3, 4]
b = [2]
print("I'm the list a: ", a)
a = b
print("I'm the list a: ", a)
print("I'm the list b: ", b)
print("We are the SAME now")
b[0]=100000000000
print("I'm the list b: ", b)
print("I'm the list a: ", a)
print("Rly? a?")

print("Use .copy")
a = [1, 2, 3, 4]
b = [2]
a = b.copy()
print("I'm the list a: ", a)
b[0] = "Hey a, what about a change?" 
print("I'm the list a: ", a)

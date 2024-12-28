# import sys

# print(sys.api_version)

# arr = [1, 2, 3]

# a, b = arr[0], arr[1]
# c = None
# d = "None"
# print(a)
# print(b)
# print(c)
# print(d)

# print(a, b, c, d)

# print(str(a) + d)

# print("Hello", "world")

# local and Global variable

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# x = range(6)

# print(x[5])

# a = frozenset((1, 2, 3))

# x = set().union(a)

# x.add(4)

# print(x)

# from random import randrange

# print(randrange(1, 10))

# txt = "The best things in life are free!"
# free = "free"
# if free in txt:
#     print("Yes")

# name = "Arijit"
# age = 24.4555555

# text = f"Hi, I am {name}, I am {age : .2f} years old" # f String

# print(text)

# myList = list()

# myList.append(1)
# myList.append(2)

# print(myList[1])

# thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# print("apple" in thislist)

# newlist = [x for x in thisList if "a" in x]

# print(newlist)

# for x in thisList:
#     print(x)

# for i in range(len(thisList)):
#     print(thisList[i])

# i = 0
# while i < len(thisList):
#     print(thisList(i))

# newList = [x for x in range(10)]

# newList.sort(reverse = True)
# newList.reverse()

# print(newList)

# target = 50

# def close_to_number(number):
#     global target
#     return number - target


# list = [100, 50, 65, 82, 35]

# list.sort(key = close_to_number, reverse = True)

# print(list)

# case sensitive sort

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# case insensitive sort


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

'''
    ways to delete items from a list
'''

# thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# del thisList[0]
# thisList.remove("apple")
# thisList.pop(0)

# poping the last element

# thisList.pop()

# print(thisList)

# thisTuple = ("apple", "banana", "cherry")

# print(thisTuple.count("apple"))

# myList = ["apple", "banana", "cherry"]

# thisTuple = tuple(myList)

# myList = list(thisTuple)

# myList.append("water mellon")

# thisTuple = tuple(myList)

# print(thisTuple)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# add two sets

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# thisset.union(tropical)

# print(thisset)

# remove items from set

#remove raise error(Key Error) if the key is not present
# thisset.remove("abc")

#inseatd use discard as discard do not raise an Error if the key is not present

# thisset.discard("abc")

# thisset.union
# thisset.update
# thisset.difference
# thisset.difference_update
# thisset.symmetric_difference
# thisset.symmetric_difference_update
# thisset.intersection
# thisset.intersection_update
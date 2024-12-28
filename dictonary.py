thisDict = dict();

thisDict["name"] = "Arijit"
thisDict["date"] = 1999

# print(thisDict)
# print(thisDict.keys())
# thisDict["contact"] = "abc"
# print(thisDict.get("name"))
# print(thisDict.keys())
# print(thisDict.values())

# for x in thisDict.values():
#     print(x)

# for x in thisDict.items():
#     name, date = x
#     print(name, date)

a = 10
b = 20

# not correct
# a > b ? print(a) : print(b)

# correct
# print(a) if a > b else print(b)

def multivalueArgs(*args):
    print(args)

def keywordArgs(**kargs):
    print(kargs)

# keywordArgs(name = "Arijit", date = "1999")

# multivalueArgs("hello", 10999, 28)
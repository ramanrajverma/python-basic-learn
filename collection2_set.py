
"""Set = {}   unordered + immutable(add/remove OK) + NO  Duplicate"""


fruits = {"orange", "dragonfruit", "banana", "apple", "avacado", "orange"}
print(fruits)
"""print(dir(fruits))
print(help(fruits))
"""
print(len(fruits))  # To check the length of set
print("orange" in fruits)   #To check element present in set

# To Add element
fruits.add("pineapple")
print(fruits)

fruits.remove("orange")
print(fruits)

fruits.pop()
print(fruits)


"""fruits.clear()
print(fruits)"""
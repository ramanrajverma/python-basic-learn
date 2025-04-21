

"""TUPLE = ()  odered + unchangable + Duplicate Ok. Faster"""
#print(help(tuple))


fruits = ("orange", "apple","guava", "pineapple", "orange")
print(fruits)
print(fruits.index("apple"))
print(fruits.count("orange"))

# For iteration
for fruit in fruits:
    print(fruit)

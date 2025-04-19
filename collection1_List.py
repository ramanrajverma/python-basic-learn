"""Collections---
    List   = []
    Set    = {}
    Tuple  = ()
"""
"""----------------------------------------------------------------------------------------
List   = []   =======================> Ordered + Changable + duplicate OK
-----------------------------------------------------------------------------------------"""

fruits = ["apple", "orange", "guava", "pineapple", "banana"]
print(fruits)
print(fruits[0])   #can use index
print(fruits[::2])   #with step of 2. every second element

print(fruits[-1])
print(fruits[::-1])

#iteration
for x in fruits:
    print(x+"1", end=" ")
print()

#Methods can be used with collections -----
    #print(dir(fruits))  #lisiting of existing method
    #help(fruits)

#get the lenght of elements in a collection
print(f"number of elements: {len(fruits)}")
#To check elements exist
print("apple" in fruits)
print("Kiwi" in fruits)                                                                                                                                                                 

print("------------- Altering by Index -------------")
#Altering List by index
fruits[0] = "DragonFruit"
print(fruits)

print("------------ To Add element to the end of list --------------")
fruits.append("Avacado")
print(fruits)

print("-- to remove the element -----------")
fruits.remove("DragonFruit")

print("------------ To add at a given Index --------------")
fruits.insert(3, "magabana")


#-------------------------------------
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

"""fruits.clear()
print(fruits)"""

print(f"Index of Guava {fruits.index("guava")}")

fruits.append("orange")
print(fruits)

#To get count of specific element from a list
print(fruits.count("orange"))







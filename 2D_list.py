
# WAY 1  - to create 2D List

"""
fruits = ["orange", "mango", "apple","banana"]
foods = ["biryani", "paneer", "daal"]
bevrages = ["tea", "coffee", "lime water", "soda water"]

groceries = [fruits, foods, bevrages]"""



# WAY 2 to create 2D list
groceries = [["orange", "mango", "apple","banana"],
             ["biryani", "paneer", "daal"],
             ["tea", "coffee", "lime water", "soda water"]]

groceries1 = ({"orange", "mango", "apple","banana"},
              {"biryani", "paneer", "daal"},
              {"tea", "coffee", "lime water", "soda water"})


groceries2 = (("orange", "mango", "apple","banana"),
              ("biryani", "paneer", "daal"),
              ("tea", "coffee", "lime water", "soda water"))

print(groceries)


print(groceries[0])
print(groceries[1])
print(groceries[2])



print(groceries[1][0])
print(groceries[1][2])
#print(groceries[1][3])

print("------------------------  PRINT -1 -------------------------------")

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

print("------------------------  PRINT-2 -------------------------------")

for collection in groceries1:
    for food in collection:
        print(food, end=" ")
    print()

print("------------------------  PRINT-3 -------------------------------")

for collection in groceries2:
    for food in collection:
        print(food, end=" ")
    print()

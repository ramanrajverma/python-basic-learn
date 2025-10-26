
# dictionary  ---key-pair and no duplicate allowed

capitals = {"India": "Delhi",
            "Russia": "Moscow",
            "USA": "W DC"}
#print(dir(help))

# to the value from a Key

print(capitals)
print(capitals.get("India"))
print(capitals.get("India1"))



if capitals.get("India"):
    print("Capital exist")
else:
    print("Capital not exist")


# To Update dictionary
capitals.update({"Japan": "Tokyo"})  #To add New
capitals.update({"India": "Shimla"})  #Existing
capitals.update({"China": "Tibet"})  #Existing

print(capitals)
"""
#To remove
capitals.pop("China")
print(capitals)

#To remove the latest item inserted
capitals.popitem()
print(capitals)
"""

print("------------------  Keys  -------------------------")
keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)
print("-------------------------  Values ----------------")
for value in capitals.values():
    print(value)

print("-----------  items  -------------")
items = capitals.items();
print(items)

for key, value in capitals.items():
    print(f"{key}  --- {value}")
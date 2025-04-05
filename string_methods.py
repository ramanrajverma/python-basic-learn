#len()
#find()   #to get the first occurance
#rfind()  #to get the last occurance

name = input("Enter your full name: ")
result = len(name)
print(f"length of the name: {result}")

#
result_findspace = name.find(" ")
print(result_findspace)


result_last_occurance = name.rfind("v")
print(result_last_occurance)

#name = "raman"
print(name.upper())
print(name.lower())

#if didgit there ?
print(name.isdigit())
print(name.isalpha())
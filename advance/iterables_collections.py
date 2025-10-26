
#List  []
#Tuple ()
#Sets {}    # not revesible like list
#Strings
#Dictionary  {'key', 'value'}    #Like a set but a key value pair

########### list = []
numbers = [1,2,3,4,5,6, 'Hello']
for number in numbers:
    print(number, end=" ")
print()
#To print list in reversed orders
for number in reversed(numbers):
    print(number, end="\n")
print()

######### Tuple = ()
scores = (10,100,16, 23)
for score in scores:
    print(score, end=" ")
print()

######### Sets   {}
fruits  = {"apple", "mango", "banana", "kiwi"}
for fruit in  fruits:
    print(fruit, end=" ")
print()

#######string
name = "RamanRajVerma"
for n in name:
    print(n, end=" ")
print()


########dictionay  
my_test_dict = {"fruit": "apple", "Juice": "Mix-juice", "food": "Non-veg"}
for key in my_test_dict:
    print(key)
print()
print("--------dict-value-------")
for key in my_test_dict.values():
    print(key)
print("--- To get both ----")
for key, value  in my_test_dict.items():
    print(key, value)
    print(f"{key}={value}")

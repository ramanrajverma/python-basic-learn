import random

#print(help(random))

number = random.randint(1,6)
print(number)

low = 1
high = 100
num1 = random.randint(low, high)
print(num1)


options = ("rock", "paper", "sscissor")
choice = random.choice(options)
print(choice)

cards = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
random.shuffle(cards)
print(cards)

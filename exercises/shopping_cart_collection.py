
"""Collections---
    List   = []
    Set    = {}
    Tuple  = ()
"""
"""List   = []   =======================> Ordered + Changable + duplicate OK
Set = {}   unordered + immutable(add/remove OK) + NO  Duplicate
TUPLE = ()  odered + unchangable + Duplicate Ok. Faster"""

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() =="q":
        break;
    else:
       price = float(input(f"Enter the price of {food}: INR "))
       foods.append(food)
       prices.append(price)

print("------------------   YOUR  CART  --------------")
for food in foods:
    print(food, end=" ")

print()
print("----------  Total Price --------------")
for price in prices:
    total += price
print(f"Your total is: INR {total}")


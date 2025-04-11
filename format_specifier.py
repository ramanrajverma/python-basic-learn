

price1 = 3.1256
price2 = -345.456
price3 = 12.4345
print(f"Price 1 is ${price1: .2f}")  #print the result with from decimal to two places(f floating)
print(f"Price 2 is ${price2: .2f}")
print(f"Price 3 is ${price3: .1f}")

#To add the spces in o/p  or 10 space pased
print("To add the spaces in front of output")
print(f"Price 1 is ${price1:10}")  #print the result with from decimal to two places(f floating)
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")
      
#left justified
#To add the spces in o/p  or 10 space pased
print("Left justified output")
print(f"Price 1 is ${price1:<10}")  
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

#Right justified
#To add the spces in o/p  or 10 space pased
print("Right justified output")
print(f"Price 1 is ${price1:>10}")  
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

#Center alligned o/p
print("Center alligned output")
print(f"Price 1 is ${price1:^10}")  
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")
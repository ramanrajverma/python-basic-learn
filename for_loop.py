
for x in range(1, 5):
    print(x)

## way:1
print("---------  reversed loop------------")
for x in reversed(range(1, 5)):
    print(x) 

## way:2
for x in range(my_time, 0, -1):     ## ---------------------  IMP   --------------- Another way to loop backward
    #time.sleep(x)
    print(f"Time-Up; {x}")


print("------------  adding step ---------")
for x in range(1,10,2):   # 2 is the step here
    print(x)

print("--------------------  Iterating over a String -----------------")
credit_card_num = "1234-5678-9213-5643"
for x in credit_card_num:
    print(x)

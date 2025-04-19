import time

"""time.sleep(3)
print("Time Up!")"""

my_time = int(input("enter the time in seconds: ")) 
"""time.sleep(my_time)
print("Time Up!")"""

"""for x in range(0, my_time):
    time.sleep(1)
    print(f"Time Up {x}!")
print("Time Up!")"""


"""for x in reversed(range(0,3)):
    time.sleep(1)
    print(f"Time Up {x}!")"""


for x in range(my_time, 0, -1):     ## ---------------------  IMP   --------------- Another way to loop backward
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")   #02 is a format specifies
    time.sleep(x)
print(f"Time-Up")

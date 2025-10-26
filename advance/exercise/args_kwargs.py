
# Combining *args and **kwargs -------------   

"""def shipping_label(args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print("-------  Home Address ------")
    print()

    for key, val in kwargs.items():
        print(f"{key}: {val}")


shipping_label("Mr.", "Raman", "Raj", "Verma",
               village="Chamyar",
               PO="Tihra",
               Teh="Sarkaghat",
               Distt="Mandi",
               State="H.P")
"""

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print("-------  Home Address ------")
    print()
    
    print(f"{kwargs.get('village')}")  #one way to  do it
    print(f"{kwargs.get('village1')}") #If no value this ll give : none

    for key, val in kwargs.items():   #another way to do it
        print(f"{key}: {val}")

shipping_label("Mr.", "Raman", "Raj", "Verma",
               village="Chamyar",
               PO="Tihra",
               Teh="Sarkaghat",
               Distt="Mandi",
               State="H.P")
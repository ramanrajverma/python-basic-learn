username = input("Please enter the name: ")

# if len(username) <12 and username.isdigit():
#    print(username)


if len(username) > 12:
   print("Not a valid name")
elif not username.find(" ") == -1:
   print("Username with spaces")
elif not username.isalpha():
   print("Username with digits")
else:
   print(f"valid name: {username}")
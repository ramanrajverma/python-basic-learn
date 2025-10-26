#[First : end : step]
#First inclusive, and end exclusive

credit_number = "1234-5678-9834-3456"
#print(credit_number[5])

#print(credit_number[0:6])
#print(credit_number[:6])   // assuming automatic 0 - starting index

print(credit_number[5:9])
print(credit_number[15:])  #to get all from last

#get things from last of index
print(credit_number[-2])   #to get things from the last


#step 
#Begning with first character and then jump the step
print(credit_number[::2])
print(credit_number[::3])

#to get the last four digits of credit card number
print(credit_number[-4:])

#Reverse a string
newReverseCreditCardNumber = credit_number[::-1]
print(newReverseCreditCardNumber)
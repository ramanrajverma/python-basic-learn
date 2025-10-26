import random

lowest_num = 1
highest_num = 5
ans = random.randint(lowest_num, highest_num)
print(ans)
guesses = 0
is_running = True

print("-------- Python number guessing game --------")
print(f"Select number between {lowest_num} and {highest_num}")
while is_running:
    guess = input("Please enter the number: ")
    if guess.isdigit():
        guess = int(guess)
        if guess < lowest_num or guess > highest_num:
            print("Guess out of range")
        elif ans == guess:
            print("Correct guess")
            is_running = False
        else:
            print("Try again")
    else:
        print("Invalid input")
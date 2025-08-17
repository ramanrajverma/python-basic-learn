import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

#print(" # ● ┌ ─ ┐ │ └ ┘")

"┌─────┐"
"|     |"
"|  ●  |"
"|     |"
"└─────┘"

#creting dictionary with tuple
dice_art = {
    1: ("┌─────┐",
        "|     |",
        "|  ●  |",
        "|     |",
        "└─────┘"),
    2: ("┌─────┐",
        "|     |",
        "|  ●● |",
        "|     |",
        "└─────┘"),
    3: ("┌─────┐",
        "|     |",
        "| ●●● |",
        "|     |",
        "└─────┘"),
    4: ("┌─────┐",
        "| ●●  |",
        "| ●●  |",
        "|     |",
        "└─────┘"),
    5: ("┌─────┐",
        "| ●●  |",
        "| ●●● |",
        "|     |",
        "└─────┘"),
    6: ("┌─────┐",
        "| ●●  |",
        "| ●●  |",
        "| ●●  |",
        "└─────┘")
}

dice = []
total = 0
number_of_dice = int(input("How many dice?: "))

for die in range(number_of_dice):
    dice.append(random.randint(1,6))
print(dice)


"""
for die in range(number_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)"""

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()


for die in dice:
    total += die
print(f"total: {total}")

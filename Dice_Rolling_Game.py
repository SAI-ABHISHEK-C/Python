import random

while True:
    ans = input("Roll the Dice ? (y/n)")
    if ans.lower() == 'y':
        dice = random.randint(1, 6)
        print(dice)

    elif ans.lower() == 'n':
        print("Thank You for Playing")
        break

    else:
        print("Invalid Input")
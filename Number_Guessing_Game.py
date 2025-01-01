import random
count = 0
num = random.randint(1,100)

while True:
    try:
        count += 1
        say = input("Guess a number between 1 and 100: ")

        if int(say) > num:
            print("Too high")
        elif int(say) < num:
            print("Too low")
        else:
            print("U have guessed the number and it is ", num, " in ", count, "counts")
            break

    except ValueError:
        count -= 1
        print("Please enter a valid number between 1 and 100")


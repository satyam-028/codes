import random


while True:
    Computer = random.randrange(1, 101)
    n = int(input("Enter a any number : "))

    if n > Computer:
        print("Computer Number",Computer)
        print(f"Your guess {n} number is too high ")
    elif n < Computer:
        print("Computer Number",Computer)
        print(f"Your guess {n} number is too low ")
    elif n == Computer:
        print("Computer Number",Computer)
        print("Congratulation you guessed the number! ")
    else:
        print("Plz enter number in range ") 
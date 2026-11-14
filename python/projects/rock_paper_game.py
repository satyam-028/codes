import random

l = ["rock", "paper", "scissor"]

print("Welcome in game!!!\n")
print("rock paper scissor Game Start... \nchoice option to continue game ")

print("1. play yes")
print("2. Exit\n")


while True:
    
    choice = input("Enter your choice to continue game (1 to 2) : ")

    if choice == "1":
        for i in range(1, 6):
            user = int(input("1. Rock\n2. paper\n3. scissor"))
            if user == 1:
                uchoice = "rock"
            elif user == 2:
                uchoice = "paper"
            elif user == 3:
                uchoice = "scissor"
         
            Cchoice = random.choice(l)
            
            if choice == uchoice:
                print("Computer Value : ", Cchoice)
                print("User Value : ", uchoice)
                print("Game draw")


            elif(uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock")  or (uchoice == "scissor" and Cchoice == "paper"):
                print("Computer Value : ", Cchoice)
                print("User Value :", uchoice)
                print("You win the game!!!")
            
            else:
                print("Computer Value ", Cchoice)
                print("User Value ", uchoice)
                print("Computer win the game!!!")
    

    elif choice == "2":
        print("Game over!!!")
        break


        # Game Rules:


        # Snake drinks Water → 🐍 wins

        # Water douses Gun → 💧 wins

        # Gun kills Snake → 🔫 wins


import random

def game():

    
    print("Welcome to the Snake, Water or Gun game!")

    print("Choose one from Snake, Water, or Gun ")
    
    print("The first one to score 2 will win the game")

    print("Let's start!")

    Choices = ["Snake", "Water", "Gun"]

    user_score = 0
    computer_score = 0
    Round_num = 1

    while user_score<2 and computer_score<2:
        print(f"--- Round{Round_num} ---")

        user = input(f"Your Choice: ").capitalize().strip()
        if user not in Choices:
            print("Invalid input")

            continue

        computer = random.choice(Choices)

        print("Computer choose:", computer)

        if user == computer:
            print("it's a draw")

            print(f"Your score is {user_score} and the computer score is {computer_score}")
            
            Round_num+=1

        elif (user =="Snake" and computer == "Water") or \
            (user == "Water" and computer == "Gun") or \
            (user == "Gun" and computer == "Snake"):

            print("You win this round")

            Round_num+=1
            user_score+=1

            print(f"Your score is {user_score} and the computer score is {computer_score}")

        else: 
            print ("Computer wins this round")
            
            Round_num+=1
            computer_score+=1

            print(f"Your score is {user_score} and the computer score is {computer_score}")

    if user_score == 2:
        print("Congractulations! You won!")
    else:
        print("Opps! You Lost!")


    again = ("Would you like to play again: Yes/No")

    print(again)

    again_choices = ("Yes", "No")

    Replay = input("Choose Yes or No: ").capitalize()

    if Replay not in again_choices:
        print("invalid input")

    elif Replay == "Yes":
        game()

    else: 
        print("Thanks for playing")


game()


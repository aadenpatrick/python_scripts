import random

def play_game():
    choice = input("pick one: rock, paper or scissors: ")
    derp = random.randint(1, 3)
    if derp == 1 and choice == "paper":
        print("computer chose rock and you chose paper, you win!")
    elif derp == 2 and choice == "paper":
        print("computer chose scissors and you chose paper, you lose!")
    elif derp == 3 and choice == "paper":
        print("computer chose paper and you chose paper, it's a tie!")
    elif derp == 1 and choice == "rock":
        print("you chose rock and computer chose rock, it's a tie!")
    elif derp == 2 and choice == "rock":
        print("you chose rock and computer chose scissors, you win!")
    elif derp == 3 and choice == "rock":
        print("you chose rock and computer chose paper, you lose!")
    elif derp == 1 and choice == "scissors":
        print("computer chose rock and you chose scissors, you lose!")
    elif derp == 2 and choice == "scissors":
        print("computer chose scissors and you chose scissors, it's a tie!")
    elif derp == 3 and choice == "scissors":
        print("computer chose paper and you chose scissors, you win!")
    elif not choice == "scissors" or choice == "paper" or choice == "rock":
        print("i didn't understand your choice, try again")
        play_game()
    elif choice == "scissors" or choice == "paper" or choice == "rock":
        exit()       
    
yn = input("would you like the play a game of rock paper scissors?(yes/no)")
if yn == "yes":
    play_game()
else:
    print(":(")
        

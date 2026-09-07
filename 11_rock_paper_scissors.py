import random

options = ("rock", "paper", "scissors")

score = {"player": 0, "computer": 0}

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
        score["player"] += 1
        score["computer"] += 1
    elif (player == "rock" and computer == "scissors"):
        print("You win!")
        score["player"] += 1
    elif (player == "paper" and computer == "rock"):
        print("You win!")
        score["player"] += 1
    elif (player == "scissors" and computer == "paper"):
        print("You win!")
        score["player"] += 1
    else:
        print("You lose!")
        score["computer"] += 1

    # play_again = input("Do you want to play again? (y/n): ").lower()
    # if play_again != "y":
    #     running = False

    if not input("Do you want to play again? (y/n): ").lower().startswith('y'):
        running = False

print("Thanks for playing!")
print(f"Final Score - Player: {score['player']}, Computer: {score['computer']}")
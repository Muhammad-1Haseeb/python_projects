import random
from wordslist import words


# Dictionary of key: ASCII art stages
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("Answer: " + " ".join(answer))

def get_valid_guess(guessed_letters):
    """Loop until user enters a valid single letter."""
    while True:
        guess = input("Guess a letter: ").lower().strip()
        
        if len(guess) != 1:
            print("⚠️ Please enter exactly one letter.")
            continue
        
        if not guess.isalpha():
            print("⚠️ Please enter a letter (A-Z).")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try again.")
            continue
            
        return guess

def play_game():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    max_wrong = len(hangman_art) - 1
    
    print(f"\n🎮 New Game! The word has {len(answer)} letters.")
    print(f"💡 You can guess up to {max_wrong} wrong times.")

    while True:
        display_man(wrong_guesses)
        display_hint(hint)
        
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in answer:
            print(f"✅ Correct! '{guess}' is in the word.")
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            print(f"❌ Wrong! '{guess}' is not in the word.")
            wrong_guesses += 1

        # Check Win Condition
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("🎉 You WIN! 🎉")
            return True
        
        # Check Loss Condition
        if wrong_guesses >= max_wrong:
            display_man(wrong_guesses)
            display_answer(answer)
            print("💀 You LOSE! 💀")
            return False

def main():
    is_running = True
    while is_running:
        play_game()
        
        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again != 'y':
            is_running = False
            print("Thanks for playing! Goodbye!")
        else:
            print("\n" * 2) # Clear screen visually

if __name__ == "__main__":
    main()
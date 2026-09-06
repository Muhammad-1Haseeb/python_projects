questions = ("How many elements are in peridoic table?: ", 
             "What animal lays the largest eggs?: ", 
             "What is the most abundant gas in Earth's atmosphere?: ", 
             "How many bones are in the human body?: ", 
             "Which planet in the solar system is the hottest?: ")

options = (("A. 118", "B. 119", "C. 120", "D. 121"),
           ("A. Ostrich", "B. Whale", "C. Crocodile", "D. Snake"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 205", "C. 201", "D. 208"),
           ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter"))

answers = ("A", "A", "B", "A", "B")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("-------------------------")
print("Results")
print("-------------------------")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

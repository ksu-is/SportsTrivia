# Tyler George's Final project
def ask_question(question, options, correct_answer):
    print("\n" + question)
    for option in options:
        print(option)

    answer = input("Enter your answer (A, B, C, D): ").upper()

    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
def save_score(name, score):
    file = open("scores.txt", "a")
    file.write(f"{name},{score}\n")
    file.close()

def show_high_score():
    try:
        file = open("scores.txt", "r")
        high_score = 0
        top_player = ""

        for line in file:
            line = line.strip()
            if line == "":
                continue

            data = line.split(",")

            if len(data) < 2:
                continue

            try:
                score = int(data[1])
            except:
                continue

            if score > high_score:
                high_score = score
                top_player = data[0]

        file.close()

        if top_player != "":
            print(f"\nHigh Score: {top_player} with {high_score}")
        else:
            print("No scores yet.")

    except:
        print("No scores yet.")
        
def main():
    print("Welcome to the Ultimate Sports Quiz!")
    name = input("Enter your name: ")

    score = 0

    score += ask_question(
        "1. How many players are on a basketball team on the court?",
        ["A. 3", "B. 5", "C. 7", "D. 9"],
        "B"
    )

    score += ask_question(
        "2. Which NFL team won Super Bowl LVII?",
        ["A. Chiefs", "B. Eagles", "C. Rams", "D. Patriots"],
        "A"
    )

    score += ask_question(
        "3. What sport is known as 'the beautiful game'?",
        ["A. Basketball", "B. Baseball", "C. Soccer", "D. Tennis"],
        "C"
    )

    score += ask_question(
        "4. How many points is a touchdown worth?",
        ["A. 3", "B. 6", "C. 7", "D. 2"],
        "B"
    )

    score += ask_question(
        "5. Which player is known as 'King James'?",
        ["A. Kobe Bryant", "B. Michael Jordan", "C. LeBron James", "D. Steph Curry"],
        "C"
    )

    print(f"\n{name}, your final score is: {score}/5")

    save_score(name, score)
    show_high_score()

    replay = input("\nPlay again? (yes/no): ").lower()
    if replay == "yes":
        main()
    else:
        print("Thanks for playing!")


main()

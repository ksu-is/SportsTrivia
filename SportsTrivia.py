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
            data = line.strip().split(",")
            score = int(data[1])

            if score > high_score:
                high_score = score
                top_player = data[0]

        file.close()

        if top_player != "":
            print(f"\nHigh Score: {top_player} with {high_score}")
    except:
        print("No scores yet.")


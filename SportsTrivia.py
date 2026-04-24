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

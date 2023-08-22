def quest_disp(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")
    print()

def users_choice(num_options):
    while True:
        try:
            choice = int(input("Enter the number of your answer: "))
            if 1 <= choice <= num_options:
                return choice
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question_data in questions:
        quest_disp(question_data)
        user_choice = users_choice(len(question_data["options"]))

        if user_choice == question_data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")

    print(f"You scored {score} out of {total_questions} questions.")
    x=(score/5)*100
    print(f"You got {str(x)}%")

if __name__ == "__main__":
    quiz_questions = [
        {
            "question": "What is the capital of Japan?",
            "options": ["Beijing", "Seoul", "Tokyo"],
            "answer": 3
        },
        {
            "question": "Which country is known as the 'Land of the Rising Sun'?",
            "options": ["China", "Japan", "Korea"],
            "answer": 2
        },
        {
            "question": "What is the largest ocean in the world?",
            "options": ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean"],
            "answer": 3
        },
        {
            "question": "What is the symbol for the chemical element 'Gold'?",
            "options": ["Go", "Au", "Gd"],
            "answer": 2
        },
        {
            "question": "Who painted the 'Mona Lisa'?",
            "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso"],
            "answer": 2
        },
    ]

    print("Welcome to the Quiz Game!")
    play_quiz(quiz_questions)
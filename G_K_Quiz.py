data = [
    {
        "question":"What is the biggest planet in the solar system?",
        "options":"[A] Earth [B] Jupiter [C] Mars [D] Venus",
        "answer":"[B]"
    },
    {
        "question":"Who painted Mona Lisa?",
        "options":"[A] Vincent Van Gogh [B] Pablo Picasso [C] Leonardo da Vinci [D] Michelangelo",
        "answer":"[C]"
    },
     {
         "question": "Which gas do plants absorb during photosynthesis?",
        "options": "[A] Oxygen [B] Carbon Dioxide [C] Nitrogen [D] Hydrogen",
        "answer": "[B]"
        },
    {
        "question": "What is the capital city of Japan?",
        "options": "[A] Beijing [B] Tokyo [C] Seoul [D] Kyoto",
        "answer": "[B]"
        },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": "[A] Oxygen [B] Osmium [C] Ozone [D] Oxide",
        "answer": "[A]"
        },
    {
        "question": "In computing, what does 'CPU' stand for?",
        "options": "[A] Central Processing Unit [B] Computer Power Utility [C] Central Program Unit [D] Control Processing Unit",
        "answer": "[A]"
        },
    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "options": "[A] China  [B] Japan [C] Thailand [D] South Korea",
        "answer": "[B]"
        },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": "[A] William Shakespeare [B] Charles Dickens [C] Mark Twain [D] Jane Austen",
        "answer": "[A]"
        },
    {
        "question": "What is the boiling point of water at sea level?",
        "options": "[A] 90°C [B] 95°C [C] 100°C [D] 110°C",
        "answer": "[C]"
        },
    {
        "question": "Which ocean is the largest on Earth?",
        "options": "[A] Atlantic Ocean [B] Indian Ocean [C] Pacific Ocean [D] Arctic Ocean",
        "answer": "[C]"
        }
]

score = 0

print("A General knowledge Quiz")
in1 = input("Press [1] to start: ")

if in1 != '1':
    print("Goodbye")
else:
    # Loop through each question dictionary in the 'data' list
    for q in data:
        print("\n" + "-"*30) # Separator for readability
        print(q["question"]) # Print the question
        print(q["options"])  # Print the options (The original code had an error here: 'data["options"]')

        # Get the user's answer and convert it to uppercase for consistent comparison
        in2 = input("Enter your answer (e.g., A, B, C, or D): ").upper()

        # Check if the user's answer matches the 'answer' value in the current dictionary
        # We compare the input (e.g., 'B') to the answer format (e.g., '[B]').
        if f"[{in2}]" == q["answer"]:
            print("✅ Correct Answer!")
            score += 1 # Increment score only on a correct answer
        else:
            # Extract the correct answer choice letter for the feedback
            correct_choice = q["answer"].strip('[]')
            print(f"❌ Wrong Answer. The correct answer was {correct_choice}.")

    print("\n" + "="*30)
    print(f"Quiz finished!")
    print(f"Your final score is {score}/{len(data)}")
    print("="*30)
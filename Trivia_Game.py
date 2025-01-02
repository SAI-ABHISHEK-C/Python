import random

# Take a set of questions in a dictionary

questions_main_list = {"Extension of Python file?": "py",
    "Keyword to define function?": "def",
    "Keyword for class definition?": "class",
    "Keyword to import module?": "import",
    "Keyword to handle exceptions?": "try",
    "Keyword to exit loop early?": "break",
    "Keyword to skip iteration?": "continue",
    "Keyword for empty block?": "pass",
    "Data type for sequence?": "list",
    "Immutable sequence type?": "tuple",
    "Unordered unique collection?": "set",
    "Key-value collection type?": "dict",
    "To get length of list?": "len",
    "Convert string to integer?": "int",
    "Keyword for inheritance?": "super",
    "Operator for exponentiation?": "**",
    "Method to add item in list?": "append",
    "Method to remove item from list?": "remove",
    "Function to display output?": "print"}

# Select the random 5 questions which needs to be displayed to the user Like this --> (1. When was python invented ?)
questions_list = list(questions_main_list.keys())
questions = random.sample(questions_list,5)

score = 0

for idx,question in enumerate(questions):
    print(f"{idx + 1}. {question}\n")
    ans = input("Your Answer: ").lower().strip()
    correct_answer = questions_main_list[question]

    if ans == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is",correct_answer)

print(f"Your Final Score is {score}/5")

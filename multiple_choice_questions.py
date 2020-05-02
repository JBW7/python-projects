questions_list = [
    "1. Whats 11 to the power of 4?\n(a) 14641\n(b) 1331\n(c) 1221\n(d) 1431\n\n",
    "2. Whats 7 to the power of 3?\n(a) 243\n(b) 392\n(c) 343\n(d) 341\n\n",
    "3. Whats 391038 to the power of 0?\n(a) 391038\n(b) 0\n(c) 782930\n(d) 1\n\n"
]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(questions_list[0], "b"),
    Question(questions_list[1], "c"),
    Question(questions_list[2], "d"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You Scored " + str(score) + " Out Of " + str(len(questions)))


run_test(questions)
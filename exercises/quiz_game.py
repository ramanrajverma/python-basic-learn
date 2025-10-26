
questions = ("Which is the easiest Programming language?",
             "Which language is best for memory management?",
             "Which language is won by Microsoft?",
             "Which is the best UI framework?")


options = (("A. Python","B. Ruby","C. C#","D. Java"),
           ("A. Go","B. Rust","C. C","D. C++"),
           ("A. Java","B. JS","C. Python","D. C#"),
           ("A. Angular","B. HTML","C. React","D. CSS"))


answers =  ("A","C","D","C")
guesses = []
score = 0
question_num = 0

#way1
"""for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)  
    user_quess = input("Enter your choice: ").upper()
    for answer in answers[question_num]:
        if answer == user_quess:
            score +=1
            print("----- CORRECT -------")
        else:
            print("-------- INCORRECT  -------")
        break
    question_num +=1

print(f"--------  Your to total score: {score}")"""

#way2
for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)  
    user_quess = input("Enter your choice(A, B, C, D): ").upper()
    guesses.append(user_quess)
    for answer in answers[question_num]:
        if answer == user_quess:
            score +=1
            print("----- CORRECT -------")
        else:
            print("-------- INCORRECT  -------")
        break
    question_num +=1

print(f"--------  Your to total score: {score}")
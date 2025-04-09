quiz = [
    {
        "question":"how many bits are in one byte?",
        "options":["A.10","B.8","C.6","D.4"],
        "answer":"B"
    },
    {
        "question":"A collection of items is referred to as:",
        "options":["A.list","B.dictionary","C.variable","D.turple"],
        "answer":"A"
    },
    {
        "question":"Which component is considered as the brain of the computer?",
        "options":["A.RAM","B.CMOS","C.CPU","D.Motherboard"],
        "answer":"C"
    },
    {
        "question":"which of the following is not a datatype?",
        "options":["A.Numeric","B.String","C.Boolean","D.Logical"],
        "answer":"D"
    },
    {
        "question":"What is the importance of the 'f'string?",
        "options":["A.To improve readability and less code","B.to store values.","C.To skip to the next line","D.To make operations on values"],
        "answer":"B"
    }  

]
score = 0
correct = 0
wrong = 0
for question in quiz:
    print(question['question'])
    for option in question["options"]:
        print(option)

    answer = input("please select option: ") 

    if answer ==question["answer"]:
        print("correct")
        correct += 1
        score +=5
    else:
        wrong += 1
        print(f"Wrong\ncorrect Answer is {question["answer"]}") 
print(f"\nscore :{score}")           
print(f"CORRET ANSWER :{correct}\n WRONG ANSWER:{wrong}")

     

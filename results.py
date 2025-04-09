# aprogram to compute the average and total of the students
students = ["TWAHA" ,"SAM" ,"JACKSON" , "DERICK"]
for student in students:
    print(student)
    math_score    = int(input("ENTER MATH SCORE:"))
    science_score = int(input("ENTER SCIENCE SCORE:"))
    islam_score   = int(input("ENTER ISLAM SCORE:"))
    cre_score     = int(input("ENTER CRE SCORE: "))
    total = math_score + science_score + islam_score + cre_score 
    average = total/4
    
    print(f"TOTAL MARK: {total}\nAVERAGE MARK: {average}\n")

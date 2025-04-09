# HOW Many have passed and how many have failed , passing is determined by 50 average
students =["TWAHA" , "VANY", "JACK", "SAM", ]
subjects =["Eng","Maths","Sci","Arts"]

class_average = 0
for student in students:
    print(student)
    total =0
    for subject in subjects:
        score = int(input(f"\t{subject}:")) 
        total += score
        
    average = total/4
    class_average += total/4
    print(f"{student}'s TOTAL:{total}\n&\nAVERAGE: {average}")
print(f"class_average: {class_average}")


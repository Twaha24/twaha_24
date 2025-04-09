#a program to ask the usr enter the student names
student_names = input("ENTER STUDENT NAMES: ")
cap = (student_names.index(" "))
print(f"{student_names.upper()[:cap]}")
#score in english, math,science,and arts 
#english
english = int(input("enter english score: "))
#math score
math = int(input("enter math score: "))
#arts acorea
arts  = int(input("enter arts score: "))
#science score
science = int(input("enter science  score: "))
#getting the total score of ALL sublects
total_score = english + math + arts + science
print(f"total csore:  {total_score}")
average_score = total_score/4
print(f"average score: {average_score}")
totalmark = 400
percentage_score = total_score/totalmark*100
print(f"percentage score: {percentage_score}")








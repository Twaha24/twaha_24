scores = []

def add_score(score):
    if score > 0:
        scores.append(score)
    else:
        print('''we expect numbers above zero "0"''') 

    return None

def list_score(scores):
    for score in scores:
        print(score)

    return None


def sum_list_score(score,total):
    for score in scores:
       total += score
    return total

def largest_number(scores):
    largest_number = 0
    for score in scores:
        if score > largest_number:
            largest_number = score
    return largest_number        

    #scores.sort()
    #scores.reverse()
    #highest_score = scores[0]
    #return highest_score
    
#no_of_times = 5
#for value in range(no_of_times):
    #user = int(input("Enter score: "))
    #add_score(user)

while True:
    score = input("Enter score or Q to quit: ")
    if score.upper() == "Q":
        break
    add_score(int(score))



# we add a function to sum up the values in scores list
# determine the largest number in the scores list
list_score(scores)
total = 0
print(scores)

print(f"Total Score:{sum_list_score(score,total)}")

print(f"Highest number:{largest_number(scores)}")
 




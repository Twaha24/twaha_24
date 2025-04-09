games =["NETWORK","CODING","REPAIR","QUIZ"]
groups  = ["CYBER","SYNTAX","CODERS",]

group_scores = []

for group in groups:
    games_scores = []
    print(f"\n\t\t{group}")
    for game in games:
        games_score =  int(input(f"\t\tENTER GAME SCORE {game}:  "))
        games_scores.append(games_score)

    group_scores.append(games_scores)
 
    for group_score in group_scores:
        total = 0
        for score in group_score:
            total += score
    print(f"TOTAL {group} :{total}")    

print(f"\n\tGROUP \tNETWORK\tCODING\tREPAIR\tQUIZ")
index = 0
for game in games_scores:
    output = "\t\t"
    for score in game:       
      output += f"\t\t{games_scores}"

    print(output)  

    

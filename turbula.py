activities = ["Quran","Poem","Quiz","News"]
no_of_schools = 5
school_names =[]
gamesscores = []
for school in range(no_of_schools):
    schoolname = input("ENTER SCHOOL NAME: ")
    school_names.append(schoolname)
    game_scores = []
    for activity in activities:
        gamescore = int(input(f"Enter {activity} Score: "))
        game_scores.append(gamescore)
    gamesscores.append(game_scores)

print("\t\t\t*THE 2019 IMSAK ANNUAL COMPETIIONS*\n\t\t\t      SUMMARISED RESULTS SCHEMME")       
print("\tName\t Quran\t Poem\t Quiz\t News \ttotal\t Average")
index = 0
for game in gamesscores:
    output = f"\t{school_names[index]}\t"
    for score in game:
        output += f"  {score}\t"
    index += 1
    print(f"{output}")         

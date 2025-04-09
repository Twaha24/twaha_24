print("\u2764")  # ❤")
name = input("ENTER YOUR NAME: ")


age = 18
age = input("ENTER YOUR AGE: ")
gender = input("ENTER YOUR  GENDER: ")
nationality = input("ENTER YOUR NATIONALITY: ")

if int(age) >= 18:  
    print("your an adult")
elif int(age) >=13:
    print("oli mwaana muto nyo sebo")  
else:
    print("todawano kubanga toyina mpisa") 



names = ['twaha',"juma","joan","jona"]

if "name" in names:
    print("name is among the provided names")
else:
    print("tetumumanyi wade ,tetumulabangako")

nationality = ['ugandan',"kenya","america","tanzania"]

if "nationality" in nationality:
    print(f"we have comfirmed that u really belong to {nationality}")
else:
    print("your among the criminals")    
# aprogram to ask the user enter the employee name  print("\u2764")  # ❤
AVERAGE_HOURS = 50
ABOVE_AVERAGE = 30000
BELOW_AVERAGE = 25000
employee_name = input("ENTER YOUR NAME: ")

# Checking for hours worked
hours_worked = int(input("ENTER HOURS WORKED: "))

#a program should display "above average" if the hours worked 50 and above otherwise "below average"
 #a program should compute the wage at a rate of 30000 if the hours-worked is 50 and above 
 # otherwise the rate is 25000

      
if hours_worked >AVERAGE_HOURS:
    print("above average 😄")
    wage = ABOVE_AVERAGE * hours_worked
else:
     print("Wow, below average! 😲")
     wage = BELOW_AVERAGE * hours_worked
    
print(f"WAGE: {wage}")   

      

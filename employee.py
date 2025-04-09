#a program to ask the user the employee name, gender and hours worked
#a program the computes the wage as the product of hours worked and the fixed rate of 40000
#also computes the aloowance as 105 of the wage, crosswage 
#  which is the sumation of wage and alolowance ,tax which is 5% of the cross wage and netwage which is the difference between
# the program should then output all the required details 

employee_name = input("ENTER YOUR NAME: ")
gender = input("ENTER GENDER: ")
hours_worked = input("ENTER HOURS WORKED: ")
fixed_rate = int(40000)

wage = int(hours_worked) * fixed_rate              
allowance = (10/100) * wage
gross_wage = wage + allowance 
tax = (5/100) * gross_wage
net_wage = gross_wage - tax

print(f"wage: {wage}shs \nAllowance: {allowance}shs\nGross wage: {gross_wage}shs\nTax:{tax}shs\nNetwage:{net_wage}shs\n THANK YOU" )

def compute_wage(hours,rate):
    wage = hours * rate
    return wage

def compute_allowance(wage,allowance_rate):
    allowance = wage * allowance_rate
    return
hours = int(input("Enter hours_worked:" ))
rate = int(input("Enter rate: "))

def compute_gross_wage(wage,allowance):

    gross_wage = wage + allowance
    
    return gross_wage

def compute_tax(tax_rate,wage):

    tax  = tax_rate * wage
    return tax

def net_wage(wage,tax):

    net_wage = wage - tax
    return net_wage

print(f"wage:{compute_wage(hours,rate)}\n Allowance:")

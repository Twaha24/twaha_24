#in a supermaarket  acustomer can peak upto five items, write a program to capture the items taken, quantity 
# and price. the program should compute the amount of each item and the total bill of all items 
# discount of 10% if total bill is 50000 and above
counter = 1
total_bill = 0
discount = 0
net_pay = 0
while counter <=5:
    item_taken = input(f"ENTER ITEM {counter}: ")
    if item_taken == "q":
    quantity   = int(input("ENTER QUANTITY: "))
    price      = int(input(" ENTER PRICE: "))
    amount = price * quantity
    total_bill = total_bill + amount
    if total_bill >= 50000:
        discount = (10/100) * total_bill
        net_pay = total_bill - discount
    counter +=1
    print(f"AMOUNT: {amount}")
print(f"TOTAL BILL: {total_bill}\nDISCOUNT: {discount}\nfinal bill {net_pay} ")
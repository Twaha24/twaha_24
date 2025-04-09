#write the program to ask the nuser enter item taken, quantity and price
#the program should compute the amount
item_taken = input('enter item taken: ')
quantity = input("enter quantity taken: ")
price = input("enter price of the amount: ")

amount = int(price) * int(quantity )
print(f"you have bought {item_taken} of total amount = {amount}UGX")
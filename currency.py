currencies = {
"USD": 3750,
 "GBP":5000,
 "DELAM":6000,
 "YUAN":3000,
 "TWA":3500,

}

user_amount = int(input("ENTER AMOUNT: "))
currency = input("ENTER CURRENCY: ")

currencies.get(currency)
exchange_amount = user_amount /currencies.get(currency)
   
print(f"EXCHANGE RATE : {exchange_amount}")
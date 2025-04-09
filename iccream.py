

    # Prices (you can adjust these)
print('''
1. cup = 1000
2. scoop = 1000
3. lake = 1500
4. sprinkles = 2500
5. strawberry = 2000
6. cone   = 3000   
''')
prices = cup =  1000
flakes =  1500
sprinkles =  2500
strawberry = 2000
cone = 3000
#choosing a container
container = input("please choose a container cup/cone")
scoops = int(input(" how many scoops do you want (1-4)"))
if scoops >4:
    print("scoops do not exceeed 4")
flake = input(" would you like  the flake?:(yes/no) ")
chocolate_sprinkle = input("would you like a chocolate sprinkle?(yesa/no) ")
strawberry = input("would you like a strawberry?(yes/no) ")

# calculations of prices
total_price = 0
if prices ==cup:
    total_price =  scoops * prices
elif prices == cone:
    total_price = scoops * prices  
elif prices == flakes:
    total_price = flakes * prices  
elif prices == strawberry:
    total_price = strawberry * prices
elif prices == sprinkles:
    total_price = sprinkles * prices  
           

         
          



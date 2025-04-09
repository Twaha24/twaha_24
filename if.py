# Basic if statement
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# If-elif-else example
age = 15

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


# Nested if example
num = 10

if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")

# Using logical operators
temperature = 25

if temperature > 20 and temperature < 30:
    print("The weather is warm.")
else:
    print("The weather is not warm.")

# Using 'in' with if statement
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list of fruits.")
else:
    print("Apple is not in the list of fruits.")


# Conditional expression
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)

numbers = []

no_of_numbers = 10
for number in range(no_of_numbers):
    number += 1
    value = int(input(f"ENTER NUMBER {number}: "))
    numbers.append(value)
numbers.sort()    
print(numbers)
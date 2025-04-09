text = ('''n python Basics: Strings and  String Methods, you used strings for text
data in python. You also learned  how to manipulate stings with string Methods.
For example, you changed strings from lowercase to uppercase,
removed whitespace from the beginning or end of a string,
and replaced parts of the string with different text''')

#a python program to count the occurrence of string,python,method
print(f"string: {text.count("strings")}")
print(f"python: {text.count("python")}")
print(f"Method: {text.count('method')}")

#replace all space characters with->
print(text.replace(" ","->"))

#display the length(number of characters)of the paragraph
print(f"length: {len(text)}")

#checking if "print" exists in the paragraph (NOTE : if statement not needed)
print("print" not in text)

#display characters from 20 to 80
print(f"characters from 20 to 80: {text[20:80]}")
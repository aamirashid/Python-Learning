# Python Basics Exercises
# 1. Assign a message to a variable and then print that message.
message = "Amir Rashid PIAIC107890 GenAI Batch 62."
print(message)

# 2.1 Assign a message to a variable and print that message.
message = "This task is same as above."
print(message)

# 2.2 Change the value of the variable to a new message, and print the new message.
message = "Initialization"
print(message)
message = "Reinitialization"
print(message)

# 3. Use a variable to represent a person’s name. Print a message to that person,
# such as, “Hello Eric, would you like to learn some Python today?”
name = "Amir Rashid"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

# 4. Use a variable to represent a person’s name.
# Print the person’s name in lowercase, uppercase, and title case.
name = "aMir rasHid"
print(name.lower())
print(name.upper())
print(name.title())

# 5. Find a quote from a famous person you admire. Print the quote and the name of its author.
# The output should look something like the following:
# Albert Einstein once said, "A person who never made a mistake never tried anything new."
author = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
print(f'{author} once said, "{quote}"')

# 6.Use a variable called famous_person to represent the famous person’s name.
# Compose the message and represent it with a variable called message. Print the message.
famous_person = "Hazrat Ali ibn Abi Talib"
message = "The most complete gift of ALLAH is: A life based on knowledge."
print(f'{famous_person}, said, "{message}"')

# 7. Stripping Names - Use a variable to represent a person’s name, and include some
# whitespace characters at the beginning and end of the name. Make sure you use each
# character combination, \t and \n, at least once. Print the name once, so the whitespace
# around the name is displayed. Print the name using each of the three stripping functions:
# lstrip(), rstrip(), and strip().
name = "     Amir Rashid\t\t"
print(f"Name with original whitespaces: '{name}'")
print(f"Name after lstrip(): '{name.lstrip()}'")
print(f"Name after rstrip(): '{name.rstrip()}'")
print(f"Name after strip(): '{name.strip()}'")

# 8. Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum.
x=5
y=10
z=15
sum=x+y+z
print(f"The sum of {x}, {y}, and {z} is: {sum}")

# 9. Swap the values of two variables a and b. Print the values before and after the swap.
a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")
a,b = b,a               # swapping
print(f"After swap: a = {a}, b = {b}")

# 10. Create a variable with your favorite color and print it.
# Then change the variable name to something else and print the color again.
fav_color="Green"
print("Favorite Color is", fav_color)
color=fav_color
print("Favorite Color is still", color)

# 11. Create a variable pet_name and set it to "Buddy".
# Change the value of pet_name to "Max" and print the new value.
pet_name = "Buddy"
print("Original pet_name is", pet_name)
pet_name = "Max"
print("Changed value of pet_name is", pet_name)

# 12. Assign the value "Sunshine" to a variable and print it.
# Then, mistakenly try to print a variable with a different name (like sunsine) and observe the error.
weather = "Sunshine"
print("The weather is", weather)
#print("The weather is", sunsine)

# 13. Assign the value 100 to a variable score and print it.
# Then assign a new value to score and print it again.
score=100
print("Initial value of score is:", score)
score=110
print("Updated value of score is:", score)

# 14. Create a string variable city and assign it the name of a city you like. Print the city name.
city: str = "Makkah"
print("City i like is", city, "and date type of this city belongs", type(city))

# 15. Create a variable text with the value "python programming" and print it in title case.
text = "python programming"
print("In Title case:", text.title())

# 16. Assign a string with mixed cases to a variable and print it in all lowercase letters.
mixed_cases = "aMir RAShid"
print("In Lower Case:", mixed_cases.lower())

# 17. Assign a string with mixed cases to a variable and print it in all uppercase letters.
mixed_cases = "aMir RAShid"
print("In Upper Case:", mixed_cases.upper())

# 18. Create a variable temperature with the value 25.
# Print "The current temperature is [temperature] degrees." using the variable.
temperature = 25
print(f"The current temperature is {temperature} degrees.")

# 19. Create a variable poem with a short poem that has multiple lines.
# Print the poem with each line starting on a new line.
poem = """This is an example of a multi-line
short poem in which each line appears
on a new line.
 
You may create a variable by using 
triple quotes (single or double) 
to handle multi-line strings."""
print(poem)
# End
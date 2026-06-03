""" Python Strings """
# Triple Quotes in Python
United_kingdom = '''
 The United Kingdom comparises Englan, Scoutland, Northern Ireland and Wales.'''

print(United_kingdom)
print(type(United_kingdom))

# Types in Python
score = 20



print(score)
print(type(score))

# Indexing in String
my_location = "united_kingdom_nottingham"
print(my_location[0:14])
print(my_location[1])

# Using f-string in Python
name = "Emmanuel"
location = "Nottingham"
age = 30

print(f"My name is {name}, I live in {location}, and I am {age} years old.") 

# Concatenating Strings in Python
first_name = "Saturday"     

last_name = "Okposio"
age = 40

full_message = "My name is " + first_name + " " + last_name + " " + "and my age is " + str(age) + "."
print(full_message.upper())
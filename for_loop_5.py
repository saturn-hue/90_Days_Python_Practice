"""For Loop in Python"""
# Looping through List
animal_kingdom = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Zebra']

for x in animal_kingdom:
    print(x)
    if x == 'Tiger':
        break

# looping through String
for a in "nottingham":    
    print(a)
    if a == 'a':
        break

# Continue Statement in For Loop(continue skipped the current iteration and move to the next one)
animal_kingdom = ['Monkey', 'Lion', 'lizard', 'kangaroo', 'Snake', 'Fox', 'Panda', 'Bear']

for x in animal_kingdom:    
    if x == 'Snake':
        continue
    print(x)

# Range Function in For Loop(Note that range(40) is not the values of 0 to 40, but the values 2 to 37.)
# range(start, stop, step)
for u in range(2, 40, 5):
    print(u)

# Loop in Dictionary 
user_details = {"name": "John", "age": 30, "city": "New York", "occupation": "Software_Engineer"} 
for key, value in user_details.items():
    print(key, value)

#Tuples in Loop
# Looping through a tuple
school_scores = (101, 22, 523, 454, 65, 96, 74)
for num in school_scores:
    print(num)

# Nested loop
fruits = ['apple', 'banana', 'cherry', 'date']
colors = ['red', 'green', 'blue']
for fruit in fruits:
    for color in colors:
        print(fruit, color)

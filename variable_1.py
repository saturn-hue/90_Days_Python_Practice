"""working with python variables"""

# Assign values to multiple variables in one line
animal_types, fruits_types, car_types, number = "mammals", "tropical", "sedan", 100

print(animal_types)

print(fruits_types)

print(car_types)

print(type(number))

# Assign one to multiple variables in one line
_lizards = _snakes = _turtles = "reptiles"

print(type(_lizards))

print(_snakes)

print(_turtles)

# Case-Sensitivity of Python Variables

age = 40

Age = 20

print(type(age))

print(Age)

# Global Variable
""" Print a list of primates using a global variable and a function """
# monkey = chimpanzee = gorilla = "primates"
primates = ["monkey", "chimpanzee", "gorilla"]

""" Define a function to print the list of primates using the global variable """
def show_primates() -> None:
    print(
        f"The following are relatives:  {primates[0]}, {primates[1]}, and {primates[2]}"
    )


# print(f"The following are relatives:", ", ".join(primates))

show_primates()

#Swapping Two Variables
a, b = 5, 10
a, b = b, a
print(a, b)

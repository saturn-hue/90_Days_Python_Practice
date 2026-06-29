""" Python Set """
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.*/
#Set ignore duplication, set unchangeable, unordered

#  Simple set
english_fruits = {"apple", "orange", "banana", 20,  True, False}
print(len(english_fruits))
print(type(english_fruits))


# Loop in set
weather = ("summer", "sunny", "rain", "cold")
for x in weather:
    print(x)

print(weather)
# Check if "cold" is present in the set:
print("cold" in weather)


# Adding to set
car_in_stores = {"bmw", "toyota", "audi"}
car_in_stores.add("jeep")
#print(car_in_stores)



# To add items from another set into the current set, use the update() method.:
car_in_stores = {"bmw", "toyota", "audi"}
english_fruits = {"apple", "orange", "banana", 20,  True, False}
car_in_stores.update(english_fruits)

# Removing set
car_in_stores.remove("bmw")
print(car_in_stores)

# updating set(set doen't pick duplicate item twice, only pick one out of all)
fruit_set = {"mango", "plum", "cashew", "mango"}
animal_set = {"giraffe", "zebra", "panda", "panda"}
cities_names = {"London", "Ghana", "Nigeria", "London"}

fruit_set.update(animal_set, cities_names)
fruit_set.discard("cashew")


#items = fruit_set.intersection()

print(fruit_set)


# Joining In Set
student_names = {"John", "Andrew", "Paul"}
student_skills = {"SQL", "Power_Bi", "Python"}
student_scores = {70, 50, 65, 40, 89}

student_details = student_names.union(student_skills)
print(student_details)
""" Python Dictionary"""

# Creating simple Python dictionary
car_details = {
    "brand": "BMW",
    "model": "X3",
    "year": 2026,
    "cost": 75000,
    "engine": "full electric",
    "door": 4
}

new_car_details = car_details.get("year")
print(new_car_details)

# Adding item to Dictionary
car_details.update({"location": "Nottingham"})

#Adding item to Dictionary
car_details["brand"] ="Ford"
car_details["bluetooth"] = True

# Changing the value of an existing key
car_details["color"] ="Green"

# Removing item from dictionary
car_details.pop("cost")

# looping through dictionary(bo)
for key, value in car_details.items():
    print(key, value)

#Looping through dictionary keys
for  key in car_details:
    print(key)

# Looping through dictionary values
for value in car_details.values():
    print(value)    

#car_details.clear()  # This will remove all items from the dictionary

print(car_details)
print(type(car_details))
print(car_details["year"])
print(car_details.get("model"))

# Nested Dictionary
user_details_1 = {
    "name": "Johnson",
    "age": 47,
    "location": "London"
}

user_detals_2 = {
    "name": "Paul",
    "age": 82,
    "location": "Manchester"
}

user_details_3 = {
    "name": "David",
    "age": 35,
    "location": "Liverpool"
}

attendees = {
    "user_1": user_details_1,
    "user_2": user_detals_2, 
    "user_3": user_details_3
}

# Accessing nested dictionary values
print(attendees["user_2"]["location"])

#Looping through nested dictionary
for user, details in attendees.items():
    print(user)
    for key, value in details.items():
        print(key, value)



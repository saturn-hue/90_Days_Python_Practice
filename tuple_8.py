""" Python Tuples, tuple is an immutable ordered collection of elements """

# Creating a tuple
united_kigdom_cities = ("Derby","Nottingham", "conventry", "Leicester", "London", "Manchester", "Liverpool", "Birmingham")

print(united_kigdom_cities[3:])



#  Create tuple Stores Details and delete one of the element from the tuple
store_details = ("Store_Name", "Store_Location", "Store_Owner", "Store_Contact_Number")
new_store_details  = list(store_details)

new_store_details.remove("Store_Location")

store_details = tuple(new_store_details)

# Accessing Tuple elements
print(store_details)


print(len(store_details))


# check item in Tuple
fruits_inventory = ("Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Watermelon", "Papaya", "Kiwi", "Strawberry")


if "Potato" in fruits_inventory:
    print("Yes  Potato is available in the fruits inventory")
else:
    print("No is not available in the fruits inventory")    



# Concatenating Tuples

street_numbers = (10, 50, 90, 50, 70, 80, 90, 100)

street_names = ("Main Street", "Oak Avenue", "Pine Road", "Elm Street", "Maple Drive", "Cedar Lane", "Willow Way", "Birch Court")

detail_informations = street_names + street_numbers

print(detail_informations)


#Updating Tuple elements
data_engineering_skills = ("Python", "Data Warehousing", "ETL", "Data Modeling", "Data Visualization", "Big Data", "Machine Learning", "Biology")

# Converting Tuple to List in other to modify tuple
data_skills = list(data_engineering_skills)

# Removing Tuple
data_skills.remove("Biology")

# Adding SQL to list
data_skills[-1] = "SQL"

# Converting back to tuple
data_engineering_skills = tuple(data_skills)

print(data_engineering_skills)

# Looping through Tuple
data_engineering_skills = ("Python", "Data Warehousing", "ETL", "Data Modeling", "Data Visualization", "Big Data", "Machine Learning", "Big_Query")

for k in range(len(data_engineering_skills)):

    print(data_engineering_skills[k])




# Tuple Method (Returning number of times the value occurance  in tuple)
scores = (10, 20, 50, 20, 60, 40, 50, 99, 2, 66, 20, 100)
score_rating = scores.count(50)

print(score_rating)

# Tuple conversions  to dictionary (Countries and currencies )
country_currencies = ("usa", "dollar", "uk", "pound", "nigeia", "naira", "ghana", "cedi")

new_conversion =  dict(zip(country_currencies[0::2], country_currencies[1::2]))
print(new_conversion)
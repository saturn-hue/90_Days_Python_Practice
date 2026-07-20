""""JSON 14: A Python module for handling JSON data. """

# (1) Loop through JSON data

import json 

with open("customers.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for customer in data:
    print(customer['id'], customer['name'], customer['phone'], customer['email'])
    #print(type(customer))

    #print(json.dumps(customer['name'], indent=4, sort_keys=True))
    #print(json.dumps(customer['phone']))

    # Pretty‑print JSON (human‑readable)
     # print(json.dumps(data, indent =4, sort_keys=True))

    #print(json.dumps(customer, indent=4, sort_keys=True))
  

#(2) Create json string from dictionary

# user_details = {
#     'first_name': 'Saturday', 
#     'last_name': 'Okposio', 
#     'age':57, 
#     'location': 'Nottingham',
#       'is_married': True
#       }

# jsonString = json.dumps(user_details)
# print(jsonString)




# (3) Create JSON string from Python list
# fruits_cost = [{
#     'mango': 10,
#     'orange':20,
#     'cashew':50
#     }]

# jsonString = json.dumps(fruits_cost)

# print(jsonString)

#Convert dictionary with values of different types to JSON
# store = {
#     "name": "John Doe",
#     "age": 30,
#     "is_student": False,
#     "grades": [85, 71, 39]
# }

# jsonString = json.dumps(store)
# print(store["name"], store["age"], store['grades'])


#(4) Convert dictionary with values of different types to JSON
# store_products = {'fruits':['orange', 'cashew', 'potato'], 'cars':['toyota', 'benz', 'ford'], 'laptops':['hp', 'dell', 'lenovo']}

# jsonString = json.dumps(store_products)

#Return the length of the list of laptops in the store_products dictionary
# print(len(store_products['laptops']))

# print(type(jsonString))
# print(json.dumps(store_products, indent=4, sort_keys=True))



# (6) Convert Python List to JSON string
# uk_cities = ['London', 'Manchester', 'Liverpool', 'Birmingham', 'Leeds']
# jsonString =json.dumps(uk_cities)
# print(jsonString)

#(7) Convert Python list of dictionaries to JSON
# students_details = [
#     {"name": "Saturday", "age": 57, "location": "Nottingham"},
#     {"name": "Bukky", "age": 48, "location": "Ibadan"},
#     {"name": "Favour", "age": 23, "location": "Ibadan"},
#     {"name": "Great", "age":21, "location": "Ibadan"}
# ]
# jsonString = json.dumps(students_details)
# print(json.dumps(students_details, indent=4, sort_keys=True))


# with open('customers.json', 'r') as f:
#     data = json.load(f) 
#print(data)

# import os
# print(os.getcwd())

# import os
# print(os.getcwd())



# with open(r"C:\Users\Home\Desktop\customers.json", "r") as f:
#     data = json.load(f)

# print(data)

# import os
# print(os.getcwd())
# print(os.path.exists(r"C:\Users\Home\Desktop\customers.json"))




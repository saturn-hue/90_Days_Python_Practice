""" Python List"""

# ANIMAL LIST

# Create a List and  nested list
animal_list = [['cat', 'dog', 'rabbit'], ['parrot', 'hamster', 'tiger'], ['lion', 'elephant', 'giraffe', 'zebra'], ['bear', 'wolf']]

# Loop through the list and print each element
for s in range(len(animal_list)):
    print(animal_list[3][1])



#adding new element to the list to the end of the list
animal_list.append("monkey")
print(animal_list)

# FRUIT LIST

fruit_list = ['apple', 'banana', 'cherry', 'apple', 'kiwi', 'mango', 'orange', 'papaya', 'pear', 'pineapple', 'plum', 'strawberry']

fruit_list.append("cahew")

fruit_list.extend(['grape', 'watermelon'])  # Sort the list in ascending order

for fruit in fruit_list:
    print(fruit)





# Removing an elemt from the list
fruit_list.remove("apple")

# Removing an element from the list using pop() method(specified index in the list)
fruit_list.pop()

# deleting an element from the list using del() method(specified index in the list)
del fruit_list[2]


print(fruit_list)


""""Python Array Module is used to create an array. An array is a data structure that can hold more than one value at a time. It is similar to a list in Python, but it can only hold values of the same data type. The array module provides an array() function that can be used to create an array. The array() function takes two arguments: the first argument is the data type of the array, and the second argument is a list of values to be stored in the array."""

import array as arr
# The first argument specifies the (Type of the values) that we store in the array
# The second argument is a (list of the values) using which the array is initialized.

#(1)
# Create Signed Integer Array
my_score = arr.array('i', [10, 52, 99, 45, 41])

#Update elements of Python array
my_score[3] = 1005
print(my_score[3])  # Output: 1005


#(2)
# Create Array with Floating Point Numbers
street_numbers = arr.array('f', [10.6, 8.5, 5.4, 7.5, 4.4])

# Remove last item in given integer array
removed_number = street_numbers.pop()
print("The last number that was removed :", removed_number)  # Output: 4.4


# Append new value to the array
street_numbers.append(200.5)
print(street_numbers)  # Output: array('f', [10.6, 8.5, 5.4, 7.5, 4.4, 1000.5])
print("The street number is:", len(street_numbers), "and the value is:", street_numbers[1])

#(3)
# Create Empty Integer Array
empty_cards = arr.array('i', [])
print(empty_cards)  # Output: array('i')


#(4)
#Python - Iterate over Array
my_score = arr.array('i', [10, 52, 99, 45, 41, 400, 59, 55, 100, 200])

for x in my_score:    
     # Output: 10, 52, 99, 45, 41, 400, 59, 55, 100, 200
    print(x) 
    print("Array Type:", my_score.typecode) # Output: 10, 52, 99, 45, 41, 400, 59, 55, 100, 200


#(5)
# Python Array - Remove Item at (specific Index)
store_prize = arr.array('i', [10, 52, 99, 45, 41, 400, 59, 55, 100, 200, 50])
i =  5
store_prize.pop(i) # 400 Removed from the array
print(store_prize)


""""Python Range() function is used to generate a sequence of numbers. It is commonly used in for loops to iterate over a block of code a specified number of times. The range() function can take one, two, or three arguments:"""
score_number =range(6)

print(len(score_number))

# Range with 2 arguments
score_number = range(3, 11)
print(list(score_number))

# range with 3 arguments
city_numbers = range(5, 50, 5)

print(len(list(city_numbers)))


#For loop in Range
car_price = range(5, 20, 3)
car = []

for x in car_price:    
    car.append(x)
    print(car)

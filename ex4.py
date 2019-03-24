cars = 100 #amount of cars
space_in_a_car = 4.0#if we wtite just =4, it won't be a float number
#this the space of the car
drivers = 30#amount of drivers
passengers = 90#amount of passengers
cars_not_driven = cars - drivers #amount of not available cars
cars_driven = drivers#amount of available cars
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven#the average
#"Traceback (most recent call last ): File ”ex4.py”, line 8, in <module>
#average_passengers_per_car = car_pool_capacity / passenger NameError: name ’car_pool_capacity ’ is not defined"
#this error, the name is not defined, because it wrotten incorrect.
#"carpool" wrutten without underscore
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")

print('THE 4TH TASK')
i = 3
x = 4
j = 5

print(i * j)
print(x - j*i)

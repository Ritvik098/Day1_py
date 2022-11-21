# my_age = 10
# print(my_age + 12345)

# first_name = "bob"
# last_name = "som"
# print(first_name + " " + last_name)

# bool(0)
# print(bool(0))

# helloworld = 5
# print(helloworld)

# full_name = "Rick"
# print("my name is " + full_name)

# myNumber = 100
# print(myNumber + 1)


# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers #70
# cars_driven = drivers #30
# carpool_capacity = cars_driven * space_in_a_car #120
# average_passengers_per_car = passengers / cars_driven #3

# print("There are", cars, "cars available.")
# print("There are only", drivers, "drivers available.")
# print("There will be", cars_not_driven, "empty cars today.")
# print("We can transport", carpool_capacity, "people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", average_passengers_per_car,"in each car.")

# age = input("How old are you? ")
# print("You are {} years old".format(age))


# number = input("Enter a number between 1 and 100")
# if  > b 

number = input("Enter a number between 1 and 100 ")
number = int(number) 

if number < 1 or number > 100:
    print("invaild Number")
else:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz") 
    elif number % 5 == 0:
        print("Buzz")
        

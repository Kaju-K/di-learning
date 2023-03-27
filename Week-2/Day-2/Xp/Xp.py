# Exercise 1

my_fav_numbers = set()
my_fav_numbers.add(3)
my_fav_numbers.add(14)

my_fav_numbers_list = list(my_fav_numbers)
my_fav_numbers_list.pop(-1)

my_fav_numbers = set(my_fav_numbers_list)

friend_fav_number = {2,4,6,8,10}

our_fav_number = my_fav_numbers.union(friend_fav_number)

print(our_fav_number)

# Exercise 2

# can't change a tupple, they are immutable
# the way to do it is to transform it into a list and than get back to tuple

my_tuple = (3, 14)
my_tuple_list = list(my_tuple)
my_tuple_list.append(15)
my_tuple = tuple(my_tuple_list)

# or you can use the spread operator

my_tuple2 = (3, 14)
value_to_add = 15
my_tuple2 = (*my_tuple2, value_to_add)

# Exercise 3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")

basket.append("Kiwi")

basket.insert(0,"Apples")

print(basket.count("Apples"))

basket.clear()

print(basket)

# Exercise 4

# Float has decimal values
# for example:
# Float -->  3.1415926535
# Integer --> 3

max_number = 5
min_number = 1.5
pace = 0.5

amount_numbers = int(((max_number - min_number)/pace + 1))

float_list = []

for i in range(amount_numbers):
    float_list.append(1+(i+1)*pace)

print(float_list)

# Exercise 5

for i in range(20):
    print(i+1)

# Exercise 6

my_name = "marcelo"
input_name = ""

while input_name.lower() != my_name:
    print("What's your name?")
    input_name = input()

# Exercise 7

print("What's your favorite fruits? (If more than one, separate the fruits with a single space -> \"apple cherry mango\")")

fruit_input = input().lower()

fruit_list = fruit_input.split(" ")

print("\nNow write the name of any fruit (just one)")
fruit_name = input().lower()

if (fruit_name in fruit_list):
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 8

not_satisfied = True
toppings = []

while not_satisfied:
    print("What toppings do you want to add in your pizza?")
    single_topping = input().lower()
    toppings.append(single_topping)
    print("\nDo you want to add more? If yes, type anything, if no, type quit")
    user_answer = input().lower()
    if (user_answer == "quit"):
        not_satisfied = False

print(f"\nNice, you pizza will be with {', '.join(toppings)}. It will cost you {10+2.5*len(toppings)} NIS")

# Exercise 9

print("What are the ages of people that wants to get a ticket? (write the number with a space between each number)")
ages = input()

ages_list = ages.split(" ")

total = 0

for age in ages_list:
    age_int = int(age)
    if (age_int < 3):
        continue
    elif (3 <= age_int < 12):
        total += 10
    else:
        total += 15

print(f"It will be a total of {total} NIS. Enjoy!")


print("What are the names of the people in the group? (write with a space between each name)")
teen_names = input().lower()
teen_names_list = teen_names.split(" ")
not_allowed = []

for name in teen_names_list:
    teen_age = int(input(f"How old is {name}? "))
    if (16 > teen_age) or (teen_age > 21):
        print("oi")
        not_allowed.append(name)
    
for name in not_allowed:
    teen_names_list.remove(name)

print(f"The list of people that are allowed in this movie is: {', '.join(teen_names_list)}")

# Exercise 10

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches = []

for i in range(len(sandwich_orders)):
    finished_sandwiches.append(sandwich_orders.pop(0))

for i in finished_sandwiches:
    print(f"I made your {i}")

# Exercise 11

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Egg sandwich", "Pastrami sandwich", "Sabih sandwich", "Pastrami sandwich"]

print("Deli has run out of pastrami.")

finished_sandwiches = []

for i in range(len(sandwich_orders)):
    sandwich = sandwich_orders.pop(0)
    if "pastrami" not in sandwich.lower():
        finished_sandwiches.append(sandwich)

print(finished_sandwiches)
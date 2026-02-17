# Task 01: Split the alice_in_wonderland variable so that it spans multiple physical lines.
alice_in_wonderland = """ Would you tell me, please, which way I ought to go from here?
That depends a good deal on where you want to get to," said the Cat.
I don't much care where ——" said Alice.
Then it doesn't matter which way you go," said the Cat.
—— so long as I get somewhere, Alice added as an explanation.
Oh, you're sure to do that," said the Cat, if you only walk long enough.
"""


# task 02 == Find and display all single quote characters single quote in the text.
one_quotes = [i for i, char in enumerate(alice_in_wonderland) if char == "'"]
print(f"Single quotes are located at the following positions: {one_quotes}")
# task 03 == Print the alice_in_wonderland variable
print(f"{alice_in_wonderland}")


"""
    # Tasks 04 - 10:
    # Translate the problems from the "Mathematics, 5th Grade" textbook
    # into Python code and output the answers in a way
    # that is easy for a 5th-grade student to understand.
"""
# task 04
"""
The area of the Black Sea is 436,402 km², and the area of the Sea of Azov is 37,800 km².
What is the total area occupied by the Black and Azov Seas together?
"""

black_sea_area = 436_402
azov_sea_area = 37_800
print(f"Total area of the seas: {black_sea_area + azov_sea_area} km2")


# task 05
"""
A supermarket chain has 3 warehouses with a total of 375,291 items. 
The first and second warehouses contain 250,449 items. 
The second and third warehouses contain 222,950 items. 
Find the number of items stored in each warehouse.
"""

total_items = 375_291
first_and_second_shop = 250_449
second_and_third_shop = 222_950
second = second_and_third_shop - (total_items - first_and_second_shop)
first = first_and_second_shop - second
third = second_and_third_shop - second
print(f"Number of items stored in first warehouse: {first} ")
print(f"Number of items stored in second warehouse: {second} ")
print(f"Number of items stored in third warehouse: {third} ")

# task 06
"""
Mike and his parents decided to buy a computer using an 'Installment Plan'. 
It is known that they will have to pay 1,179 EUR per month for a year and a half. 
Calculate the total cost of the computer.
"""

year = 12
half_year = 6
month_payment = 1_179
full_period = year + half_year
total_cost = full_period * month_payment
print(f"Installment Plan: {total_cost}")

# task 07
"""
Find the remainder of the division for the following numbers:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019
b = 9907
c = 2789
d = 7248
e = 7128
f = 19224
remainder_a = a % 8
remainder_b = b % 9
remainder_c = c % 5
remainder_d = d % 6
remainder_e = e % 5
remainder_f = f % 9
print(f"Remainder of the division 8019 : 8 = {remainder_a}")
print(f"Remainder of the division 9907 : 9 = {remainder_b}")
print(f"Remainder of the division 2789 : 5 = {remainder_c}")
print(f"Remainder of the division 7248 : 6 = {remainder_d}")
print(f"Remainder of the division 7128 : 5 = {remainder_e}")
print(f"Remainder of the division 19224 : 9 = {remainder_f}")


# task 08
# Irynka is preparing for her birthday and has made a shopping list.
# Calculate the total amount of money needed for her order.
# Items: Large Pizza ( 274 UAH), Medium Pizza (2 x 218 UAH), Juice  (4 x 35 UAH),
# Cake (1 x 350 UAH), Water (3 x 21 UAH).

pizza_large = 274
pizza_large_qty = 4
pizza_medium = 218
pizza_medium_qty = 2
juice = 35
juice_qty = 4
cake = 350
cake_qty = 1
water = 21
water_qty = 3
total_pizza_large = pizza_large * pizza_large_qty
total_pizza_medium = pizza_medium * pizza_medium_qty
total_juice = juice * juice_qty
total_cake = cake * cake_qty
total_water = water * water_qty
total_order_amount = (total_pizza_large + total_pizza_medium + total_juice + total_cake + total_water)
print(f"Total amount for order: {total_order_amount} UAH")

# task 09
# Task: Photo Album Calculation
# Ihor has 232 photos. Each album page can hold up to 8 photos.
# Calculate how many pages are needed for all photos.

total_photos = 232
photos_per_page = 8
pages_needed = total_photos // photos_per_page
remaining_photos = total_photos % photos_per_page
print(f"Total photos: {total_photos}")
print(f"Number of pages needed: {pages_needed}")

# task 10
# A family is planning a road trip from Kharkiv to Budapest. The distance between these cities is 1,600 km.
# It is known that 9 liters of gasoline are needed for every 100 km. The fuel tank capacity is 48 liters.
# 1) How many liters of gasoline will be needed for this trip?
# 2)What is the minimum number of times the family needs to stop at a gas station during this trip,
# filling up a full tank each time?

distance = 1_600
gasoline_per_100km = 9
fuel_tank = 48
total_fuel_needed = (distance / 100) * gasoline_per_100km
refills_needed = total_fuel_needed // fuel_tank
print(f"Total fuel needed: {total_fuel_needed} liters")
print(f"Minimum number of full tank refills: {int(refills_needed)}")


# Task 11: School Supplies
# English Translation: A school bought 45 laptops for 12,500 UAH each
# and 15 interactive whiteboards for 24,300 UAH each. What is the total cost of all the equipment?

laptop = 45
laptop_price = 12_500
white_board = 15
white_board_price = 24_300
total_laptop_cost = laptop_price * laptop
total_white_board_cost = white_board_price * white_board
all_devices_cost = total_laptop_cost + total_white_board_cost
print(f"Total cost of all the equipment: {all_devices_cost} UAH")


# Task 12: Fruit Warehouse
# A warehouse has 1,200 kg of fruit. There are 450 kg of apples and 380 kg of pears.
# The rest are bananas. How many kilograms of bananas are in the warehouse?

total_fruit = 1_200
apples = 450
pears = 380
bananas = total_fruit - (apples + pears)
print(f"Total bananas in warehouse: {bananas}")


# Task 13: Delivery Van
# A delivery van needs to transport 155 identical boxes.
# The van can carry a maximum of 12 boxes per trip. How many trips will the van need to make to deliver all the boxes?
# (Hint: consider if there is a remainder).

boxes = 155
capacity_van = 12
full_trips = boxes // capacity_van
leftover_boxes = boxes % capacity_van
total_trips = full_trips + (1 if leftover_boxes > 0 else 0)

print(f"Full trips: {full_trips}")
print(f"Boxes left for the last trip: {leftover_boxes}")
print(f"Total trips needed to deliver ALL boxes: {total_trips}")


# Task 14: Time Conversion
# An automation script runs for 5,000 seconds.
# Convert this time into full minutes and remaining seconds.

script_time = 5_000
seconds_in_minute = 60
full_minutes = script_time // seconds_in_minute
remaining_seconds = script_time % seconds_in_minute
print(f"Total time: {full_minutes} minutes and {remaining_seconds} seconds")

# Task 15: Egg Cartons
# A farm collected 147 eggs. One carton can hold 12 eggs.
# How many full cartons are ready for sale?
# How many eggs are left over and cannot fill a whole carton?

eggs = 147
carton_hold = 12
total_carton = eggs // carton_hold
eggs_left = eggs % carton_hold
print(f"Total cartons rady to sale: {total_carton} and {eggs_left} left.")


# Task 16: Building Floors
# A building is 52 meters high. Each floor is 3 meters high.
# Find the number of full floors and the height of the attic.

building_height = 52
floor_height = 3
full_building_floors = building_height // floor_height
high_attic = building_height % floor_height
print(f"Number of full floors is: {full_building_floors} and high in attic is: {high_attic} meters.")

# Task 17: Cinema Seats
# A cinema hall has 250 seats. Each row has 14 seats.
# How many full rows are in the hall?
# How many seats are in the last, incomplete row?

seats = 250
row = 14
full_row = seats // row
seats_incomplete_row = seats % row

print(f"Full rows are in the hall is: {full_row}.")
print(f"Seats in the last row is: {seats_incomplete_row}. ")

# Task 18: USB Flash Drive
# A USB flash drive has a capacity of 8 GB (8,192 MB). Each photo takes up 15 MB.
# How many full-sized photos can you save on the flash drive?
# How many megabytes of free space will be left?

capacity_mb = 8_192
photo_mb = 15
full_sized = capacity_mb // photo_mb
free_space = capacity_mb % photo_mb

print(f"You can save: {full_sized} full-sized photos.")
print(f"You have: {free_space} MB free space.")

# Task 19: Distributing Candies
# A teacher has 130 candies and wants to distribute them equally among 28 students.
# How many candies will each student receive?
# How many candies will the teacher have left over?

candies = 130
students = 28
students_got_candies = candies // students
candies_left = candies % students

print(f"Each student will receive: {students_got_candies} candies")
print(f"{candies_left} Candies will left over.")

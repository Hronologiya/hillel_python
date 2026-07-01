# Create a function called show_name.
# The function should print:
# "Leo"
# Call the function two times.
#
# def show_name():
#     print("Leo")
# show_name()
# show_name()
#
#
# Create a function called show_stars.
#
# The function should print:
# "**********"
#
# Call the function three times.
#
#
# def show_stars():
#     print("**********")
# show_stars()
# show_stars()
# show_stars()
#
#
# Create a function called show_menu.
#
# The function should print:
# "1. Start"
# "2. Settings"
# "3. Exit"
#
# Call the function once.
# def show_menu():
#     print("1. Start")
#     print("2. Settings")
#     print("3. Exit")
# show_menu()
#
#
# Create a function called greet_user.
# The function should have one parameter called name.
# Inside the function print:
# "Hello, " and the value of the parameter.
# Call the function three times with:
# "Leo"
# "Kate"
# "Mike"
#
#
# def greet_user(name):
#     print(f"Hello, {name}")
# greet_user("Leo")
# greet_user("Kate")
# greet_user("Mike")
#
#
# Create a function called introduce_person.
# The function should have one parameter called name.
# Inside the function print:
# "My name is " and the value of the parameter.
# Call the function with:
# "Leo"
# "Anna"
# "Tom"
# "Sophia"
#
#
# def introduce_person(name):
#     print(f"My name is {name}")
# introduce_person("Leo")
# introduce_person("Anna")
# introduce_person("Tom")
# introduce_person("Sophia")
#
#
# Create a function called introduce_person.
# The function should have two parameters:
# first_name
# age
# Inside the function print:
# "My name is <first_name> and I am <age> years old."
# Call the function with:
# "Leo", 25
# "Anna", 31
# "Tom", 18
#
#
# def introduce_person(first_name, age):
#     print(f"My name is {first_name} and I am {age} years old.")
# introduce_person("Leo",25)
# introduce_person("Anna", 31)
# introduce_person("Tom", 18)
#
#
# Create a function called greet_user.
# The function should have one parameter:
# name
# The default value of the parameter should be:
# "Guest"
# Inside the function print:
# "Hello, <name>"
# Call the function:
# 1. Without arguments.
# 2. With the argument "Leo".
# 3. With the argument "Anna".
#
#
# def greet_user(name="Guest"):
#     print(f"Hello, {name}")
# greet_user()
# greet_user("Leo")
# greet_user("Anna")
#
#
# Create a function called get_country.
# The function should not have any parameters.
# Inside the function return:
# "Ukraine"
# Save the returned value into a variable called country.
# Print the variable country.
#
#
# def get_country():
#     return "Ukraine"
# country = get_country()
# print(country)
#
#
# Create a function called get_full_name.
# The function should have two parameters:
# first_name
# last_name
# The function should return:
# "<first_name> <last_name>"
# Save the returned value into a variable called full_name.
# Print the variable full_name.
# Call the function with:
# "Leo", "Smith"
#
#
# def get_full_name(first_name, last_name):
#     return first_name + " " + last_name
# full_name = get_full_name(first_name="Leo", last_name="Smith")
# print(full_name)
#
#
# Create a function called create_email.
# The function should have two parameters:
# first_name
# last_name
# The function should return an email address in this format:
# "first_name.last_name@gmail.com"
# Example:
# first_name = "Leo"
# last_name = "Smith"
# Returned value:
# "Leo.Smith@gmail.com"
# Save the returned value into a variable called email.
# Print the variable email.
# Call the function with:
# "Leo", "Smith"
#
#
# def create_email(first_name, last_name):
#     return first_name + "." + last_name + "@gmail.com"
# email = create_email(first_name="Leo", last_name="Smith")
# print(email)
#
#
# Create a function called add_numbers.
# The function should have two parameters:
# first_number
# second_number
# The function should return the sum of the two numbers.
# Example:
# first_number = 10
# second_number = 5
# Returned value:
# 15
# Save the returned value into a variable called result.
# Print the variable result.
# Call the function with:
# 10, 5
#
#
# def add_numbers(first_number, second_number):
#     return first_number + second_number
# result = add_numbers(first_number=10, second_number=5)
# print(result)
#
#
# Create a function called multiply_numbers.
# The function should have two parameters:
# first_number
# second_number
# The function should return the product of the two numbers.
# Example:
# first_number = 6
# second_number = 4
# Returned value:
# 24
# Save the returned value into a variable called result.
# Print:
# "The result is:"
# Print the variable result.
# Call the function with:
# 6, 4
#
#
# def multiply_numbers(first_number, second_number):
#     return first_number * second_number
# result = multiply_numbers(first_number=6, second_number=4)
# print("The result is:")
# print(result)
#
#
# Create a function called is_even.
# The function should have one parameter:
# number
# If the number is even, return:
# True
# Otherwise, return:
# False
# Example:
# number = 8
# Returned value:
# True
# Save the returned value into a variable called result.
# Print the variable result.
# Call the function with:
# 8
#
#
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# result = is_even(8)
# print(result)
#
#
# Create a function called is_positive.
# The function should have one parameter:
# number
# If the number is greater than 0, return:
# True
# Otherwise, return:
# False
# Example:
# number = 15
# Returned value:
# True
# Save the returned value into a variable called result.
# Print the variable result.
# Call the function with:
# -5
#
#
# def is_positive(number):
#     if number > 0:
#         return True
#     else:
#         return False
# result = is_positive(-5)
# print(result)
#
#
# Create a function called is_adult.
# The function should have one parameter:
# age
# If the age is greater than or equal to 18, return:
# True
# Return:
# False
# Do not use else.
# Example:
# age = 20
# Returned value:
# True
# Save the returned value into a variable called result.
# Print the variable result.
# Call the function with:
# 16
#
#
# def is_adult(age):
#     return age >= 18
# result = is_adult(16)
# print(result)
#
#
# Create a function called check_temperature.
# The function should have one parameter:
# temperature
# If the temperature is greater than or equal to 20, return:
# "Warm"
# Otherwise, return:
# "Cold"
# Example:
# temperature = 25
# Returned value:
# "Warm"
# Save the returned value into a variable called result.
# Print the variable result.
# Call the function with:
# 15
#
#
# def check_temperature(temperature):
#     if temperature >= 20:
#         return "Warm"
#     else:
#         return "Cold"
# result = check_temperature(15)
# print(result)
#
#
# Create a function called check_password.
# The function should have one parameter:
# password
# If the password is equal to:
# "python123"
# Return:
# "Access granted"
# Otherwise, return:
# "Access denied"
# Example:
# password = "python123"
# Returned value:
# "Access granted"
# Save the returned value into a variable called result.
# Print the variable result.
# Call the function with:
# "123456"
#
#
# def check_password(password):
#     if password == "python123":
#         return "Access granted"
#
#     return "Access denied"
# result = check_password(password="123456")
# print(result)
#
#
# Create a function called check_discount.
# The function should have one parameter:
# age
#
# If age is greater than or equal to 65, return:
# "Senior Discount"
#
# If age is greater than or equal to 18, return:
# "Regular Price"
#
# Otherwise, return:
# "Child Discount"
#
# Save the returned value into a variable called result.
# Print the variable result.
#
# Call the function with:
# 70
#
#
# def check_discount(age):
#     if age >= 65:
#         return "Senior Discount"
#
#     if age >= 18:
#         return "Regular Price"
#
#     return "Child Discount"
# result = check_discount(age=70)
# print(result)
#
#
# Create a function called check_score.
# The function should have one parameter:
# score
# If score is greater than or equal to 90, return:
# "Excellent"
# If score is greater than or equal to 75, return:
# "Good"
# If score is greater than or equal to 50, return:
# "Pass"
# Otherwise, return:
# "Fail"
# Save the returned value into a variable called result.
# Print the variable result.
# Call the function with:
# 78
#
#
# def check_score(score):
#     if score >= 90:
#         return "Excellent"
#
#     if score >= 75:
#         return "Good"
#
#     if score >= 50:
#         return "Pass"
#
#     return "Fail"
# result = check_score(78)
# print(result)
#
#
# Create a function called check_user_status.
# The function should have one parameter:
# is_active
# If is_active is equal to True, return:
# "User is active"
# Otherwise, return:
# "User is inactive"
# Save the returned value into a variable called result.
# Print the variable result.
# Call the function with:
# False
#
#
# def check_user_status(is_active):
#     if is_active:
#         return "User is active"
#
#     return "User is inactive"
# result = check_user_status(False)
# print(result)
#
#
# Create a function called check_test_result.
# The function should have one parameter:
# passed
# If passed is True, return:
# "Test Passed"
# Otherwise, return:
# "Test Failed"
# Save the returned value into a variable called result.
# Print the variable result.
# Call the function with:
# True
#
#
# def check_test_result(passed):
#     if passed:
#         return "Test Passed"
#
#     return "Test Failed"
# result = check_test_result(True)
# print(result)
#
#
# Create a function called is_even.
# The function should have one parameter:
# number
# Return:
# True if the number is even.
# Otherwise, return:
# False
# Create another function called check_number.
# The function should have one parameter:
# number
# If is_even(number) returns True, return:
# "Even"
# Otherwise, return:
# "Odd"
# Save the returned value into a variable called result.
# Print the variable result.
# Call check_number with:
# 7
#
#
# def is_even(number):
#     if number % 2 == 0:
#         return True
#
#     return False
#
# def check_number(number):
#     if is_even(number):
#         return "Even"
#
#     return "Odd"
# result = check_number(7)
# print(result)
#
#
# Create a function called is_positive.
# The function should have one parameter:
# number
# Return:
# True if the number is greater than 0.
# Otherwise, return:
# False
# Create another function called check_number_type.
# The function should have one parameter:
# number
# If is_positive(number) returns True, return:
# "Positive"
# Otherwise, return:
# "Not positive"
# Save the returned value into a variable called result.
# Print the variable result.
# Call check_number_type with:
# -3
#
#
# def is_positive(number):
#     if number > 0:
#         return True
#
#     return False
#
# def check_number_type(number):
#     if is_positive(number):
#         return "Positive"
#
#     return "Not positive"
# result = check_number_type(-3)
# print(result)
#
#
# Create a function called is_admin.
# The function should have one parameter:
# role
# Return:
# True if role is equal to "admin".
# Otherwise, return:
# False
# Create another function called check_access.
# The function should have one parameter:
# role
# If is_admin(role) returns True, return:
# "Access granted"
# Otherwise, return:
# "Access denied"
# Save the returned value into a variable called result.
# Print the variable result.
# Call check_access with:
# "user"
#
#
# def is_admin(role):
#     if role == "admin":
#         return True
#
#     return False
# def check_access(role):
#     if is_admin(role):
#         return "Access granted"
#
#     return "Access denied"
# result = check_access("user")
# print(result)
#
#
# Create a function called is_valid_age.
# The function should have one parameter:
# age
# Return:
# True if age is greater than or equal to 18.
# Otherwise, return:
# False
#
# Create another function called register_user.
# The function should have one parameter:
# age
# If is_valid_age(age) returns True, return:
# "Registration completed"
# Otherwise, return:
# "Registration denied"
#
# Save the returned value into a variable called result.
# Print the variable result.
# Call register_user with:
# 16
#
#
# def is_valid_age(age):
#     if age >= 18:
#         return True
#
#     return False
# def register_user(age):
#     if is_valid_age(age):
#         return "Registration completed"
#
#     return "Registration denied"
# result = register_user(16)
# print(result)
#
#
# Create a function called is_logged_in.
# The function should have one parameter:
# logged_in
# Return:
# True if logged_in is True.
# Otherwise, return:
# False
# Create another function called open_dashboard.
# The function should have one parameter:
# logged_in
# If not is_logged_in(logged_in), return:
# "Please log in"
# Otherwise, return:
# "Dashboard opened"
# Save the returned value into a variable called result.
# Print the variable result.
# Call open_dashboard with:
# False
#
#
# def is_logged_in(logged_in):
#     if logged_in:
#         return True
#
#     return False
# def open_dashboard(logged_in):
#     if not is_logged_in(logged_in):
#         return "Please log in"
#
#     return "Dashboard opened"
# result = open_dashboard(False)
# print(result)
#
#
# Create a function called is_premium.
# The function should have one parameter:
# subscription
# Return:
# True if subscription is equal to "Premium".
# Otherwise, return:
# False
# Create another function called watch_video.
# The function should have one parameter:
# subscription
# If is_premium(subscription) returns True, return:
# "Video started"
# Otherwise, return:
# "Upgrade your subscription"
# Save the returned value into a variable called result.
# Print the variable result.
# Call watch_video with:
# "Basic"
#
#
# def is_premium(subscription):
#     if subscription == "Premium":
#         return True
#
#     return False
# def watch_video(subscription):
#     if is_premium(subscription):
#         return "Video started"
#
#     return "Upgrade your subscription"
# result = watch_video("Basic")
# print(result)
#
#
# Create a function called is_banned.
# The function should have one parameter:
# banned
# Return:
# True if banned is True.
# Otherwise, return:
# False
# Create another function called enter_game.
# The function should have one parameter:
# banned
# If not is_banned(banned), return:
# "Welcome to the game"
# Otherwise, return:
# "Access denied"
# Save the returned value into a variable called result.
# Print the variable result.
# Call enter_game with:
# True
#
#
# def is_banned(banned):
#     if banned:
#         return True
#     return False
#
# def enter_game(banned):
#     if not is_banned(banned):
#         return "Welcome to the game"
#     return "Access denied"
#
# result = enter_game(True)
# print(result)
#
#
# Create a function that returns True if a user is active.
# Create another function that allows the user to enter only if the user is NOT blocked.
#
# Call the function with:
# active = True
# blocked = False
#
# Expected result:
# "Access granted"
#
#
# def is_user_active(active):
#     if active:
#         return True
#     return False
#
# def is_blocked(blocked):
#     if blocked:
#         return True
#     return False
#
# def enter_game(active, blocked):
#     if not is_blocked(blocked) and is_user_active(active):
#         return "Access granted"
#     return "Access denied"
#
# result = enter_game(True, False)
# print(result)
#
#
# Create a function that checks if a user is verified.
# The function should have one parameter:
# verified
# Return True if the user is verified.
# Otherwise, return False.
#
# Create another function that returns:
# "Profile opened" if the user is verified.
# Otherwise, return:
# "Verification required"
#
# The second function should have one parameter:
# verified
#
# Save the returned value into a variable called result.
# Print the variable result.
# Call the second function with:
# False
#
#
# def is_verified(verified):
#     if verified:
#         return True
#     return False
#
# def open_profile(verified):
#     if is_verified(verified):
#         return "Profile opened"
#     return "Verification required"
#
# result = open_profile(False)
# print(result)
#
#

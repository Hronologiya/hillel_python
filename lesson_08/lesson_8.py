# Create a function called can_vote.
# The function should have two parameters:
# age
# citizen
# Return True only if:
# age is greater than or equal to 18
# AND
# citizen is True.
# Otherwise, return False.
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# age = 20
# citizen = True
#
#
# def can_vote(age, citizen):
#     if age >= 18 and citizen:
#         return True
#     return False
#
# result = can_vote(age=20, citizen=True)
# print(result)
#
#
# Create a function called can_buy_ticket.
# The function should have two parameters:
# age
# has_money
# Return True only if:
# age is greater than or equal to 16
# AND
# has_money is True.
# Otherwise, return False.
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# age = 15
# has_money = True
#
#
# def can_buy_tickets(age, has_money):
#     if age >= 16 and has_money:
#         return True
#     return False
#
# result = can_buy_tickets(15, True)
# print(result)
#
#
# Create a function called is_admin.
# The function should have one parameter:
# role
# Return True if role is equal to "admin".
# Otherwise, return False.
# Create another function called can_edit.
# The function should have two parameters:
# role
# active
# Return True only if:
# is_admin(role) is True
# AND
# active is True.
# Otherwise, return False.
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# role = "admin"
# active = True
#
#
# def is_admin(role):
#     if role == "admin":
#         return True
#     return False
#
# def can_edit(role, active):
#     if is_admin(role) and active:
#         return True
#     return False
#
# result = can_edit("admin", True)
# print(result)
#
#
# Create a function called has_permission.
# The function should have one parameter:
# role
# Return True if role is equal to "manager".
# Otherwise, return False.
# Create another function called can_delete_file.
# The function should have two parameters:
# role
# confirmed
# Return True only if:
# has_permission(role) is True
# AND
# confirmed is True.
# Otherwise, return False.
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# role = "manager"
# confirmed = False
#
#
# def has_permission(role):
#     if role == "manager":
#         return True
#     return False
#
# def can_delete_file(role, confirmed):
#     if has_permission(role) and confirmed:
#         return True
#     return False
#
# result = can_delete_file(role="manager", confirmed=False)
# print(result)
#
#
# Create a function called can_enter.
# The function should have two parameters:
# age
# has_ticket
# Return True if:
# age is greater than or equal to 18
# OR
# has_ticket is True.
# Otherwise, return False.
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# age = 15
# has_ticket = True
#
#
# def can_enter(age, has_ticket):
#     if age >= 18 or has_ticket:
#         return True
#     return False
#
# result = can_enter(15, True)
# print(result)
#
#
# Create a function called is_admin.
# The function should have one parameter:
# role
# Return True if role is equal to "admin".
# Otherwise, return False.
# Create another function called can_manage_users.
# The function should have two parameters:
# role
# super_user
# Return True if:
# is_admin(role) is True
# OR
# super_user is True.
# Otherwise, return False.
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# role = "user"
# super_user = True
#
#
# def is_admin(role):
#     if role == "admin":
#         return True
#     return False
#
# def can_manage_users(role, super_user):
#     if is_admin(role) or super_user:
#         return True
#     return False
#
# result = can_manage_users("user", True)
# print(result)
#
#
# Create a function called longest_word.
# The function should have two parameters:
# first_word
# second_word
#
# Return the length of the longer word.
#
# Use the built-in functions:
# len()
# max()
#
# Save the returned value into a variable called result.
# Print result.
#
# Call the function with:
# first_word = "Python"
# second_word = "Cat"
#
#
# def longest_word(first_word, second_word):
#     first_length = len(first_word)
#     second_length = len(second_word)
#     return max(first_length, second_length)
#
# result = longest_word("Python", "Cat")
# print(result)
#
#
# Create a function called word_length.
# The function should have one parameter:
# word
# Return the length of the word.
# Use the built-in function:
# len()
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# word = "Elephant"
#
#
# def word_length(word):
#     return len(word)
# result = word_length("Elephant")
# print(result)
#
#
# Create a function called biggest_number.
# The function should have two parameters:
# first_number
# second_number
# Return the bigger number.
# Use the built-in function:
# max()
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# first_number = 15
# second_number = 40
#
#
# def biggest_number(first_number, second_number):
#     return max(first_number, second_number)
# result = biggest_number(15, 40)
# print(result)
#
#
# Create a function called longest_word.
# The function should have two parameters:
# first_word
# second_word
# Return the length of the longer word.
# Use the built-in functions:
# len()
# max()
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# first_word = "Python"
# second_word = "Cat"
#
#
# def longest_word(first_word, second_word):
#     first_length = len(first_word)
#     second_length = len(second_word)
#     return max(first_length, second_length)
#
# result = longest_word("Python", "Cat")
# print(result)
#
#
# Create a function called shortest_word.
# The function should have two parameters:
# first_word
# second_word
# Return the length of the shorter word.
# Use the built-in functions:
# len()
# min()
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# first_word = "Elephant"
# second_word = "Cat"
#
#
# def shortest_word(first_word, second_word):
#     first_length = len(first_word)
#     second_length = len(second_word)
#     return min(first_length, second_length)
# result = shortest_word("Elephant", "Cat")
# print(result)
#
#
# Create a function called is_integer.
# The function should have one parameter:
# value
# Return the result of isinstance(value, int).
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# value = 100
#
#
# def is_integer(value):
#     return isinstance(value, int)
#
# result = is_integer(100)
# print(result)
#
#
# Create a function called is_string.
# The function should have one parameter:
# value
# Return the result of isinstance(value, str).
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# value = "QA Engineer"
#
#
# def is_string(value):
#     return isinstance(value, str)
# result = is_string("QA Engineer")
# print(result)
#
#
# Create a function called is_boolean.
# The function should have one parameter:
# value
# Return the result of isinstance(value, bool).
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# value = False
#
#
# def is_boolean(value):
#     return isinstance(value, bool)
# result = is_boolean(False)
# print(result)
#
#
# Create a function called longest_number.
# The function should have two parameters:
# first_number
# second_number
# Return the bigger number.
# Use the built-in function:
# max()
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# first_number = 150
# second_number = 85
#
#
# def longest_number(first_number, second_number):
#     return max(first_number, second_number)
#
# result = longest_number(150, 85)
# print(result)
#
#
# Create a function called shortest_word.
# The function should have two parameters:
# first_word
# second_word
# Return the length of the shorter word.
# Use the built-in functions:
# len()
# min()
# Save the returned value into a variable called result.
# Print result.
# Call the function with:
# first_word = "Computer"
# second_word = "Dog"
#
#
# def shortest_word(first_word, second_word):
#    first_word_length = len(first_word)
#    second_word_length = len(second_word)
#    return min(first_word_length, second_word_length)
# result = shortest_word("Computer", "Dog")
# print(result)
#
#
# Create a function called is_employee.
# The function should have one parameter:
# role
# Return True if role is equal to "employee".
# Otherwise, return False.
#
# Create another function called can_enter_office.
# The function should have two parameters:
# role
# has_card
# Return True if:
# is_employee(role) is True
# AND
# has_card is True.
# Otherwise, return False.
#
# Save the returned value into a variable called result.
# Print result.
#
# Call the function with:
# role = "employee"
# has_card = True
#
#
# def is_employee(role):
#     return role == "employee"
#
# def can_enter_office(role, has_card):
#     return is_employee(role) and has_card
#
# result = can_enter_office("employee", True)
# print(result)
#
#
# Create a function called is_manager.
# The function should have one parameter:
# role
# Return True if role is equal to "manager".
# Otherwise, return False.
#
# Create another function called can_open_safe.
# The function should have two parameters:
# role
# has_master_key
# Return True if:
# is_manager(role) is True
# OR
# has_master_key is True.
# Otherwise, return False.
#
# Save the returned value into a variable called result.
# Print result.
#
# Call the function with:
# role = "user"
# has_master_key = True
#
#
# def is_manager(role):
#     return role == "manager"
#
# def can_open_safe(role, has_master_key):
#     return is_manager(role) or has_master_key
#
# result = can_open_safe("user", True)
# print(result)
#
#


















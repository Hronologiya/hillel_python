# # Task: Temperature Checker
# # Create a variable 'temperature' and assign an integer value to it.
# # Write an if-elif-else statement to check the weather:
# # If the temperature is greater than 25, print "It's hot outside".
# # If the temperature is between 10 and 25 (inclusive), print "The weather is nice".
# # If the temperature is less than 10, print "It's cold outside".
#
#
# temperature = 21
#
# if temperature > 25:
#     print("It's hot outside")
# elif 10 <= temperature <= 25:
#     print("The weather is nice")
# else:
#     print("It's cold outside")
#
#
# Task: User Access Level
# Create a variable 'role' and assign it a string value (e.g., "admin", "user", or "guest").
# Write an if-elif-else statement to check the access level:
# If the role is "admin", print "Full access granted".
# If the role is "user", print "Partial access granted".
# For any other role, print "Access denied".
#
#
# role = "admin"
# if role == "admin":
#     print("Full access granted")
# elif role == "user":
#     print("Partial access granted")
# else:
#     print("Access denied")
#
#
# Task: Mower Oil Check
# Create a variable 'oil_level' and assign an integer value to it (from 0 to 100).
# Write an if-elif-else statement to check the oil level before starting the lawn mower:
# If the oil_level is greater than or equal to 70, print "Oil level is good. Ready to mow."
# If the oil_level is between 30 and 69 (inclusive), print "Oil level is low. Consider adding oil soon."
# If the oil_level is less than 30, print "Warning: Oil level critically low! Do not start the engine."
#
#
# oil_level = 50
# if oil_level >=70:
#     print("Oil level is good. Ready to mow.")
# elif 30 <= oil_level <= 69:
#     print("Oil level is low. Consider adding oil soon.")
# else:
#     print("Warning: Oil level critically low! Do not start the engine.")
#
#
# Task: Weekend Discount Check
# Create a variable 'day' and assign it a string with the day of the week (e.g., "Saturday").
# Create a variable 'is_member' and assign it a boolean value (True or False).
# Write an if-else statement using logical operators:
# If the day is "Saturday" OR "Sunday", AND the user is a member (is_member is True),
# print "Special weekend discount applied!".
# In all other cases, print "Regular price".
# Note: Use parentheses to group conditions correctly!
#
#
# day = "Saturday"
# is_member = True
# if (day == "Saturday" or day == "Sunday") and is_member:
#     print("Special weekend discount applied!")
# else:
#     print("Regular price")
#
#
# Task: Login Validator
# Create a variable 'username' and assign it a string value.
# Create a variable 'password' and assign it a string value.
# Create a boolean variable 'bypass_token' and assign it True or False.
# Write an if-else statement using logical operators:
# If the username is "admin" AND the password is "qwerty", OR if bypass_token is True:
# print "Login successful".
# In all other cases, print "Login failed".
# Note: Think carefully about where to put parentheses!
#
#
# username = ""
# password = ""
# bypass_token = True
# if (username == "admin" and password == "qwerty") or bypass_token:
#     print("Login successful")
# else:
#     print("Login failed")
#
#
# Task: Product Purchase Check
# Create a boolean variable 'in_stock' and assign it True or False.
# Create a boolean variable 'is_preorder_available' and assign it True or False.
# Create a boolean variable 'user_has_funds' and assign it True or False.
# Write an if-else statement using logical operators:
# If the product is in stock OR preorder is available, AND the user has funds:
# print "Purchase successful".
# In all other cases, print "Purchase failed".
#
#
# in_stock = True
# is_preorder_available = True
# user_has_funds = True
# if (in_stock or is_preorder_available) and user_has_funds:
#     print("Purchase successful")
# else:
#     print("Purchase failed")
#
#
# Task: Countdown Timer
# Create a variable 'seconds' and set it to 5.
# Write a while loop that runs as long as 'seconds' is greater than 0.
# Inside the loop, print "Time left: " and the value of 'seconds'.
# Decrease the 'seconds' variable by 1 in each iteration.
# Outside the loop, print "Time is up! 🚀"
#
#
# seconds = 5
# while seconds > 0:
#     print("Time left: ", seconds)
#     seconds -= 1
# print("Time is up! 🚀")
#
#
# Task: Skip Even Numbers
# Create a for loop that iterates through numbers from 1 to 10.
# Inside the loop, check if the number is even (divisible by 2).
# If the number is even — use 'continue' to skip it.
# If the number is odd — print "Odd number: " and the value of the number.
#
#
# for number in range(1,11):
#     if number % 2 == 0:
#         continue
#     print("Odd number: ", number)
#
#
# Task: Find the Admin
# Create a list 'users' with values: "guest", "user123", "admin", "moderator", "banned"
# Write a for loop that iterates through the list.
# Inside the loop, print "Checking: " and the current user.
# If the current user equals "admin" — print "Admin found! ✅" and stop the loop.
# If the loop finishes without finding "admin" — print "Admin not found ❌"
#
#
# users = ["guest", "user123", "admin", "moderator", "banned"]
# for user in users:
#     print("Checking: ", user)
#     if user == "admin":
#         print("Admin found!")
#         break
# else:
#     print("Admin not found ❌")


# Task: Password Checker
# Create a variable 'password' and set it to "python123".
# Create a variable 'attempts' and set it to 3.
# Write a while loop that runs as long as 'attempts' is greater than 0.
# Inside the loop, create a variable 'input_password' and set it to "python123".
# If 'input_password' equals 'password' — print "Access granted! ✅" and stop the loop.
# If not — print "Wrong password! Attempts left: " and the value of 'attempts'.
# Decrease 'attempts' by 1 in each iteration.
# Outside the loop, print "Account locked! ❌"
#
#
# password = "python123"
# attempts = 3
# while attempts > 0:
#     input_password = "python123"
#     if input_password == password:
#         print("Access granted! ✅")
#         break
#     else:
#         print("Wrong password! Attempts left: ", attempts)
#     attempts -= 1
# else:
#     print("Account locked! ❌")
#
#
# Task: Print Only Multiples of 3
# Write a for loop that iterates through numbers from 1 to 20.
# Inside the loop, check if the number is NOT a multiple of 3.
# If it is NOT a multiple of 3 — use 'continue' to skip it.
# If it IS a multiple of 3 — print "Multiple of 3: " and the value of the number.
#
#
# for number in range(1,21):
#     if number % 3 != 0:
#         continue
#     print("Multiple of 3: ", number)
#
#
# Task: Server Connection
# Create a variable 'connected' and set it to False.
# Create a variable 'attempts' and set it to 0.
# Write a while loop that runs as long as 'connected' is False.
# Inside the loop, increase 'attempts' by 1.
# Print "Connecting... Attempt: " and the value of 'attempts'.
# If 'attempts' equals 3 — set 'connected' to True.
# Outside the loop, print "Connected successfully! ✅ Attempts: " and the value of 'attempts'.
#
#
# connected = False
# attempts = 0
# while not connected:
#     attempts += 1
#     print(f"Connecting... Attempt: {attempts}")
#     if attempts == 3:
#         connected = True
# print(f"Connected successfully! ✅ Attempts: {attempts}")
#
#
# Task: File Scanner
# Create a list 'files' with values: "image.png", "script.py", "data.csv", "app.py", "notes.txt"
# Write a for loop that iterates through the list.
# Inside the loop, check if the file does NOT end with ".py".
# If it does NOT end with ".py" — use 'continue' to skip it.
# If it ends with ".py" — print "Python file found: " and the file name.
#
#
# files = ["image.png", "script.py", "data.csv", "app.py", "notes.txt"]
# for file in files:
#     if not file.endswith(".py"):
#         continue
#     print(f"Python file found: {file}")
#
#
# Task: Find First Negative Number
# Create a list 'numbers' with values: 5, 12, 8, -3, 7, -1, 4
# Write a for loop that iterates through the list.
# Inside the loop, print "Checking: " and the current number.
# If the number is less than 0 — print "First negative number found: " and the number, then stop the loop.
# If the loop finishes without finding a negative number — print "No negative numbers found ✅"
#
#
# numbers = [5, 12, 8, -3, 7, -1, 4]
# for number in numbers:
#     print(f"Checking:{number}")
#     if number < 0:
#         print(f"First negative numbers found:{number}")
#         break
# else:
#     print(f"No negative number found")
#
#
# Task: Multiplication Table
# Write a for loop that iterates through numbers from 1 to 10 inclusive.
# Inside the loop, print the multiplication table for number 3.
# Format: "3 x " and the current number and " = " and the result.
# Example output: "3 x 1 = 3"
#
#
# for number in range(1, 11):
#     print(f"3 x {number} = {3 * number}")
#
#
# Task: Even Number Sum
# Create a variable 'total' and set it to 0.
# Write a while loop that runs as long as 'total' is less than 50.
# Inside the loop, increase 'total' by 2 in each iteration.
# Print "Current total: " and the value of 'total'.
# Outside the loop, print "Done! Final total: " and the value of 'total'.
#
#
# total = 0
# while total < 50:
#     total += 2
#     print(f"Current total:{total}")
# print(f"Done! Final total:{total}")
#
#
# Task: Count by 3
# Create a variable number and set it to 0.
# Write a while loop that runs while number is less than 18.
# Increase number by 3 in every iteration.
# Print "Current number:" and the value of number.
# After the loop, print "Loop finished!".
#
#
# number = 0
# while number < 18:
#     number += 3
#     print(f"Current number: {number}")
# print(f"Loop finished!")
#
#
# Task: Reach 25
# Create a variable total and set it to 5.
# Write a while loop that runs while total is less than 25.
# Increase total by 5 in every iteration.
# Print "Total:" and the value of total.
# After the loop, print "Finished!".
#
#
# total = 5
# while total < 25:
#     total += 5
#     print(f"Total: {total}")
# print(f"Finished!")
#
#
# Task: Count by 4
# Create a for loop using range().
# Start from 4 and stop at 21.
# Increase by 4 each iteration.
# Print "Number:" and the current number.
# After the loop, print "Done!".
#
# for number in range(4, 22):
#     if number % 4 == 0:
#         print(f"Number: {number}")
# print(f"Done!")
#
#
# Task: Skip Number 4
# Create a for loop using range from 1 to 8.
# If the number is 4, skip it using continue.
# Print "Number:" and the current number.
# After the loop, print "Done!".
#
# for number in range(1,9):
#     if number != 4:
#         print(f"Number: {number}")
#         continue
# print(f"Done!")

# Task: Skip Even Numbers
# Create a for loop using range from 1 to 10.
# If the number is even, skip it using continue.
# Print "Odd number:" and the current number.
# After the loop, print "Finished!".
#
#
# for number in range(1,11):
#     if number % 2 != 0:
#         print(f"Odd number: {number}")
#         continue
# print("Finished!")
#
#
# Task: Stop at 7
# Create a for loop using range from 1 to 10.
# Print each number.
# If the number is 7:
#   print "Found 7!"
#   stop the loop using break.
# After the loop, print "Finished!".
#
#
# for number in range(1,11):
#     print(f"{number}")
#     if number == 7:
#         print(f"Found 7!")
#         break
# print("Finished!")
#
#
# Task: Stop at 5
# Create a for loop using range from 1 to 10.
# If the number is 5:
#   print "Target found!"
#   stop the loop using break.
# Print "Current number:" and the current number for all other iterations.
# After the loop, print "Loop ended!".
#
#
# for number in range(1,11):
#     if number == 5:
#         print(f"Target found!")
#         break
#     else:
#         print(f"Current number: {number}")
# print(f"Loop ended!")
#
#
# Task: Find First Negative Number
# Create a list 'numbers' with values:
# 8, 15, 22, -4, 10, -1, 7
#
# Write a for loop that iterates through the list.
#
# Inside the loop:
# Print "Checking:" and the current number.
#
# If the number is less than 0:
# Print "Negative number found:" and the number.
# Stop the loop using break.
#
# If the loop finishes without finding a negative number:
# Print "No negative numbers found"
#
#
# numbers = [8, 15, 22, -4, 10, -1, 7]
# for number in numbers:
#     print(f"Checking: {number}")
#     if number < 0:
#         print(f"Negative number found: {number}")
#         break
# else:
#     print(f"No negative numbers found")
#
#
# Task: Find First Number Greater Than 50
# Create a list 'numbers' with values:
# 12, -5, 34, 0, 67, 45, 80
#
# Write a for loop that iterates through the list.
#
# If the current number is negative:
# print "Skipping negative number"
# and skip this iteration using continue.
#
# Otherwise print:
# "Checking: " and the current number.
#
# If the number is greater than 50:
# print "Found number greater than 50: "
# and the number.
# Then stop the loop using break.
#
# After the loop print:
# "Search finished"
#
#
# numbers = [12, -5, 34, 0, 67, 45, 80]
# for number in numbers:
#     if number < 0:
#         print("Skipping negative number")
#         continue
#
#     print(f"Checking: {number}")
#     if number > 50:
#         print(f"Found number greater than 50: {number}")
#         break
# print("Search finished")
#
#
# Task: Find First Even Number Greater Than 20
# Create a list 'numbers' with values:
# 3, -2, 15, 21, 18, 24, 30
#
# Write a for loop that iterates through the list.
#
# If the current number is negative:
# print "Skipping negative number"
# and skip the iteration using continue.
#
# Print "Checking:" and the current number.
#
# If the number is even and greater than 20:
# print "Target found:" and the number.
# Then stop the loop using break.
#
# After the loop print:
# "Search completed"
#
#
# numbers = [3, -2, 15, 21, 18, 24, 30]
# for number in numbers:
#     if number < 0:
#         print("Skipping negative number")
#         continue
#     print(f"Checking: {number}")
#     if number % 2 == 0 and number > 20:
#         print(f"Target found: {number}")
#         break
# print("Search completed")
#
#
# Task: Find First Failed Test
# Create a list 'test_results' with values:
# "PASSED", "PASSED", "SKIPPED", "PASSED", "FAILED", "PASSED"
#
# Write a for loop that iterates through the list.
#
# If the current result is "SKIPPED":
# print "Skipping test"
# and skip the iteration using continue.
#
# Print "Checking:" and the current result.
#
# If the result is "FAILED":
# print "Failed test found"
# and stop the loop using break.
#
# After the loop print:
# "Test run finished"
#
#
# test_results = ["PASSED", "PASSED", "SKIPPED", "PASSED", "FAILED", "PASSED"]
# for result in test_results:
#     if result == "SKIPPED":
#         print("Skipping test")
#         continue
#
#     print(f"Checking: {result}")
#     if result == "FAILED":
#         print("Failed test found")
#         break
# print("Test run finished")
#
#
# Task: Find First Critical Error
# Create a list 'logs' with values:
# "INFO", "WARNING", "SKIPPED", "ERROR", "CRITICAL", "INFO"
#
# Write a for loop that iterates through the list.
#
# If the current log is "SKIPPED":
# print "Skipping log"
# and skip the iteration using continue.
#
# Print "Checking log:" and the current log.
#
# If the log is "ERROR" or "CRITICAL":
# print "Error detected"
#
# If the log is "CRITICAL":
# print "Critical error found"
# and stop the loop using break.
#
# After the loop print:
# "Log analysis finished"
#
# logs = ["INFO", "WARNING", "SKIPPED", "ERROR", "CRITICAL", "INFO"]
# for log in logs:
#     if log == "SKIPPED":
#         print("Skipping log")
#         continue
#
#     print(f"Checking log: {log}")
#     if log == "ERROR" or log == "CRITICAL":
#         print("Error detected")
#
#     if log == "CRITICAL":
#         print("Critical error found")
#         break
# print("Log analysis finished")
#
#
# Task: Process User Accounts
# Create a list 'users' with values:
# "active", "blocked", "active", "admin", "active", "deleted"
#
# Write a for loop that iterates through the list.
#
# If the current user status is "blocked":
# print "Skipping blocked user"
# and skip the iteration using continue.
#
# Print "Processing:" and the current status.
#
# If the status is "admin":
# print "Admin account found"
#
# If the status is "deleted":
# print "Deleted account found"
# and stop the loop using break.
#
# After the loop print:
# "User scan completed"
#
#
# users = ["active", "blocked", "active", "admin", "active", "deleted"]
# for user in users:
#     if user == "blocked":
#         print("Skipping blocked user")
#         continue
#
#     print(f"Processing: {user}")
#
#     if user == "admin":
#         print("Admin account found")
#
#     if user == "deleted":
#         print("Deleted account found")
#         break
#
# print("User scan completed")
#
#
# Task: Find First Valid Score
# Create a list 'scores' with values:
# -5, 0, 15, 22, 48, 75, 110, 60
#
# Write a for loop that iterates through the list.
#
# If the score is less than 0:
# print "Invalid score"
# and skip the iteration using continue.
#
# Print "Checking score:" and the score.
#
# If the score is greater than 50 and less than 100:
# print "Valid score found:" and the score.
# Then stop the loop using break.
#
# After the loop print:
# "Score analysis completed"
#
#
# scores = [-5, 0, 15, 22, 48, 75, 110, 60]
# for score in scores:
#     if score < 0:
#         print("Invalid score")
#         continue
#
#     print(f"Checking score: {score}")
#
#     if 50 < score < 100:
#         print(f"Valid score found: {score}")
#         break
# print("Score analysis completed")
#
#
# Task: Analyze API Responses
# Create a list 'responses' with values:
# 200, 200, 404, 500, 200, 403
#
# Write a for loop that iterates through the list.
#
# If the response code is 404:
# print "Page not found"
# and skip further processing of this iteration.
#
# Print "Processing response:" and the response code.
#
# If the response code is 500:
# print "Server error detected"
# and stop the loop.
#
# After the loop print:
# "Response analysis completed"
#
#
# responses = [200, 200, 404, 500, 200, 403]
# for response in responses:
#     if response == 404:
#         print("Page not found")
#         continue
#
#     print(f"Processing response: {response}")
#
#     if response == 500:
#         print("Server error detected")
#         break
# print("Response analysis completed")
#
#
# Task: Analyze Login Attempts
# Create a list '"attempts"' with values:
# "SUCCESS", "FAILED", "BLOCKED", "FAILED", "ADMIN", "SUCCESS"
#
# Write a for loop that iterates through the list.
#
# If the current attempt is "BLOCKED":
# print "Blocked user detected"
# and skip the iteration using continue.
#
# Print "Checking attempt:" and the current attempt.
#
# If the attempt is "FAILED" or "ADMIN":
# print "Attention required"
#
# If the attempt is "ADMIN":
# print "Admin login detected"
# and stop the loop using break.
#
# After the loop print:
# "Login analysis completed"
#
#
# attempts = ["SUCCESS", "FAILED", "BLOCKED", "FAILED", "ADMIN", "SUCCESS"]
# for status in attempts:
#     if status == "BLOCKED":
#         print("Blocked user detected")
#         continue
#
#     print(f"Checking attempt: {status}")
#
#     if status == "FAILED" or status == "ADMIN":
#         print("Attention required")
#
#     if status == "ADMIN":
#         print("Admin login detected")
#         break
#
# print("Login analysis completed")
#
#
# Task: Analyze Orders
# Create a list 'orders' with values:
# "NEW", "CANCELLED", "PROCESSING", "VIP", "SHIPPED", "ERROR"
#
# Write a for loop that iterates through the list.
#
# If the current order status is "CANCELLED":
# print "Skipping cancelled order"
# and skip the iteration using continue.
#
# Print "Checking order:" and the current status.
#
# If the status is "VIP" or "ERROR":
# print "Priority attention needed"
#
# If the status is "ERROR":
# print "Order processing stopped"
# and stop the loop using break.
#
# After the loop print:
# "Order analysis completed"
#
#
# orders = ["NEW", "CANCELLED", "PROCESSING", "VIP", "SHIPPED", "ERROR"]
# for status in orders:
#     if status == "CANCELLED":
#         print("Skipping cancelled order")
#         continue
#
#     print(f"Checking order: {status}")
#
#     if status == "VIP" or status == "ERROR":
#         print("Priority attention needed")
#
#     if status == "ERROR":
#         print("Order processing stopped")
#         break
# print("Order analysis completed")
#
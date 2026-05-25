# # 1. Create a tuple named 'db_config' with the following values: "localhost", 5432, "admin", "password123"
# # 2. Print the whole tuple to the console.
# # 3. Access and print only the port number (5432) using its index.
# # 4. Try to change the port number to 8080 and observe what happens (comment out the error line after wards).
# from enum import unique
#
# db_config = ("localhost", 5432, "admin", "password")
# print(db_config)
# port_index = db_config.index(5432)
# print(f"Port index: {port_index}")
# print(db_config[1])
# # db_config[1] = 8080
#
# # Create a list named 'failed_tests' containing two strings: "test_login" and "test_cart".
# # Add a new test "test_payment" to the end of the list using the append() method.
# # Remove "test_login" from the list using the remove() method.
# # Print the final list to the console.
#
#
# failed_tests = ["test_login", "test_cart"]
# failed_tests.append("test_payment")
# failed_tests.remove("test_login")
# print(failed_tests)
#
#
# # 1. Create a set named 'ui_elements' with the strings: "button", "input", "link".
# # 2. Add a new element "checkbox" to the 'ui_elements' set using the add() method.
# # 3. Create a second set named 'api_elements' with the strings: "link", "dropdown".
# # 4. Combine both sets into a new set named 'all_elements' using the union() method or '|' operator.
# # 5. Print the 'all_elements' set to the console.
#
#
# ui_elements = {"button", "input", "link"}
# ui_elements.add("checkbox")
# api_elements = {"link", "dropdown"}
# all_elements = ui_elements.union(api_elements)
# print(all_elements)
#
#
# # Create a dictionary called server response with keys status code and message.
# # Assign 200 to status code and OK to message.
# # Print the dictionary to the console.
#
#
# server_response = {"status_code" : 200, "message" : "OK"}
# print(server_response)
#
#
# # Using the dictionary from the previous task, print only the message value.
# # Add a new key called response time with a value of 0.5.
# # Print the updated dictionary.
#
#
# print(server_response["message"])
# server_response["response_time"] = 0.5
# print(server_response)
#
#
# # Create a dictionary called test user with keys username and email.
# # Assign "qa_ninja" to username and "qa@test.com" to email.
# # Print only the email value to the console.
# # Add a new key called is active with a value of True.
# # Print the updated dictionary.
#
#
# test_user = {"username" : "qa_ninja" , "email" : "qa@test.com"}
# print(test_user["email"])
# test_user["is_active"] = True
# print(test_user)
#
#
# # Create a dictionary called app config with key environment assigned to dev.
# # Change the value of environment key to prod.
# # Print the dictionary to the console.
#
#
# app_config = {"environment" : "dev"}
# app_config["environment"] = "prod"
# print(app_config)
#
#
# # Create a list named execution times with the numbers: 5.2, 1.1, 3.4, 0.9.
# # Sort the list in ascending order.
# # Print the sorted list to the console.
#
#
# execution_times = [5.2, 1.1, 3.4, 0.9]
# execution_times.sort()
# print(execution_times)
#
#
# # Create a list named error codes with the numbers: 404, 500, 401, 403.
# # Sort the list in descending order.
# # Print the sorted list to the console.
#
#
# error_codes = [404, 500, 401, 403]
# error_codes.sort(reverse=True)
# print(error_codes)
#
#
# # Create a list named test statuses containing the strings passed, failed, skipped, blocked.
# # Sort the list alphabetically.
# # Print the sorted list to the console.
#
#
# test_statuses = ["passed", "failed", "skipped", "blocked"]
# test_statuses.sort()
# print(test_statuses)
#
#
# # Create a variable company name and assign the string Google to it.
# # Convert this string into a list and store it in a variable called letters list.
# # Print letters list to the console.
#
# company_name = "Google"
# letters_list = list(company_name)
# print(letters_list)
#
#
# # Create a tuple named server ports containing the numbers 80, 443, and 8080.
# # Convert this tuple into a list and store it in a variable named active ports.
# # Print the active ports list to the console.
#
#
# server_ports = (80, 443, 8080)
# active_ports = list(server_ports)
# print(active_ports)
#
#
# # Create a set named unique browsers containing the strings Chrome, Firefox, and Safari.
# # Convert this set into a list and store it in a variable named browsers list.
# # Print browsers list to the console.
#
#
# unique_browsers = {"Chrome", "Firefox", "Safari"}
# browsers_list = list(unique_browsers)
# print(browsers_list)
#
#
# # Create a list containing numbers from 1 to 5.
# # Use list comprehension to create a new list where each number is multiplied by itself.
# # Print the new list to the console.
#
#
# base_numbers = [1,2,3,4,5]
# squared_numbers = [n * n for n in base_numbers]
# print(squared_numbers)
#
#
# # Create a list containing the strings get, post, put, delete.
# # Use list comprehension to create a new list where each string is converted to uppercase using the upper() method.
# # Print the new list to the console.
#
#
# http_methods = ["get", "post", "put" , "delete"]
# upper_methods = [method.upper() for method in http_methods]
# print(upper_methods)
#
#
# # Create a list containing numbers from 1 to 10.
# # Use list comprehension to create a new list containing only the even numbers from the first list.
# # Print the new list to the console.
#
#
# old_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [n for n in old_numbers if n % 2 == 0]
# print(even_numbers)
#
#
# # Create a set named run1_failures containing the numbers 101, 105, 108.
# # Create a set named run2_failures containing the numbers 105, 108, 110.
# # Find the intersection of both sets to see which tests failed in both runs, and store it in common_failures.
# # Print common_failures to the console.
#
#
# run1_failures = {101, 105, 108}
# run2_failures = {105, 108, 110}
# common_failures = run1_failures & run2_failures
# print(common_failures)
#
#
# # Create a set named expected elements containing the strings header, footer, sidebar, banner.
# # Create a set named actual elements containing the strings header, footer, sidebar.
# # Find the difference to see which elements are missing from the actual elements, and store it in missing elements.
# # Print missing elements to the console.
#
#
# expected_elements = {"header", "footer", "sidebar", "banner"}
# actual_elements = {"header", "footer", "sidebar"}
# missing_elements = expected_elements - actual_elements
# print(missing_elements)
#
#
# # Create a set named backend tags containing the strings smoke, regression, auth.
# # Create a set named frontend tags containing the strings smoke, ui, regression.
# # Find the union of both sets to get all unique tags, and store it in all tags.
# # Print all tags to the console.
#
#
# backend_tags = {"smoke", "regression", "auth"}
# frontend_tags = {"smoke", "ui", "regression"}
# all_tags = backend_tags | frontend_tags
# print(all_tags)
#
#
# # Create a list named raw ids containing the numbers 10, 20, 10, 30, 20.
# # Convert this list into a set to remove duplicates and store it in unique ids.
# # Print unique_ids to the console.
#
#
# raw_ids = [10, 20, 10, 30, 20]
# unique_ids = set(raw_ids)
# print(unique_ids)
#
#
# # Create a tuple named status_codes containing the numbers 200, 404, 200, 500, 404.
# # Convert this tuple into a set to keep only unique codes and store it in unique_codes.
# # Print unique_codes to the console.
#
#
# status_codes = (200, 404, 200, 500, 404)
# unique_codes = set(status_codes)
# print(unique_codes)
#
#
# # Create a variable named error_message and assign the string Timeout error to it.
# # Convert this string into a set to find all unique characters used in the message, and store it in unique_chars.
# # Print unique_chars to the console.
#
#
# error_message = "Timeout error"
# unique_chars = set(error_message)
# print(unique_chars)
#
#
# # Create a list named raw_tags containing the strings UI, API, ui, Backend.
# # Use set comprehension to create a new set where each tag is converted to lowercase using the lower() method.
# # Print the new set to the console.
#
#
# raw_tags = ["UI", "API", "ui", "Backend"]
# lower_tags = {tag.lower() for tag in raw_tags}
# print(lower_tags)
#
#
# # Create a list named raw_numbers containing the numbers -2, -1, 0, 1, 2.
# # Use set comprehension to create a new set containing the squares of these numbers (n * n).
# # Print the new set to the console.
#
#
# raw_numbers = [-2, -1, 0, 1, 2]
# squares_number = {n * n for n in raw_numbers}
# print(squares_number)
#
#
# # Create a dictionary named api_response with the key status assigned to the number 200.
# # Use the .get() method to find the value of a key named error_message, and store it in a variable named error.
# # Print the error variable to the console.
#
# api_response = {"status" : 200}
# error = api_response.get("error_message")
# print(error)
#
#
# # Create a dictionary named user_data with the keys username and role.
# # Assign the value admin to username and qa_engineer to role.
# # Use the .keys() method to get all the keys from the dictionary and store them in a variable called dict_keys.
# # Print dict_keys to the console.
#
# user_data = {"username" : "admin", "role" : "qa_engineer"}
# dict_keys = user_data.keys()
# print(dict_keys)
# from pyexpat import features

# Create a dictionary named test_results with the keys test1 and test2.
# Assign the value passed to test1 and failed to test2.
# Use the .values() method to get all the values from the dictionary and store them in a variable called dict_values.
# Print dict_values to the console.

# test_results = {"test1" : "passed", "test2" : "failed"}
# dict_values = test_results.values()
# print(dict_values)


# Create a list of tuples named user_roles containing the pairs ("admin", 1) and ("user", 2).
# Convert this list into a dictionary using the dict() function and store it in roles_dict.
# Print roles_dict to the console.

# user_roles = [("admin", 1), ("user", 2)]
# roles_dict = dict(user_roles)
# print(roles_dict)


# Create a list named keys_list containing the strings "env" and "db".
# Create a list named values_list containing the strings "prod" and "postgres".
# Use dict() and zip() functions to combine them into a dictionary, and store it in config_dict.
# Print config_dict to the console.

# keys_list = ["env", "db"]
# values_list = ["prod", "postgres"]
# config_dict = dict(zip(keys_list, values_list))
# print(config_dict)


# Create a dictionary using the dict() function by passing keyword arguments.
# Assign the value "John" to the key first_name and "Doe" to the key last_name.
# Store the result in a variable named user_profile.
# Print user_profile to the console.


# user_profile = dict(first_name = "John", last_name = "Doe")
# print(user_profile)


# Create a list named features containing the strings "auth", "checkout", "search".
# Use dictionary comprehension to create a new dictionary named feature_status.
# In this dictionary, each feature from the list should be a key, and its value should be the string "pending".
# Print feature_status to the console.

# features = ["auth", "checkout", "search"]
# feature_status = {feature : "pending" for feature in features}
# print(feature_status)


# Create a list named test_names containing the strings "login", "api", "ui".
# Use dictionary comprehension to create a new dictionary named name_lengths.
# In this dictionary, each name from the list should be a key, and its length (using the len() function) should be the value.
# Print name_lengths to the console.
#
#
# # test_names = ["login", "api", "ui"]
# # name_lengths = {name : len(name) for name in test_names}
# # print(name_lengths)
#
#
# # Create a list named status_codes containing the numbers 200, 404, 500, 201.
# # Use dictionary comprehension to create a new dictionary named error_statuses.
# # Make each code the key and the string "error" the value, but ONLY include codes that are greater than or equal to 400.
# # Print error_statuses to the console.
#
# # status_codes = [200, 404, 500, 201]
# # error_statuses = {code : "error" for code in status_codes if code >= 400}
# # print(error_statuses)
#
#
# # Task: Filter e-commerce products by criteria
# # We have product_data where the key is the product ID.
# # The value is a tuple containing: (product_name, rating, price, in_stock).
# # We have a tuple named search_filter: (min_rating, max_price, should_be_in_stock)
# # Write code that filters products matching ALL criteria from search_filter.
# # Sort the matching products by rating in descending order (from highest to lowest).
# # Print all found elements.
#
# product_data = {
#     'p101': ('Laptop Lenovo', 4.5, 25000, True),
#     'p102': ('Mouse Logitech', 4.8, 1200, True),
#     'p103': ('Keyboard Razer', 4.2, 3500, False),
#     'p104': ('Monitor Dell', 4.9, 15000, True),
#     'p105': ('Headphones Sony', 4.1, 4000, True),
#     'p106': ('Webcam Logitech', 4.6, 2800, False),
#     'p107': ('USB Hub', 4.0, 800, True),
#     'p108': ('Laptop Apple', 4.9, 55000, True),
#     'p109': ('Mouse Apple', 4.3, 4500, True)
# }
#
# search_filter = (4.4, 20000, True)
#
# filtered_products = []
# for product_id, product_info in product_data.items():
#     if (product_info[1] >= search_filter[0]
#             and product_info[2] <= search_filter[1]
#             and product_info[3] == search_filter[2]):
#         filtered_products.append((product_info[1], product_info[0]))
# filtered_products.sort(reverse=True)
# print(filtered_products)
#
#
#
# # Task: Analyze failed tests from execution logs
# # test_logs contains data where the key is the test ID.
# # The value is a tuple: (test_name, module_name, execution_time_seconds, status).
# # We need to find tests that belong to the "checkout" module, failed ("FAILED"), and took strictly more than 3 seconds to execute.
# # Write code to filter these tests.
# # Store them in a list as tuples: (execution_time_seconds, test_name).
# # Sort the results by execution time in descending order (longest execution first).
# # Print the results.
#
# test_logs = {
#     't_01': ('test_login_valid', 'auth', 1.2, 'PASSED'),
#     't_02': ('test_payment_visa', 'checkout', 4.5, 'FAILED'),
#     't_03': ('test_cart_add', 'cart', 2.1, 'PASSED'),
#     't_04': ('test_payment_mastercard', 'checkout', 5.8, 'FAILED'),
#     't_05': ('test_checkout_guest', 'checkout', 1.5, 'PASSED'),
#     't_06': ('test_discount_code', 'checkout', 3.0, 'FAILED'),
#     't_07': ('test_search_filter', 'search', 6.2, 'FAILED'),
#     't_08': ('test_payment_paypal', 'checkout', 7.1, 'FAILED'),
#     't_09': ('test_password_reset', 'auth', 2.5, 'FAILED')
# }
#
# failed_test_check = []
# for test_id, test_info in test_logs.items():
#     if test_info[1] == "checkout" and test_info[3] == "FAILED" and test_info[2] > 3:
#         failed_test_check.append((test_info[2], test_info[0]))
# failed_test_check.sort(reverse=True)
# print(failed_test_check)
#
#
# # Task: Filter inactive admin users from API response
# # users_api_response is a list of dictionaries.
# # We need to find users who:
# # 1. Have the role "admin"
# # 2. Are active (is_active == True)
# # 3. Have been offline for strictly more than 30 days (days_offline > 30)
# #
# # Write a loop to filter these users.
# # Store the result in a new list as tuples: (days_offline, user_id).
# # Sort the list in descending order by days_offline (longest offline first).
# # Print the final list.
#
# users_api_response = [
#     {'user_id': 101, 'role': 'user', 'is_active': True, 'days_offline': 5},
#     {'user_id': 102, 'role': 'admin', 'is_active': True, 'days_offline': 45},
#     {'user_id': 103, 'role': 'admin', 'is_active': False, 'days_offline': 60},
#     {'user_id': 104, 'role': 'manager', 'is_active': True, 'days_offline': 12},
#     {'user_id': 105, 'role': 'admin', 'is_active': True, 'days_offline': 32},
#     {'user_id': 106, 'role': 'user', 'is_active': True, 'days_offline': 1},
#     {'user_id': 107, 'role': 'admin', 'is_active': True, 'days_offline': 15}
# ]
#
# filtered_admins = []
# for user in users_api_response:
#     if user['role'] == 'admin' and user['is_active'] == True and user['days_offline'] > 30:
#         filtered_admins.append((user['days_offline'], user['user_id']))
# filtered_admins.sort(reverse=True)
# print(filtered_admins)

# Task: User Data Processing
# We have a raw string from a database:
# user_record = "ID_5402_AGENT_SMITH_STATUS_ACTIVE"

# 1. Using slicing, extract the word "AGENT" and print it.
# 2. Using slicing, extract the ID number "5402" and print it.
# 3. Using indexing, print only the very last letter of the whole string.
# 4. Using slicing with a step, print every second character of the word "SMITH"
#    (Hint: first slice "SMITH", then apply step 2).

user_record = "ID_5402_AGENT_SMITH_STATUS_ACTIVE"
print(user_record[8:13])
print(user_record[3:7])
print(user_record[-1])
print(user_record[14:19:2])

# Task 2: Split and Join
# 1. Split the path by "/"
file_path = "documents/projects/test_cases/login_test.py"
part = file_path.split("/")
print(part[-1])

# 2. Join the list into a string
words = ["QA", "Automation", "Python"]
sentence = "_".join(words)
print(sentence)

# Task 3: User Data Reformatting
# 1. We have a string from a form: raw_user = "Ivan;Ivanov;30;QA_Engineer"
# 2. Split this string into a list using ";" as a separator. Print the list.
# 3. Create a new variable 'full_name' by joining the first element
#    and the second element of your list using a space " " as a separator.
#    Print 'full_name' (it should be "Ivan Ivanov").
# 4. Take the whole list and join all elements into a string using " | "
#    as a separator. Print the final string.

raw_user = "Ivan;Ivanov;30;QA_Engineer"
list_using = raw_user.split(";")
print(list_using[-1])
full_name = " ".join(list_using[:2])
print(full_name)
new_list = " | ".join(list_using)
print(new_list)


# Task 4: URL Parsing
# 1. We have a test URL: url = "https://mysite.com/catalog/shoes/size-42"
# 2. Split the URL by the "/" character. Print the resulting list.
# 3. From the list, extract the last element ("size-42") and store it in a variable 'item'.
# 4. Split the 'item' variable by the "-" character.
#    Print the second element of this new list (it should be "42").

url = "https://mysite.com/catalog/shoes/size-42"
url_part = url.split("/")
print(url_part)
item = url_part[-1]
print(item)
item_separated = item.split("-")
print(item_separated[-1])


# Task 5: Log Tagging
# 1. We have a list of test tags: tags = ["Smoke", "Regression", "UI", "Sprint-5"]
# 2. Join these tags into a single string where they are separated by a comma and a space ", ".
#    Store this in a variable 'report_tags' and print it.
# 3. Create another string 'header_tags' where the same tags are joined by a hash symbol "#".
#    The result should look like: "Smoke#Regression#UI#Sprint-5". Print it.

tags = ["Smoke", "Regression", "UI", "Sprint-5"]
report_tags = ", ".join(tags)
print(report_tags)
header_tags = "#".join(tags)
print(header_tags)


# Task: Data Cleaning and Formatting
# 1. We have a messy string from a log file:
#    raw_data = "user:admin | ip:192.168.1.1 | session:active | code:200"
#
# 2. Split this string by " | " to get a list of segments. Print this list.
# 3. From the list, take the first element ("user:admin") and
#    split it by ":" to get only the name "admin".
#    Store it in a variable 'user_name' and print it.
# 4. From the list, take the second element ("ip:192.168.1.1") and
#    split it by ":" to get only the IP address.
#    Store it in a variable 'ip_address' and print it.
# 5. Create a new list called 'result_list' that contains only
#    your 'user_name' and 'ip_address'.
# 6. Join this 'result_list' into a string using " -> " as a separator.
#    Print the final string (it should look like: "admin -> 192.168.1.1").

raw_data = "user:admin | ip:192.168.1.1 | session:active | code:200"
new_data_list = raw_data.split(" | ")
print(new_data_list)
user_parts = new_data_list[0].split(":")
user_name = user_parts[1]
print(user_name)

ip_parts = new_data_list[1].split(":")
ip_address = ip_parts[1]
print(ip_address)

result_list = [user_name, ip_address]
final_string = " -> ".join(result_list)
print(final_string)


# Task 7: Domain and User Analysis
# 1. We have a list of emails: emails = ["admin@google.com", "test@apple.com", "dev@amazon.com"]
# 2. Take the FIRST email from the list.
# 3. Split this email by "@" to get the username and the domain.
# 4. Print the username (the part before @).
# 5. Print the domain (the part after @).
# 6. Take all emails from the 'emails' list and join them into one string
#    separated by a semicolon and a space "; ". Print the result.

emails = ["admin@google.com", "test@apple.com", "dev@amazon.com"]
first_email = emails[0]
separated_email = first_email.split("@")
print(separated_email[0])
print(separated_email[1])
all_emails = "; ".join(emails)
print(all_emails)


# Task 8: Data Extraction from Web URL
# 1. We have a search URL: web_url = "https://myshop.com/search?product=iphone&color=black&storage=256"
# 2. First, split the URL by the "?" character to separate the base URL from the parameters.
#    Print the second part (the parameters: "product=iphone&color=black&storage=256").
# 3. Take those parameters and split them by the "&" character to get a list of settings.
#    Store it in 'settings_list' and print it.
# 4. From 'settings_list', extract the first element ("product=iphone"),
#    split it by "=", and print only the value "iphone".
# 5. Join all elements from 'settings_list' into a new string using " | "
#    as a separator. Print the result.

web_url = "https://myshop.com/search?product=iphone&color=black&storage=256"
web_url_first_part = web_url.split("?")
print(web_url_first_part[1])
settings_list_first = web_url_first_part[1].split("&")
print(settings_list_first)
settings_list_second = settings_list_first[0].split("=")
print(settings_list_second[1])
settings_list_final = " | ".join(settings_list_first)
print(settings_list_final)


# Task 9: Log Data Formatting
# 1. We have three separate variables:
#    timestamp = "2026-02-19"
#    status = "SUCCESS"
#    action = "UserLogin"
#
# 2. Create a list called 'log_data' and put these three variables into it.
# 3. Join the elements of 'log_data' into a single string using a hyphen "-"
#    as a separator. Print this string.
# 4. Take the final string from step 3 and split it back into a list
#    using the same hyphen "-". Print this new list.

timestamp = "2026-02-19"
status = "SUCCESS"
action = "UserLogin"
log_data = [timestamp, status, action]
log_string = "-".join(log_data)
print(log_string)
log_list = log_string.split("-")
print(log_list)


# Task 10: The Ultimate QA Reporter
# 1. We have a list of test results:
#    results = ["login:passed", "checkout:failed", "payment:passed"]
#
# 2. You need to create a clean report. First, join all elements
#    into one string using a " | " separator. Print this string.
# 3. Now, imagine you need to replace all "passed" with "OK"
#    and all "failed" with "ERROR" in this string.
#    Hint: use .replace() twice. Print the new string.
# 4. Finally, split this new string by " | " to get a list again.
#    Print the final list.

results = ["login:passed", "checkout:failed", "payment:passed"]
clean_report = " | ".join(results)
print(clean_report)
report_string_first = clean_report.replace("passed", "OK")
report_string_second = report_string_first.replace("failed", "ERROR")
print(report_string_second)
final_list = report_string_second.split(" | ")
print(final_list)


# Task 11: Security Masking and Validation
# 1. We have a sensitive string:
#    card_number = "4444-5555-6666-7777"
#
# 2. Use .replace() to hide the numbers. Replace all hyphens "-" with stars "*".
#    Print the result.
# 3. Check if the original 'card_number' starts with "4444".
#    Print the result (it should be True or False).
# 4. Check if the original 'card_number' ends with "8888".
#    Print the result.

card_number = "4444-5555-6666-7777"
card_number_with_stars = card_number.replace("-", "*")
print(card_number_with_stars)
card_number_check = card_number.startswith("4444")
print(card_number_check)
card_number_check_original = card_number.endswith("8888")
print(card_number_check_original)


# Task 12: Searching for Errors in Logs
# 1. We have a log message:
#    log_entry = "2026-02-19 14:00:05 - ERROR - Database connection failed"
#
# 2. Use .find() to locate the word "ERROR".
#    Print the index where it starts.
# 3. Use .find() to look for the word "SUCCESS".
#    Print the result (it should be -1).
# 4. Use .replace() to change "ERROR" to "WARNING".
#    Print the updated log entry.

log_entry = "2026-02-19 14:00:05 - ERROR - Database connection failed"
log_entry_search_first = log_entry.find("ERROR")
print(log_entry_search_first)
log_entry_search_second = log_entry.find("SUCCESS")
print(log_entry_search_second)
log_entry_change = log_entry.replace("ERROR", "WARNING")
print(log_entry_change)


# Task13 : Formatting and Validating File Names
# 1. We have a file name:
#    file_name = "report_2026_final.PDF"
#
# 2. Check if the file name ends with ".PDF".
#    Print the result.
# 3. Use .replace() to change the extension from ".PDF" to ".txt".
#    Store it in 'new_file_name' and print it.
# 4. In the 'new_file_name', find the position of the first underscore "_".
#    Print the index.

file_name = "report_2026_final.PDF"
file_name_ends = file_name.endswith(".PDF")
print(file_name_ends)
new_file_name = file_name.replace(".PDF", ".txt")
print(new_file_name)
new_file_name_search = new_file_name.find("_")
print(new_file_name_search)


# Task 14: URL Protocol and Domain Check
# 1. We have a website address:
#    site_url = "http://dev-server.com/login"
#
# 2. Security check: verify if the URL starts with "https".
#    Print the result (should be False).
# 3. Use .replace() to "upgrade" the connection:
#    change "http" to "https". Print the new URL.
# 4. Use .find() to see if the domain contains the word "dev".
#    Print the index.

site_url = "http://dev-server.com/login"
security_check = site_url.startswith("https")
print(security_check)
connection_change = site_url.replace("http", "https")
print(connection_change)
domain_contains = site_url.find("dev")
print(domain_contains)


# Task 15: Clean Data Entry
# 1. We have a username from a form:
#    user_input = "ID_user_777"
#
# 2. Use .startswith() to check if the name begins with "ID_".
#    Print the result.
# 3. Use .replace() to remove "ID_" (replace it with an empty string "").
#    Store it in 'clean_name' and print it.
# 4. In 'clean_name', find the position of the number "7".
#    Print the index.

user_input = "ID_user_777"
user_name_check = user_input.startswith("ID_")
print(user_name_check)
clean_name = user_input.replace("ID_","")
print(clean_name)
clean_name_index_search = clean_name.find("7")
print(clean_name_index_search)


# Task 16: Normalized Search Term
# 1. We have a search query from a user:
#    raw_query = "iPhOnE 15 Pro"
#
# 2. Check if the query is already in lowercase.
#    Print the result.
# 3. Create a new variable 'normalized_query' by converting
#    'raw_query' to all lowercase letters. Print it.
# 4. Check if 'normalized_query' is now in lowercase.
#    Print the result.
# 5. Use .title() on 'normalized_query' to make it look
#    like a proper product name. Print it.

raw_query = "iPhOnE 15 Pro"
print(raw_query.islower())
normalized_query = raw_query.lower()
print(normalized_query)
normalized_query_title = normalized_query.title()
print(normalized_query_title)


# Task 17: Shouting Message Check
# 1. We have a message:
#    alert = "system failure"
#
# 2. Check if the string is in uppercase using .isupper().
#    Print the result.
# 3. Convert 'alert' to uppercase so it looks like an
#    urgent notification. Print the result.

alert = "system failure"
alert_check = alert.isupper()
print(alert_check)
alert_convert = alert.upper()
print(alert_convert)


# Task 18: Formatting Names
# 1. We have a name with messy casing:
#    user_first_name = "oLEKSANDR"
#
# 2. Fix the name so it follows standard grammar rules:
#    The very first letter must be uppercase, and all other
#    letters must be lowercase.
# 3. Print the result.

user_first_name = "oLEKSANDR"
user_name_format = user_first_name.capitalize()
print(user_name_format)


# Task 19: Full Address Title
# 1. We have an address in lowercase:
#    address = "ukraine, kyiv, khreshchatyk street"
#
# 2. Format the address so that EVERY word starts with
#    an uppercase letter.
# 3. Print the result.

address = "ukraine, kyiv, khreshchatyk street"
address_format = address.title()
print(address_format)


# Task 20: Secure Password Rule (Draft)
# 1. We have a draft password:
#    password = "secret123"
#
# 2. Check if this password consists only of lowercase letters.
#    Print the result (True/False).
# 3. Create a version of this password where all letters are uppercase.
#    Print the result.

password = "secret123"
password_check = password.islower()
print(password_check)
password_change_stile = password.upper()
print(password_change_stile)

# Task 21: Comparing Emails (QA Case)
# 1. We have two versions of an email:
#    email_db = "tester@gmail.com"
#    email_input = "Tester@Gmail.Com"
#
# 2. Convert BOTH strings to lowercase.
# 3. Compare them using '==' to see if they are now equal.
# 4. Print the result of the comparison (it should be True).

email_db = "tester@gmail.com"
email_input = "Tester@Gmail.Com"
email_db_convert = email_db.lower()
email_input_convert = email_input.lower()
print(email_db_convert == email_input_convert)


# Task 22: Sentence Formatting
# 1. We have a string in all caps:
#    sentence = "PYTHON IS AMAZING"
#
# 2. First, make the entire string lowercase.
# 3. Then, make only the very first letter of the result uppercase.
# 4. Print the final result.

sentence = "PYTHON IS AMAZING"
sentence_to_lower = sentence.lower()
sentence_to_cap = sentence_to_lower.capitalize()
print(sentence_to_cap)


# Task 23: Mixed Data Validation
# 1. We have a code with mixed casing:
#    code = "AbcDef"
#
# 2. Check if the string is completely in lowercase. Print the result.
# 3. Check if the string is completely in uppercase. Print the result.
# 4. Create a version of this code that is all uppercase. Print it.

code = "AbcDef"
code_check_lower = code.islower()
code_check_upper = code.isupper()
print(code_check_lower)
print(code_check_upper)
code_change_to_upper = code.upper()
print(code_change_to_upper)


# Task: Book Title Correction
# 1. We have a book title in lowercase:
#    book = "the lord of the rings"
#
# 2. Format this string so it looks like a proper title
#    (every word starts with an uppercase letter).
#    Store it in a new variable 'formatted_book'.
# 3. Check if 'formatted_book' follows the title format rules.
#    Print the result (True/False).

book = "the lord of the rings"
formatted_book = book.title()
formatted_book_check = formatted_book.istitle()
print(formatted_book_check)


# Task: The Ultimate Toggle
# 1. We have a test status:
#    text = "Test Passed"
#
# 2. Create 'low_text' (all lowercase) and print it.
# 3. Create 'high_text' (all uppercase) and print it.
# 4. Create 'cap_text' (only the very first letter is uppercase) and print it.
# 5. Check if 'high_text' is indeed uppercase. Print the result.

text = "Test Passed"
low_text = text.lower()
print(low_text)
high_text = text.upper()
print(high_text)
cap_text = text.capitalize()
print(cap_text)
result = high_text.isupper()
print(result)


# Task 26: Trimming User Input
# 1. We have a username with accidental spaces:
#    raw_user = "   john_doe   "
#
# 2. Use a method to remove spaces ONLY from the left side.
#    Print the result and its length using len().
# 3. Use a method to remove spaces ONLY from the right side.
#    Print the result and its length.
# 4. Use a method to remove spaces from BOTH sides.
#    Store it in 'clean_user' and print it with its length.

raw_user = "   john_doe   "
raw_user_remove_left = raw_user.lstrip()
print(raw_user_remove_left)
print(len(raw_user_remove_left))
raw_user_remove_right = raw_user.rstrip()
print(raw_user_remove_right)
print(len(raw_user_remove_right))
raw_user_remove_all = raw_user.strip()
print(raw_user_remove_all)
print(len(raw_user_remove_all))


# Task 27: Cleaning Database Entries
# 1. We have a string from a log file with tabs and newlines:
#    log_message = "\t  ERROR: Connection Lost  \n"
#
# 2. Use the method that removes ALL leading and trailing
#    whitespaces (including tabs and newlines).
# 3. Print the result and its length.
# 4. Check if the cleaned string starts with "ERROR".
#    Print the result (True/False).

log_message = "\t  ERROR: Connection Lost  \n"
clear_log_report = log_message.strip()
print(f"Clear report: {clear_log_report}, lenght: {len(clear_log_report)}")
clear_log_report_format = clear_log_report.startswith("ERROR")
print(clear_log_report_format)


# Task 28: Domain Name Extraction
# 1. We have a raw URL from a test report:
#    raw_url = "www.google.com..."
#
# 2. First, remove the dots from the RIGHT side only.
#    Print the result.
# 3. Then, from the result of step 2, remove the "www."
#    from the LEFT side only.
# 4. Print the final clean domain name.

raw_url = "www.google.com..."
raw_url_clear_right = raw_url.rstrip("...")
print(raw_url_clear_right)
raw_url_clear_left = raw_url_clear_right.lstrip("www.")
print(raw_url_clear_left)


# Task 29: Cleaning Currency Symbols
# 1. We have a price string from a web page:
#    price_str = "$$199.99  "
#
# 2. First, remove all spaces from both sides.
# 3. Then, remove the "$" signs from the left side.
# 4. Print the final result (it should be "199.99").

price_str = "$$199.99  "
price_str_removal = price_str.strip(' $')
print(price_str_removal)


# Task 30: The Phone Number Cleaner
# 1. We have a phone number with some "trash" symbols:
#    phone = "++380-99-123-45-67++"
#
# 2. Clean the "+" symbols from both sides.
# 3. Print the result.
# 4. Check if the result still contains dashes "-".
#    Print True or False. (Think about which method we learned
#    earlier for checking if something is inside a string).

phone = "++380-99-123-45-67++"
phone_format = phone.strip("+")
print(phone_format)
phone_format_chaker = "-" in phone_format
print(phone_format_chaker)


# Task 31: Price Calculation Fix
# 1. We have two strings representing prices:
#    price_item1 = "50"
#    price_item2 = "25.5"
#
# 2. Convert 'price_item1' to an integer.
# 3. Convert 'price_item2' to a float.
# 4. Create a variable 'total' which is the sum of both numbers.
# 5. Print the result.

price_item1 = "50"
price_item2 = "25.5"
price_item1_convert = int(price_item1)
price_item2_convert = float(price_item2)
total_price = price_item1_convert + price_item2_convert
print(total_price)


# Task 32: The Reverse Conversion
# 1. We have a numeric score:
#    score = 95
#
# 2. Convert 'score' into a string and store it in 'score_str'.
# 3. Create a message: "Your test score is: " + score_str
# 4. Print the message.

score = 95
score_str = str(score)
print(f"Your test score is: {score_str}")


# Task 33: Boolean Logic in Testing
# 1. We have two inputs:
#    user_input = "Admin"
#    empty_input = ""
#
# 2. Convert both to boolean values and print them.
# 3. Check what happens if you convert the number 0 and the number 1 to bool.
#    Print these results too.

user_input = "Admin"
empty_input = ""
user_input_bool = bool(user_input)
empty_input_bool = bool(empty_input)
print(f"Check what happens wiz user: {user_input_bool} and {empty_input_bool}")
num_zero = 0
num_one = 1
num_large = 999
print(f"Number 0 is: {bool(num_zero)}")
print(f"Number 1 is: {bool(num_one)}")
print(f"Number 999 is: {bool(num_large)}")


# Task 34: The Formatting Master
# 1. We have a price with many decimals:
#    raw_price = 15.666666
#
# 2. Print this price using an f-string so that
#    only 2 decimal places are shown.
# 3. Print it again showing only 1 decimal place.

raw_price = 15.666666
print(f"Price is: {raw_price:.2f}")
print(f"Price is: {raw_price:.1f}")

# Task 34.2: The Final Zero
# Add one more line to print raw_price with 0 decimal places


print(f"Price is: {raw_price:.0f}")



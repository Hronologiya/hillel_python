# Task: Garden Watering Automation 🌱
# You are creating a program for automatic garden watering. The program should make decisions based on three factors:
# Data:
# soil_moisture - a number from 0 to 100 (percentage of moisture)
# temperature - air temperature in degrees
# is_raining - True or False
#
# Rules:
# If it's raining - print "No watering needed, it's raining"
# If soil moisture is more than 70% - print "Soil is moist enough"
# If soil moisture is between 40% and 70% AND temperature is more than 25 degrees - print "Light watering"
# If soil moisture is less than 40% - print "Intensive watering needed!"
# Example data for testing:

soil_moisture = 35
temperature = 28
is_raining = False

if is_raining == True:
    print("No watering needed, it's raining")
elif soil_moisture > 70:
    print("Soil is moist enough")
elif soil_moisture >= 40 and soil_moisture <= 70 and temperature > 25:
    print("Light watering")
elif soil_moisture < 40:
    print("Intensive watering needed!")

# You are developing a script for a Smart Home Thermostat. The system needs to decide whether to turn on the heating,
# the AC, or do nothing, based on the room temperature and the presence of people.
# Rules:
# Safety First: If the current_temp is below 5°C, print: "Emergency Heating: Anti-freeze mode active!"
# (This should happen regardless of whether someone is home).
# Away Mode: If is_home is False, print: "Eco Mode: System off to save energy." (Unless the safety rule above applies!).
# Heating: If current_temp is more than 3 degrees below the target_temp, print: "Heating: ON".
# Cooling: If current_temp is more than 3 degrees above the target_temp, print: "AC: ON".
# Comfort Zone: If the temperature is within 3 degrees of the target_temp (inclusive), print: "Temperature is optimal".

current_temp = 18
target_temp = 25
is_home = True
# Expected output: "Heating: ON"

if current_temp < 5:
    print("Emergency Heating: Anti-freeze mode active!")
elif not is_home:
    print("Eco Mode: System off to save energy.")
elif current_temp < target_temp -3:
    print("Heating: ON")
elif current_temp > target_temp + 3:
    print("AC: ON")
else:
    print("Temperature is optimal")

# Task: Smart Security Camera You are programming a security camera.
# It should send different notifications depending on the time of day and motion.

# Intruder: If motion is detected AND it is night AND the owner is NOT home — print: "ALARM: Intruder detected!"
# Visitor: If motion is detected AND it is night (but the first rule didn't trigger) —
# print: "Notification: Someone is walking in the yard."
# Rest: In any other case — print: "System Secure".

motion_detected = True
is_night = True
is_owner_home = False

if motion_detected and is_night and not is_owner_home:
    print("ALARM: Intruder detected!")
elif motion_detected and is_night:
    print("Notification: Someone is walking in the yard.")
else:
    print("System Secure")

# We need to program the system for a smart office
# Max Energy Saving: If it is NOT working hours AND there is NO person detected —
# print: "Lights: OFF (Energy Saving Mode)".
#
# Working Mode: If it is working hours AND a person is detected AND the light sensor is low (dark) —
# print: "Lights: ON (Full Brightness)".
#
# Night Shift: If it is NOT working hours, but a person is detected — print: "Lights: ON (Dimmed Mode)".
#
# Default: In all other cases — print: "Lights: OFF".

is_working_hours = False
person_detected = True
light_sensor_low = True

if not is_working_hours and not person_detected:
    print("Lights: OFF (Energy Saving Mode)")
elif is_working_hours and person_detected and light_sensor_low:
    print("Lights: ON (Full Brightness)")
elif not is_working_hours and person_detected:
    print("Lights: ON (Dimmed Mode)")
else:
    print("Lights: OFF")

# Task: Airport Check-in System
# Rejection: If the passenger does NOT have a ticket — print: "Access Denied: No ticket".
# Priority: If the passenger is VIP OR the luggage weight is less than 10 kg — print: "Fast Track: Priority Boarding".
# Standard: If the passenger has a ticket (but doesn't meet rule 2) — print: "Standard Check-in".
# Test data

has_ticket = True
is_vip = False
luggage_weight = 8

if not has_ticket:
    print("Access Denied: No ticket")
elif is_vip or luggage_weight < 10:
    print("Fast Track: Priority Boarding")
else:
    print("Standard Check-in")


# Online Payment Security
# Green Light: If the amount is less than 100 AND it is a trusted device — print: "Payment Authorized".
#
# Verification: If the amount is over 100 OR it is NOT a trusted device — check if they have double authentication.
# If has_double_auth is True, print: "Payment Authorized via 2FA".
#
# Blocked: In all other cases — print: "Payment Denied: Security Risk".

amount = 150
is_trusted_device = True
has_double_auth = True
# Expected result: "Payment Authorized via 2FA"

if amount < 100 and is_trusted_device:
    print("Payment Authorized")
elif (amount > 100 or not is_trusted_device) and has_double_auth:
    print("Payment Authorized via 2FA")
else:
    print("Payment Denied: Security Risk")


# Game Difficulty Selector
# Hard Mode: If the level is over 50 AND it is a boss fight — print: "Difficulty: HARD".
#
# Special Access: If the player has premium OR (level is over 20 AND it is NOT a boss fight) —
# print: "Difficulty: NORMAL".
#
# Tutorial: In all other cases — print: "Difficulty: EASY".

level = 55
has_premium = False
boss_fight = True

if level > 50 and boss_fight:
    print("Difficulty: HARD")
elif has_premium or (level > 20 and not boss_fight):
    print("Difficulty: NORMAL")
else:
    print("Difficulty: EASY")


# Task: Smart Greenhouse
# Manual Override: If the farmer pressed the manual override button (manual_override is True) —
# print: "Watering: ON (Manual Control)".
# Automatic Watering: If soil moisture is less than 20 AND it is NOT raining — print: "Watering: ON (Low Moisture)".
# Standby: In all other cases — print: "Watering: OFF".

soil_moisture = 15
is_raining = False
manual_override = False

if manual_override is True:
    print("Watering: ON (Manual Control)")
elif soil_moisture < 20 and not is_raining:
    print("Watering: ON (Low Moisture)")
else:
    print("Watering: OFF")


# Task: Shopping Discount
# Big Discount (20%): If the total purchase is over 1000 AND (it is a birthday OR there is a coupon) —
# print: "Discount: 20%".
#
# Small Discount (10%): If the total purchase is simply over 500 (but the first rule didn't trigger) —
# print: "Discount: 10%".
#
# No Discount: In all other cases — print: "No Discount".

total_purchase = 1500
is_birthday = False
has_coupon = True

if total_purchase > 1000 and (is_birthday or has_coupon):
    print("Discount: 20%")
elif total_purchase > 500:
    print("Discount: 10%")
else:
    print("No Discount")


# Task: Exam Admission
# Direct Rejection: If the student has unpaid fees (has_unpaid_fees) — print: "Admission Denied: Pay the fees".
#
# Admission: If attendance is over 75 AND the midterm is passed — print: "Admission Granted".
#
# Extra Task: In all other cases — print: "Retake midterm or improve attendance".

attendance_percentage = 85
has_unpaid_fees = False
passed_midterm = True

if has_unpaid_fees:
    print("Admission Denied: Pay the fees")
elif attendance_percentage > 75 and passed_midterm:
    print("Admission Granted")
else:
    print("Retake midterm or improve attendance")

# Task: Ski Resort Access
# Closed: If it is stormy (is_stormy) — print: "Resort Closed: Dangerous weather".
#
# Access: If the person has a ticket OR they are an instructor — print: "Access Granted: Enjoy the slopes!".
#
# Denied: In all other cases — print: "Access Denied: Ticket required".

is_stormy = False
is_instructor = False
has_ticket = True

if is_stormy:
    print("Resort Closed: Dangerous weather")
elif has_ticket or is_instructor:
    print("Access Granted: Enjoy the slopes!")
else:
    print("Access Denied: Ticket required")

# Task: Smart Home Alarm
# Safe: If the code is correct (code_entered == correct_code) OR it is the owner (is_owner) — print: "System Disarmed".
#
# ALARM: If the alarm is active AND (window is broken OR the code is incorrect) — print: "ALARM: Security breach!".
#
# Standby: In all other cases — print: "System Monitoring".

alarm_active = True
code_entered = "1234"
correct_code = "1234"
window_broken = False
is_owner = True

if (code_entered == correct_code) or is_owner:
    print("System Disarmed")
elif alarm_active and (window_broken or correct_code != correct_code):
    print("ALARM: Security breach!")
else:
    print("System Monitoring")


# Task: Order Processor
# Create a for loop that iterates through the orders list.
# For each order number, print the following message: "Processing order: " followed by the order number.

orders = [101, 102, 103, 104, 105]
for number in orders:
    print(f"Processing order: {number}")


# Task: Website Link Checker
# Create a for loop that goes through the links list. For each link,
# print the message: "Testing link: " followed by the name of the link.

links = ["home.html", "about.html", "contact.html", "shop.html"]
for x in links:
    print(f"Testing link: {x}")

# Task: Email Validator
# Create a for loop to check each email in the list.
# If the email contains the symbol "@" — print: "Valid email: [email]".
# Else — print: "Invalid email found: [email]".

emails = ["user1@test.com", "admin@site.com", "invalid-email", "tester@qa.com"]
for user_mail in emails:
    if "@" in user_mail:
        print(f"Valid email: {user_mail}")
    else:
        print(f"Invalid email found: {user_mail}")


# Task: Security Audit
# Create a for loop to check each user.
# If the user is NOT "guest" — print: "Access Granted for: [user]".
# If the user IS "guest" — print: "Access Denied for: [user]".

users = ["admin", "guest", "editor", "manager", "guest"]
for x in users:
    if x != "guest":
        print(f"Access Granted for: {x}")
    else:
        print(f"Access Denied for: {x}")


#Create a for loop. If the price is not equal to 400, print: "Price: [price]".

prices = [100, 250, 50, 400]
for x in prices:
    if x != 400:
        print(f"Price: {x}")


# In QA, we often skip testing old browsers.
# Create a for loop to check each browser in the browsers list.
# If the browser is NOT equal to "Internet Explorer", print: "Starting test in: [browser]".
# If it IS "Internet Explorer", print: "Skipping: Old browser".

browsers = ["Chrome", "Firefox", "Internet Explorer", "Safari"]
for browser in browsers:
    if browser != "Internet Explorer":
        print(f"Starting test in: {browser}")
    elif browser == "Internet Explorer":
        print(f"Skipping: Old browser")

# Bug Tracker
# Create a for loop to iterate through test_results.
# Every time you find a "Bug", increase the bug_count by 1.
# After the loop (without indentation), print the final number of bugs: "Total bugs found: [number]".

test_results = ["Success", "Bug", "Success", "Bug", "Bug", "Success"]
bug_count = 0
for res in test_results:
    if res == "Bug":
        bug_count = bug_count + 1
print(f"Total bugs found: {bug_count}")

# Create a for loop to iterate through reports.
# Use an if statement to check if the report is exactly "Critical Bug".
# If it is, increase critical_count by 1.
# After the loop, print the message: "Urgent! Found [number] critical bugs!".

reports = ["Minor Bug", "Critical Bug", "Success", "Critical Bug", "Minor Bug"]
critical_count = 0
for report in reports:
    if report == "Critical Bug":
        critical_count = critical_count + 1
print(f"Urgent! Found {critical_count} critical bugs!")


# Create a for loop to go through the test_results.
# If the result is False, print: "Alert! We found a failed test!".
# If the result is True, print: "Test passed.".


test_results = [True, True, False, True]
for res in test_results:
    if res == False:
        print(f"Alert! We found a failed test!")
    elif res == True:
        print(f"Test passed.")


# Task: Database Health Check
# Create a for loop to iterate through the emails.
# If the email is None, print: "Warning: Missing email address!".
# Otherwise (else), print: "Email found: [email]".

emails = ["admin@site.com", None, "user@test.com", None]
for email in emails:
    if email is None:
        print(f"Warning: Missing email address!")
    else:
        print(f"Email found: {email}")


# Task: Connection Specialist.
#Create a while loop that runs as long as retries is greater than 0.
#Inside the loop, print: "Connecting... Attempts left: [retries]".
#Decrease retries by 1 in each step.
#After the loop, print: "Connection failed. Please check your internet.".

retries = 5
while retries > 0:
    print(f"Connecting... Attempts left: {retries}")
    retries = retries - 1
print(f"Connection failed. Please check your internet.")

# Task: Battery Task
# Create a while loop that runs while battery_level > 0.
# Inside the loop, first print: "Phone is working. Battery: [battery_level]%".
# Then, use an if to check: if battery_level == 2, print: "Low battery! Power saving mode ON".
# Finally, decrease battery_level by 2 (battery_level = battery_level - 2).

battery_level = 10
while battery_level > 0:
    print(f"Phone is working. Battery: {battery_level}%")
    if battery_level == 2:
        print(f"Low battery! Power saving mode ON")
    battery_level = battery_level - 2

# Task: The Password Gate
# Create a while loop that runs as long as password is not equal to "secret123".
# Inside the loop, print: "Access Denied. Please enter password.".
# After the loop (0 spaces), print: "Welcome! Access Granted.".

password = ""
while password != "secret123":
    print(f"Access Denied. Please enter password.")
    password = "secret123"
print(f"Welcome! Access Granted.")


# Task: Loading Screen
# Create a while loop that runs while status is equal to "Loading".
# Inside the loop, print: "Please wait...".
# Inside the loop, change status to "Ready".
# Outside the loop (0 spaces), print: "Game Started!".

status = "Loading"
while status == "Loading":
    print(f"Please wait...")
    status = "Ready"
print(f"Game Started!")

# Task: The Counter
# Set count = 1.
# Create a while loop that runs while count <= 3 (less than or equal to 3).
# Inside: print the number (count).
# Inside: increase count by 1.
# Outside: print "Finished!".
count = 1
while count <= 3:
    print(f"Number:{count}")
    count = count + 1
print(f"Finished!")


# Task: Break in a search loop
# We are testing a list of website pages. We need to find a page that has an error (status "404").
# Once we find it, we stop the search immediately.
#
# Use a for loop to check each page in pages.
# Print: "Checking page: [page]".
# Use an if to check: if page is equal to "Error 404".
# If it is, print: "Bug found! Stopping the test..." and use break.


pages = ["Home", "About", "Error 404", "Contact", "Gallery"]
for page in pages:
    print(f"Checking page: {page}")
    if page == "Error 404":
        print(f"Bug found! Stopping the test...")
        break

# Task: Limit reached
# We are testing a server that processes photos.
# The server has a limit: it can process only 3 photos at a time.
# If there are more photos in our list, we must stop and alert about the limit.
# Data:
photos = ["photo1.jpg", "photo2.jpg", "photo3.jpg", "photo4.jpg", "photo5.jpg"]
processed_count = 0
for photo in photos:
    print(f"Processing: {photo}")
    processed_count = processed_count + 1
    if processed_count == 3:
        print(f"Limit reached! Stopping...")
        break

# # Task: Find the admin
# We are testing a list of users. We need to find the user with the role "admin" to check their permissions.
# As soon as we find the admin, we stop the search because we don't need to check other regular users.
#
# Data:
users = ["guest", "user1", "user2", "admin", "user3", "manager"]
for user in users:
    print(f"Checking user: {user}")
    if user == "admin":
        print(f"Admin found! Accessing profile...")
        break


# Task: Skip corrupted files
# We are testing a photo gallery. Some files in our list are "corrupted" (broken).
# We want to print "Processing" for all normal photos, but if we find a "corrupted" one,
# we should skip it and NOT print the processing message.

photos = ["photo1.jpg", "corrupted.jpg", "photo2.jpg", "photo3.jpg", "corrupted.jpg"]
for photo in photos:
    if photo == "corrupted.jpg":
        print(f"Skipping broken file...")
        continue
    print(f"Processing: {photo}")


# Task: VIP only
# We are testing an invitation system for a party.
# We have a list of guests, but we only want to process those who have a "VIP" status in their name.
# If a guest is not a VIP, we skip them.

guests = ["VIP_John", "Alice", "VIP_Mary", "Bob", "VIP_Steve"]
for guest in guests:
    if "VIP_" not in guest:
        print(f"Skipping regular guest: {guest}")
        continue
    print(f"Sending VIP invitation to: {guest}")

# Task: Price Filter
# You are testing a list of prices in an online store.
# Some prices are "0" due to a bug.

prices = [100, 250, 0, 500, 0, 750]
for price in prices:
    if price == 0:
        print(f"Zero price found skipping...")
        continue
    print(f"valid price: {price}")


# Task: Connection Retries
# We are testing a server connection.
# The server is unstable, so we try to connect up to 5 times.
# Use a while loop with a counter 'attempts'.
# On each attempt, print "Connecting... Attempt [number]".
# If the attempt number reaches 5, print "Connection failed!" and stop.

attempts = 1
while attempts <= 5:
    print(f"Connecting... Attempt: {attempts}")
    attempts = attempts + 1
print(f"Connection failed!")


# Task: Scan for Critical Bug
# We are scanning a list of test results.
# Some results are "Passed", some are "Skipped", and one is "CRITICAL ERROR".

results = ["Passed", "Skipped", "Passed", "CRITICAL ERROR", "Passed"]
for result in results:
    if result == "Skipped":
        continue
    elif result == "CRITICAL ERROR":
        print(f"System failure! Stopping scan...")
        break
    elif result == "Passed":
        print(f"Test Passed: {result}")


# Task: simple_function
# Create a function named "show_status".
# Inside the function, print "The system is running..."
# and "No bugs detected."
# Call this function twice.

def show_status():
    print(f"The system is running...")
    print(f"No bugs detected.")


show_status()
show_status()

# Task: print_report
# 1. Create a function named "print_report" that takes one parameter: "test_name".
# 2. Inside, print: "Starting test: [test_name]"
# 3. Then print: "Test result: SUCCESS"
# 4. Call this function twice with different test names (e.g., "Login" and "Logout").


def print_report(test_name):
    print(f"Starting test: {test_name}")
    print(f"Test result: SUCCESS")


print_report("Login Page")
print_report("Shopping Cart")

# Task: Test Steps Reporter
# 1. You have a list of steps: ["Open app", "Login", "Search product", "Add to cart"]
# 2. Use a for loop with enumerate() to iterate through this list.
# 3. Print each step in the format: "Step [number]: [step_name]"
# 4. Important: Make the numbering start from 1 instead of 0.

steps = ["Open app", "Login", "Search product", "Add to cart"]
for i, step in enumerate(steps, start=1):
    print(f"Step {i}: {step}")

# task 11 == Виправте синтаксичні помилки
name = "Іван"
age = 10
print(f"Мене звати {name} і мені {age} років")

# task 12 == Виправте синтаксичні помилки
x = 5
y = 10
if x < y:
    print("x менше за y")

# task 13 == Виправте синтаксичні помилки
result = 2 + 2
print(result)

# task 14 == Виправте синтаксичні помилки
for i in range(5):
    print(i)

# task 15 == Виправте синтаксичні помилки
message = "Привіт"
print(message)

# task 16 == Виправте назви змінних
today = "понеділок"
my_name = "Оля"
class_number = 5
result = 100

# task 17 == Вставте пропущену змінну
number = 7
doubled = number * 2
print(f"Подвоєне число: {doubled}")

# task 18 == Зробіть так, щоб кількість зошитів
# була в 3 рази більша за кількість ручок
pens = 4
notebooks = pens * 3

# task 19 == Вставте пропущені змінні у print
first_name = "Тарас"
last_name = "Шевченко"
print(f"Повне ім'я: {first_name} {last_name}")

# task 20 == Зробіть так, щоб вік сина був у 4 рази менший за вік батька
father_age = 40
son_age = father_age / 4
print(f"Son age {son_age}")


# task 21
"""
У кошику лежало 12 яєць. Мама взяла 3 яйця для сніданку,
а тато приніс ще 6 яєць з магазину.
Скільки яєць стало в кошику?
"""

eggs_start = 12
eggs_after_breakfast = eggs_start - 3
eggs_final = eggs_after_breakfast + 6
print(f"Total eggs {eggs_final}")

# task 22
"""
У Петрика було 15 грн. Він купив морозиво за 8 грн
та цукерку за 3 грн.
Скільки грошей залишилось у Петрика?
"""

money = 15
money_left = money - 8 - 3
print(f"Balance {money_left}")

# task 23
"""
Автобус їхав 2 години зі швидкістю 60 км/год.
Скільки кілометрів проїхав автобус?
Підказка: відстань = швидкість * час
"""

bus_time = 2
bus_speed = 60
distance = bus_speed * bus_time
print(f"Distance {distance} km")

# task 24
"""
У класі 28 учнів. Хлопчиків на 4 більше, ніж дівчаток.
Скільки хлопчиків і скільки дівчаток у класі?
Підказка: нехай дівчаток буде x, тоді хлопчиків x+4,
а разом x + (x+4) = 28
"""

total_students = 28
students_girls = (total_students - 4) / 2
students_boys = students_girls + 4
print(f"Girls {students_girls}")
print(f"Boys {students_boys}")
print(f"Total {students_girls + students_boys}")


# task 25
"""
Прямокутник має довжину 8 см і ширину 5 см.
Порахуйте периметр та площу прямокутника.
Підказка: периметр = 2 * (довжина + ширина)
площа = довжина * ширина
"""

length = 8
width = 5
perimeter = 2 * (length + width)
area = length * width
print(f"Perimeter {perimeter} cm")
print(f"Area {area} cm2")

# task 26
"""
Олег з'їв 3 яблука, Катя з'їла вдвічі більше за Олега,
а Максим з'їв на 1 яблуко менше за Катю.
Скільки всього яблук з'їли діти?
"""

oleg_ate_apples = 3
kate_ate_apples = oleg_ate_apples * 2
maks_ate_apples = kate_ate_apples - 1
total_apples = oleg_ate_apples + kate_ate_apples + maks_ate_apples
print(f"Total {total_apples} apples")


# task 27
"""
У магазині молоко коштує 25 грн, хліб - 15 грн,
а масло на 10 грн дорожче за хліб.
Скільки коштує покупка, якщо купити все по одному?
"""

milk = 25
bread = 15
butter = bread + 10
total = milk + bread + butter
print(f"Total price {total} hrn")

# task 28
"""
Зранку температура була -3 градуси. Вдень потепліло на 8 градусів,
а ввечері похолодало на 5 градусів.
Яка температура ввечері?
"""

t_morning = -3
t_afternoon = t_morning + 8
t_evening = t_afternoon - 5
print(f"Temperature evening {t_evening}")

# task 29
"""
На першій полиці 18 книжок, на другій - на 6 менше,
а на третій - стільки, скільки на першій та другій разом.
Скільки книжок на третій полиці?
"""

shelf_1 = 18
shelf_2 = shelf_1 - 6
shelf_3 = shelf_1 + shelf_2
print(f"Total books {shelf_3} on shelf 3")

# task 30
"""
Цукерка коштує 5 грн. Якщо купити 3 цукерки,
магазин дає знижку 2 грн на всю покупку.
Скільки коштуватимуть 3 цукерки зі знижкою?
"""

one_candy = 5
three_candy = one_candy * 3
final_price = three_candy - 2
print(f"Total price {final_price}")

# task 31 == Fix the syntax errors
price = 50
discount = 10
if price > discount:
    print("Price is higher")

# task 32 == Fix the syntax errors
colors = ["red", "blue", "green"]
print(colors)

# task 33 == Fix the syntax errors
for number in range(3):
    print(number)
print("Done")


# task 34 == Fill in the missing variable
# Make the number of pencils 5 times more than erasers
erasers = 3
pencils = erasers * 5
print(pencils)

# task 35 == Fill in the missing variables in print
first_number = 10
second_number = 20
print(f"Sum is: {first_number + second_number}")

# task 36 == Fix variable names
my_variable = 100
number_3 = 30
user_name = "John"
value = 5

# task 37 == Calculate the result
# A rectangle has length 12 and width 7
# Calculate ONLY the area (not perimeter)
# Formula: area = length * width

length = 12
width = 7
area = length * width
print(f"Area of rectangle {area}")

# task 38
"""
Sarah has 20 candies. She gave 7 candies to her friend Tom,
and then her mom gave her 5 more candies.
How many candies does Sarah have now?
"""
candies = 20
tom_got_candies = candies - 7
mom_gave_candies = tom_got_candies + 5
print(f"Sara has {mom_gave_candies} candies")

# task 39
"""
A pizza costs 12 dollars. Soda costs 3 dollars.
A salad costs twice as much as soda.
What is the total cost if you buy one of each?
"""

pizza = 12
soda = 3
salad = soda * 2
total_price = pizza + soda + salad
print(f"Total price {total_price}")

# task 40
"""
In the morning the temperature was 2 degrees.
By noon it got warmer by 6 degrees.
In the evening it got colder by 4 degrees.
What is the temperature in the evening?
"""

t_morning = 2
t_noon = t_morning + 6
t_evening = t_noon - 4
print(f"Temperature in the evening {t_evening}")

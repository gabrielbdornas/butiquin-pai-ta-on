# intro
print('Hello, is there anybody in there?')
print('o----')
print(' ||||')
print('*' * 10)

# variables
# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=783s
price = 10
rating = 4.9
name = 'Mosh'
is_published = True
print (price)

name = "John Smith"
age = 20
new_patient = True

Simone = "André"""
print(Simone)
name[1]
print(name[1])
print(name[-2])
print(name[1:-1])
print(len(name))
print(name.title())
print(name.strip())
print(f'{2+2}+{10%3}')
print(name.find("Smith"))
name = name.replace("j", "k")
print(name)
print(name.find("John"))

# Receiving input
# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=1101s

your_name = input('What is your name? ')
print('Hi ' + your_name)
your_color = input('What is your favourite color? ')
print(your_name + ' likes ' + your_color)


# Python Cheat Sheet
# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=1336s

# Type conversion
# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=1366s

birth_year = input('birth year:  ')
print(type(birth_year))
age = 2022 - int(birth_year)
print(age)
print(type(age))

weight_oz = input('What is your weight (in pounds):  ')
weight_kg = int(weight_oz) / 2.2046
print('Your weight in kilos is: ' + str(round(weight_kg)))
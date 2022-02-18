current_year = int(input('Current year? '))
birth_year = int(input('Your birth year? '))
age = current_year - birth_year
print(type(age))

# Using print and type functions without defined variables
print(type('Paul')) # it'll print a str class
print(type(2)) # it'll print a int class
print(type(2.1)) # it'll print a float class
print(type(True)) # it'll print a bool class

user_name = input("What is your name? ")
print("Hi " + user_name + ", how is it going!")

# You can pass an variable to the input function
message = "What is your name? "
user_name = input(message)
print("Hi " + user_name + ", how is it going!")

# Practice
user_name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
print(user_name + " likes " + favorite_color + "!")

# Another way to use string concatenations
print(f'{user_name} likes {favorite_color}!')

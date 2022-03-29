Object Oriented Programming in Python
===

## Class and Instances

In this tutorial we'll learning how to create and use classes within python and how object-oriented concepts are applied within the language.
Here we'll cover the basics of creating and instantiating simple classes, but first, why should we even use classes? 
This isn't specific to Python. You can see classes being used throughout most modern programming languages, and there's a good reason for that.
They allow us to logically group our data and functions in a way that's easy to reuse and also easy to build upon if needed be.

In object-oriented programming we call data as attributes and functions as methods, and you'll hear those terms a lot throughout these tutorials.

Let's go ahead and get started creating our first class.
Supose we had an application for our company and we wanted to represent our employees as a class.
This would be a great use case for a class because each individual employee is going to have specifics attributes and methods.

## Atribuites

Wouldn't be nice if we had a class or a blueprint to create each employee just one time and avoid to do this manually each time from scratch.
Each employee is going to have a name, an email address, a pay, and also some actions that they can perform.
In this case it's just as easy as saying class employee, as shown below:

```Python
class Employee:
    pass
```

If you ever have a class or a function that you want to leave empty for an while then you can simply put a `pass` statement in it and python will know that you just want to skip that for a moment and no error will be thrown.

Using our example to reinforce the difference between class and instance, each unique employee created using our employee class will be an instance of that class.

```Python
class Employee:
    pass

empl_1 = Employee()
empl_2 = Employee()
```
Each of these are unique instances of the employee class, as we can check with a print statement:

```Python
class Employee:
    pass

empl_1 = Employee()
empl_2 = Employee()

print(empl_1)
print(empl_2)
```

Here the print statement show that they both have different ids and locations in memory and this is an important distinction to know.

Now, we could manually create instance variables or atribuites like first name, last name, pay and e-mail for each employee and print one of this attibuites by doing something like this:

```Python
class Employee:
  pass

empl_1 = Employee()
empl_2 = Employee()

print(empl_1)
print(empl_2)

empl_1.first_name = 'Gabriel'
empl_1.last_name = 'Dornas'
empl_1.email = 'gabriel.dornas@company.com'
empl_1.pay = 50000

empl_2.first_name = 'Paul'
empl_2.last_name = 'Mccartney'
empl_2.email = 'paul.mccartney@company.com'
empl_2.pay = 60000

print(empl_1.email)
print(empl_2.email)
```
## Init Method and Self

How it's everything so far? Good, isn't it? But we can improve our code. 
We wouldn't have to manually set all these and other variables every time we instantiate our classes.
We don't get much benefit of using classes if we did it this way. 
As you can see it's a lot of code and it's also prone to mistakes.

Let's set all of this information for each employee when they're created rather than doing all of this manually like we did before:

```Python
class Employee:

  def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
    self.pay = pay
```
To set up automatically when we create the employee we have to use a special method called `__init__`.

When we create methods within a class they receive the instance as the first argument.
Automatically and by convention, we should call the instance `self`.
You can call it hatever you want, but it's a good idea to stick to convention here and just use `self`.
After self we can specify all other arguments that we want to accept.

Notice that in our case, we don't create email as a `__init__` method parameter. We chose to create it using the first and the last upercases names inside a string interpolation.

When we say `self` is the instance means that when we do `self.first_name`, for example, is the same as `empl_1.first_name`, except now instead of doing this manually t'll be done automatically when we create our employee objects.

Now, when we create our instances of our employee class we can pass in the values that we specified in our `__it__` method and let the instance takes cara of it for us, leaving off `self`: 

```Python
class Employee:

  def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
    self.pay = pay


empl_1 = Employee('Gabriel', 'Dornas', 50000)
empl_2 = Employee('Paul', 'Mccartney', 60000)

print(empl_1)
print(empl_2)

print(empl_1.email)
print(empl_2.email)
```

Passing in all of the same information that we did manually before will do the same for us.

## Methods

So everything that we have so far, like the names, email and the pay, are all attributes of our class. 
But now let's say that we wanted the ability to perform some kind of action.
To do that, we can add some methods to our class.
Let's say we wanted the ability to display the full name of an employee:

```Python
class Employee:

  def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
    self.pay = pay
  
  def full_name(self):
    return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'


empl_1 = Employee('Gabriel', 'Dornas', 50000)
empl_2 = Employee('Paul', 'Mccartney', 60000)

print(empl_1)
print(empl_2)

print(empl_1.email)
print(empl_2.email)

print(empl_1.full_name())
print(empl_2.full_name())
```

This is an action that you'd likely need to do a lot with a class.
Of course we can do this manually outside the class, but that's a lot to type in each time that you want to display the employees full name.
Instead, the method within our class allows us to put this functionality in one place.

Pay attention to use parentheses in order to run `full_name()` method properly, because if we left the parentheses off and printed this then you'll see the method's information instead of the return value of it.

One more quick thing to point out here is a common mistake when creating methods is forgetting the self argument for the instance.
If run the method that we accidentally left self off of then, we'll see a type error message saying that we "takes zero positional arguments but one was given".
This can be confusing because it doesn't look like we're passing any arguments into full name, but the instance is getting it passed automatically.
We have to expect that instance argument in our method, and that's why we added self in it.

To ilustrate that let's call `full_name()` method directly from Employee class. In this case, we have to manually pass in the instance as an argument.

```Python
class Employee:

  def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
    self.pay = pay
  
  def full_name(self):
    return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'


empl_1 = Employee('Gabriel', 'Dornas', 50000)
empl_2 = Employee('Paul', 'Mccartney', 60000)

print(empl_1)
print(empl_2)

print(empl_1.email)
print(empl_2.email)

print(Employee.full_name(empl_1))
print(empl_1.full_name())
```

As you can see above, the two new lines are exact the same thing, but in the seconde case when we do employee one, which is a instance and I call the method, I don't need to pass in self, because it does it automatically. 
On the other hand, when we call the method on the class and it doesn't know what instance that we want to run that method with, we do have to pass in the instance and that gets passed in as self.
Its good to show that because that's actually what's going on in the background when we call our class' methods.

That's it for this tutorial. So far we've learned how to create simple classes, the difference between a class and an instance of that class and we also learned how to initialize class attributes and create methods properly.
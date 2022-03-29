Object Oriented Programming in Python
===

## Class X Variables

In this tutorial we'll learning how to create and use classes within python and how object-oriented concepts are applied within the language.
Here we'll cover the basics of creating and instantiating simple classes, but first, why should we even use classes? 
This isn't specific to Python. You can see classes being used throughout most modern programming languages, and there's a good reason for that.
They allow us to logically group our data and functions in a way that's easy to reuse and also easy to build upon if needed be.

In Object Oriented Programming - OOP, we call those data and functions attributes and methods, and you'll hear those terms a lot throughout these tutorials.

Let's go ahead and get started creating our first class.
Supose we had an application for our company and we wanted to represent our employees as a class.
This would be a great use case for a class because each individual employee is going to have specifics attributes and methods.

For example each employee is going to have a name, an email address, a pay, and also some actions that they can perform.

Wouldn't be nice if we had a class or a blueprint to create each employee just one time and avoid to do this manually each time from scratch.
In this case it's just as easy as saying class employee, as shown below:

```Python
class Employee:
    pass
```

If you ever have a class or a function that you want to leave empty for an instance then you can simply put a `pass` statement in it and python will know that you just want to skip that for a moment and any error will be thrown.

Using our example to reinforce the difference between class and instance, each unique employee created using our employee class will be an instance of that class.

```Python
class Employee:
    pass

empl_1 = Employee()
empl_2 = Employee()
```
Each of these are going to be their own unique instances of the employee class, as we can check with a print statement:

```Python
class Employee:
    pass

empl_1 = Employee()
empl_2 = Employee()

print(empl_1)
print(empl_2)
```

Here the print statement show that they both have different ids and locations in memory and this is an important distinction to know.

Now, we could manually create instance variables like first name, last name, pay and e-mail for each employee and print one of this attibuites by doing something like this:

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
## Init Method

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


empl_1 = Employee('Gabriel', 'Dornas', 50000)
empl_2 = Employee('Paul', 'Mccartney', 60000)

print(empl_1)
print(empl_2)

print(empl_1.email)
print(empl_2.email)
```
To set up automatically when we create the employee we have to use a special method called `__init__`.

When we create methods within a class they receive the instance as the first argument.
Automatically and by convention, we should call the instance `self`.
You can call it hatever you want, but it's a good idea to stick to convention here and just use `self`.
After self we can specify all other arguments that we want toa accept.

Notice that in our case, we don't create email as a `__init__` method parameter. We chose to create it using the first and the last name upercases inside a string interpolation.

## Self

Okay, so whenever I say that self is the instance what I mean by [that] is that when we self dot first?

equals [two] first here

It's going to be the same thing as us saying down here that employee one dot first equals

[Korey] except now instead of doing this manually

It'll be done automatically when we create our employee objects

Now these don't need to be the same as our arguments so for example. I could make this

Self dot f name equals first, but I usually like to keep these similar if possible

So I'm going to go ahead and set that back [to] self dot first equals first, okay?

So now when we create our instances of our employee class right here now

we can pass in the values that we

specified in our anit method now our net method takes the instance which we call itself and the first name last name and

Pay as arguments, but when we create our employee down here the instance is passed automatically

So we can leave off self we only need to provide the names and the pay so we could create these by

Passing in first and we have to do this in order

So I will pass in all of the same information that we did manually down there and for the second one

I'll do [test] and

User and I think I had that at

[sixty] [thousand] okay

so what would happen on this line when we create this employee the anit method will [be] run automatically, so

Employee one will be passed in as self and then it will set all [of] these attributes

So it'll set employee one dot first is equal to first which we passed in as quarry

Employee one that last equals what we passed in is last and so on so now that we have that an it method in place

We can go [ahead] and delete these manual assignments that we made down here

And you can see by deleting that that we got rid of a lot of code

So I'm going to go ahead and comment out those lines

[we're] printing [the] employees, and I'm just going [to] go ahead and print out the email

So if I run that then you can see that that still works, okay?

So everything that we have so far [like] the names and email and the pay are all attributes of our class now

Let's say that we wanted the ability to perform some kind of action not to do that

We can add some methods to our class

So let's say [that] I wanted the ability to display the full name of an employee now

This is an action that you'd likely need to do a lot with a class like this

So we can do this manually outside the class if I was to come down here and do

Print and I could get the full name just by putting in two

placeholders there and doing a format and saying employee one dot first and

Employee one dot last and if I go ahead and print this out

And you can see that we got the full name there

But that's a lot to type in each time that you want to display the employees full name, [so] instead

Let's create a method within our class that allows us to put this functionality in one place, so within our class here

I'm going to create a method called full name and we can do that with just doing a death of

Full name now [like] I said before each method within a class

Automatically takes the instance as the first argument

and

We're going to always call [that] self and the instance is the only argument that we'll need in order to get the full name

So within this method here

I'm just going [to] take the same logic that we had down here and cut that out

and I'm just going to go ahead and return that but we have to be careful here because

now instead of printing Employee [1]

[first-name] and [lastname], [I'm] going to use self so that it will work [with] all instances

So I'm going to do self dot first and self dot last

So now that we created that method instead of printing like we did before now

I can just come down [here] and do employee 1 dot full name and

Print that out

And if I run that then you can see that we got the same [thing] and notice that we need the parentheses here

Because this is a method instead of an attribute

So if I left the parentheses off and printed this then you can see that it prints the method instead

[of] the return value of the

method so we're going to have to put those parentheses on in order to run that properly so now we have full advantage of

Code reviews here, so instead of typing this out for each full name that I want to print now

I can just use that method so now if I wanted to print employee two's full name

It's just as easy as replacing employee one with employee two and running that and we get the correct answer

Okay, and one more quick thing that I wanted [to] point out here

Now one common mistake that I see when creating methods is forgetting the self argument for the instance

So let's take a quick look at what that would look like if we left that off

so now before I run this if I just comment it out this printing of full name down here and

Ran this then you can see I'm actually going to remove these print statements here as well

Now [you] can see that this runs without any errors

But if I was to try to run this method that we accidentally left self off of then

Run this and you can see that we get an error and the error that we got was a type error

full-name takes zero positional arguments

But one was given now this can be confusing because it doesn't look like we're passing any arguments here into full name

But the instance which in this case is employee two is getting passed automatically

So we have to expect that instance argument in our method, and that's why we added self

so I'm going to come back up [here] to full name and

Put self back in and now running this you can see that [it] runs

Correctly now we can also run these methods using the class name

Itself which makes it a bit more obvious of what's going on in the background because whenever we do that, so I'll do employee

Dot full name now [when] we run it from the class we have to manually pass in the instance as an argument

So in this case

I'll pass in employee one so you can see how these are similar, but not exactly the same

So I'm going to put these side-by-side just so that we can compare them here

So these two lines here do the exact [same] thing, but here when I do employee one

Which is a instance and I call the method. I don't need to pass in self

It does it automatically and when we call the method on the class

And it doesn't know what?

instance that we want to run that method with so we do have to pass in the instance and that gets passed in as

self and if I go [ahead] and

Print this out and run it then you can see that it works

Just like if we were to print out the employee one dot full name

And I wanted to show you that because that's actually what's going on in the background

when we run employee one dot full name it gets transformed into this here employee dot full name and

Passes in employee one as self and that's why we have self for these methods, so I hope that makes sense to you

That's not extremely important to know when we're just getting started with working with classes

But we need to understand that [in] later videos once we start inheriting from other classes and things like that

So I figured it would be a good thing to go ahead, and show you that now okay?

So I think that's going to do it for this video in this video

We learned how to create simple classes the difference between a class and an instance of that class and we also learned how to initialize

class attributes and create methods now

We still have a lot to cover in future videos, and we'll be going over more advanced topics, so in the next video

We'll learn about class variables, and how they differ from instance variables that we saw here

But if you do have any [questions] with what we covered in this video

Then feel free to ask in the comment section [below] and I'll do my best to answer those

If you enjoy these tutorials and would like to support them then there are several ways you can do that

The easiest way is to simply like the video and give it a thumbs up and also

it's a huge help to share these videos with

Anyone who you [think] would find them useful and if you have the means you can contribute through patreon

And there's a link to that page in [its] scription section below be sure to subscribe for future videos and thank you all for [watching]
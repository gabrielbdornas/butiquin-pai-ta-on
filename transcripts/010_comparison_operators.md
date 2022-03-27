#Comparison Operators

python.
In this tutorial I'm going to talk to you guys about comparison operators in Python. 
We use comparison operators in situations where we want to compare a variable with a value, for example, if temperature is greater than 30, then we want to print it's a hot day. 
Otherwise, if it's less then 10, it's a cold day, otherwise it it's neither hot nor cold. 
And by the way I'm taking about celsius, not farenheit.
So, to build these rules into our program, we need to use comparison operators. 
Back to app.py, I define this temperature value, let's write an if statement, if temperature now we want to check to see if this is greater than 30, so we use the greater than operator. 
If this is greater than 30, we want to print it's a hot day otherwise, let's just print it's not a hot day. 
Now, when we run this program, we're going to see this second message because 30 is not greater than 30. 
So our first condition a value is to false. 
let's verify that. 
So run, it's not a hot day. 
Now if you change the temperature to 35 and run this again, we're going to see a different message, it's a hot day, so this is where we use comparison operators. 
Now what we have here as you know is an expression because it's a piece of code that produces a value. 
So more accurately this is a boolean expression. 
So this is the greater than operator, we also have greater than or equal to, we have less then, less then or equal to, here's the equality operator, so if the temperature equals to 30, then you can say it's a hot day. 
Note that this is different from the assignment operator that has only one equals sign. 
You can see that if we use only one equal sign here we immediately get this red underline because this is simply an assignment statement. 
We're changing the value of the temperature.
You are setting the value of something else. 
So we don't have a boolean expression, you are not producing a boolean value. 
Okay? So, our equality operator has two equal signs and finally we have not equal which is an exclamation followed by an equal sign.
Now here's an exercise for you. 
You have probably seen that when you fill out a form online, sometimes the input fields have validation messages, or example, let's say we have an input field for the user to enter their name.
Now if the name is less then 3 characters wrong we want to display a validation error, like name must be at least three characters, otherwise, if the name is more then 50 characters long then we want to display a different validation error like name can be a maximum of 50 characters. 
Otherwise if the name is between 3 and 50 characters then we just want to tell the user that name looks good.
So go ahead, and write a plan to implement these rules.
Alright let's define a variable called name and set it to let's say j. 
So we're assuming this is what the user types into an input field.
Now, we want to get the number of characters in this string.
So we use the len function, right? Len of name.
When we print this we get 1, right you have seen this before. 
Now here we want to use an if statement so if len of name is less then 3, then we want to print name must be at least 3 characters now here we need a second condition to check the upper limit. 
So el if len of name is greater than 50, then we want to print a different message, name, must be a maximum of 50 characters.
Okay? And otherwise if else none of these conditions are true that means the name looks good. 
So, print, name looks good. 
Let's run our program. So in this case we get this message
because our name is too short. 
Now if you go back here and type something really really long. 
And then we run our program we're going to see a different message name must be a maximum of 50 characters and finally if we type a proper name here like John Smith and run our program we get name.
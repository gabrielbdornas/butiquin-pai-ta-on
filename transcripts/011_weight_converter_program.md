#Weight Converter Program

looks good.
Here's another good exercise that combines many of the materials you have learned so far, so earlier you built a program to convert someone's weight from pounds to kilograms. 
Now we want to extend this program and allow the user to enter their weight in either kilograms or pounds and then we will convert it to the other unit. 
Here's how our program is going to work. 
So I enter my weight in pounds so 100 and 60 now it's telling me if it's in pounds or kilograms. 
So here I'm adding l to lbs or k for kilograms.
And by the way, this program is not case sensitive so when I enter a capital l or lowercase l it takes it as pounds. 
Now it tells me ur set it to kilos. 
Let's run this program one more time, this time I'm going to enter my weight in kilo's, so send it to is the weight and the unit is kilograms so k, and it says you are 160 pounds.
So go ahead and spend a few minutes on this exercise, you will see my solution next.
Alright first let's ask the user their weight. 
So we use the input function, weight colon we get the return value and store it in the variable called weight.
Now the second question, so one more time we use the input function el for pounds.
Or k for kilograms. 
So, let's get that too and store it in a variable called unit now we need an if statement. 
So if unit equals l then we need to convert this weight into kilograms. 
However, with this implementation we are only allowing the user to enter a capitol l, if they enter a lowercase l this code is not going to work. 
So this is where we use the upper method of string objects so this unit is a string because as I told you before, the input function always returns a string.
So, we can use the dot operator to access all it's methods or functions, here we call the upper method, this will convert whatever the user enters to upper case and then we'll convert it to a capital l. 
Now, if this condition is true, then we need to get the weight and multiply it by 0,.45 However, as you know this weight is a string object, and we cannot multiply a string by a floating point number, we talked about this earlier in this course.
So first we need to convert this weight to a numerical value. 
So right here, when we call the input function, we can get the return value and pass it to the int function. So, we call the int function and give it the return value of the input function. 
Now, the in function will return an integer so we can store it in this weight variable. 
So here's the converted weight, let's store it in a variable called converted, then we print here we can use a formatted string, so we prefix this string with f ur we add curly braces to dynamically insert the value of converted variable. 
And finally we add kilo.
Otherwise, if the unit is kilograms.
We need to divide the weight by 0.45. q
So, weight divided by 0.45 and just to refresh your memory, this division operator returns a floating point number but if we use double slashes we'll get an integer.
In this case, we want to get a floating point number, finally let's print a formatted string, ur curly braces, converted pounds. 
Okay? Now let's run this program and see what happens. 
So weight is 160 and lbs in and that equals to 72 kilos, perfect, if we run it one more time, and enter 72 kilos.
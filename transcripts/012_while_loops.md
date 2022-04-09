#While Loops

we get 160 pounds.
In this tutorial I'm going to show you how to use y loops in python. 
We use y loops to execute a block of code multiple times and there are often useful in building interactive programs and games. 
In a future tutorial I'm going to show you how to build a simple game using a y loop.
So, let's get started with the basics, we write a y statement and right after that, we type a condition followed by a colon as long as this condition is true the quote that we write in this block will be repeatedly executed. 
Here is an example.
We can define a variable like i, as in short for index and set it to 1. 
Now we set our condition to i less than or equal to 5, so as long as I is less then or equal to 5, we can print i, on the terminal. 
And then we need to increment i, by 1. 
So we set i to i plus 1. 
The reason we do this is that if we don't do this I will be 1 forever so we'll end up with an infinite loop. 
Because this condition will always be true. 
One is always less then 5, so in every iteration of this loop, we increment i by 1, so at some point, i is gonna be six and then that is when this condition will be false and then we'll jump out of this loop, okay? Now to demonstrate how everything works after this loop I'm going to add a print statement say done. 
So note that these two lines are indented so they are part of the y block. 
Okay, now let's go ahead and run this program and see what happens. 
So, take a look, we get the numbers 1-5 followed by done. 
So heres how this program gets executed first we set i to 1 now python interpreter executes line 2, this condition is true because i is less then 5, so i is printed on the terminal and then incremented by 1. 
Then the control moves back to the beginning of the y loop.
So it doesn't go to the next statement. 
So, we come back here and now we are in the second iteration. 
In the second iteration i is 2, and because 2 is less then 5, our condition is still true, so i will be printed on the terminal, and once again it will be incremented by 1, so at some point i is going to be 6, and that's when this condition will be false so our look will be terminated and this done message will be printed on the terminal.
So this is the basics of y loops. 
Now let's make this program a little bit more interesting. 
Here we can write an expression like this. 
We add a string, and in this string we add an asterisk and then we multiply this string by i. 
So with this expression, we can repeat a string, when we multiply a string by a number, that string will be repeated. 
For example, if i is two, this expression will produce a string with two asterisks. 
Now let's run the program and see what we get. 
So we see this little triangle shape here. 
Because in the first iteration i is 1, so, 1 times an asterisk produces 1 asterisk.
In the second iteration i is 2, so when we multiply 2
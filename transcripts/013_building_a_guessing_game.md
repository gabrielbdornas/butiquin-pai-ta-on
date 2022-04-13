#Building a Guessing Game

by 1 asterisks, we'll get 2 asterisks.
In this tutorial I'm going to show you how to use a y loop to build a guessing game like this. 
So we have this secret number which is currently set to 9. 
Now the computer is asking me to make a guess. 
So, let's say 1 is not right because the secret number is 9, okay, try again, 2, no it's not right, let's try again, so I only have three chances to make a guess. 
If I can't guess the number the program tells me that I failed. 
Let's run the program one more time, this time I'm going to guess the number, it's 9, there you go, it says you in.
So let's go ahead and build this program using a y loop.
Alright, let's start by defining a variable to store our secret number so, we call the secret underline number and set it to 9.
Now we need a while loop to repeatedly ask a user to make a guess. 
So while condition colon What is our condition here? Well we want to give our user a maximum of three guesses. 
So similar to the last tutorial, we can define a variable like I, set it to 0, and assume this represents the number of guesses the user has made. 
And then we write our condition as i less then 3. ?
Note that here I'm not using less then or equal to operator, because with this condition our loop will be executed 4 times, while i is 0, one, two, and three, so here we should use the less then operator. 
Now if we give this code to someone else it's unclear what does i represent here, it's only in our head that i represents the number of guesses the user has made. 
So as a best practice, always use meaningful and descriptive names for your variables.
So it's better to rename this variable to guess, count.
Let me show you how to rename. 
So right click on i variable, and then go to refactor and rename it. 
Look at the shortcut. 
On a Mac computer it's shift and f 6. 
Now in this dialogue box we can easily rename your variable and pycharm will update all the references to that variable so we don't have to manually update each instance, okay? Let's change this to guess_count enter, there you go, now that is better, also it's better to store 3 in a separate variable to make our code more readable, because it's not quite clear what does 3 represent here.
So, let's define a variable called guess limit say to 3, and then we can change 3 to guess underline limit, now our code is more readable while guess count is less then guess limit, see it reads like a story this is how you should write code. 
Okay, so while this condition is true, we want toast the user to make a guess. 
So here we use our input function, guess Now whatever the user enters comes out as a string so we need to convert it to an integer.
So right here, we pass the result to the end function and then get it and store it in a separate variable called guess.
So at this point the user made a guess, now we need to increment guess count so guess count we set it to plus equal 1 or okay, now we need to check to see if the user will make the right guess.
So here we need an if statement. 
If what the user guessed equals our secret number, again see our code is so readable. 
It's like a story you can read it like plain English. 
So if this condition is true we want to tell the user they won. 
So print you won now lets go ahead and run our program up to this point.
So okay it's asking me to make a guess, I'm going to make the wrong guess so one it asked me again, 2 one more time, 3, okay, what is missing in this implementation is the message that tells me that I failed. 
We're going to take care of it momentarily, but let's run the program one more time and make the right guess. 
So, 9 okay it says you won, but it's still asking me to make a guess, because our while loop is going to get executed 3 times. 
Look 1 and 2. 
So we need to change our program such that if the user makes the right guess, we need to terminate our while loop, we need to jump out of it. 
How do we do that? So, over here if the user makes the right guess, after we print this message we can use the brick statement to terminate terminate a loop, when python interpreter sees this, it's going to immediately terminate our loop, it's not going to evaluate this condition again.
Now let's run our program and see what happens. 
So, I'm going to guess the right number, you won and look, you are now asked to make two more guesses, beautiful. 
Now the last thing we need to add here is the message that tells the user that they failed if they could not guess the right number. 
How do we do that? Well in Python our while loops can optionally have an else part.
Similar to the if statements. 
So earlier you learned that our if statements can optionally happen else part. 
Here, so if this condition is true, do this, otherwise do something else. 
In this case our if statement doesn't have an else part. 
Now, similar to the if statements Our while loops, our while statements can also have an else part.
So, right at this level we can add an else block, so else colon.
And the code that we write here will get executed if this while loop completes successfully without an immediate break. 
In other words. 
If the user guesses the right number, you break this loop, you jump out of it so the code that we write in the else block will not get executed.
But if the user cannot guess this number, you're never going to break out of this loop, so this loop will be executed to completion untill this condition become false. 
In that case, the code that we write in the else block will get executed, and this is the perfect opportunity for us to tell the user hey, you made three guesses but none of them were right.
So, print, sorry you failed. 
Now, let's test the program one more time.
So, guess 1, 2, 3, sorry you failed, let's run it one more time. 
This time I'm going to make a wrong guess, and then the right guess,
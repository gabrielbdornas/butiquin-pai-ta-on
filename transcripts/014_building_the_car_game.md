#Building the Car Game

we won and our loop terminated immediately.
Alright, now it's time for you to practice what you have learned so far.
So once again we're going to build a game this game is a simulation card game. 
Now our game doesn't have a graphical user interface or gooey and it doesn't really matter for now, our focus is entirely on building the engine for this game. 
So let's see how this works.
When we run this, we get this little symbol here, and our program is waiting for us to enter a command. 
If you type help either a lower case or upper case we get the list of commands that our program or our game currently supports. 
So we can type the start command to start our car, we can type stop command to stop our car, and quit to terminate the game.
Any other commands that we type our program is going to tell us hey I don't understand that.
For example, if I type asd here, it's going to say I don't understand that.
If you type start, we get this message, car started, ready to go, if you type stop it says car stopped, and finally if we hit quit our program terminates, this is a fantastic exercise for you to practice wha you have learned, so pause the video and spend 5-10 minutes to build this program.
Alright, we're going to start with a while loop with a condition What is our condition here? We want to run this loop until the user types quit. 
So we can define a variable or a story to command what the user enters, and then we can run this loop as long as the command does not equal to quit. 
So right before the loop, we define a variable, command, and initially we set it to an empty string. 
An empty string is a string that has no characters in it. 
We only have the quotes. 
So then we type out our condition as while command does not equal to quit then do something.
Now immediately we have a problem here because we're assuming that the user types the command in lower case, so if they type this in upper case they our program is not going to behave properly, so to fix this problem, you need to call the lower method of the string object and then compare the results.
With this quit. 
You could also call this upper and then type quit in upper case. 
It's about our personal preference in this demo I'm going to use lower case characters.
So, okay, now in this loop we need to ask the user to enter a command. 
So once again we're going to use our input function, we're going to add a greater then symbol followed by a space, whatever the user enters, we get it and store it in our command variable. 
Now apart from quit command, there are three other commands that we need to support. 
Start, stop, and help. 
So here we need an if statement to compare what the user enters with one of the supported commands.
So, if command.lower equals start then you want to print the message like the car started. 
So print the car started.
Ready to go, it doesn't matter, now the second condition. 
What if its not start, maybe it's stop? So, el if command.lower equals stop, there you go, then we print a different message car stopped. 
Now look at our code.
We have repeated this lower lower lower multiple times.
This is bad, in programming we have a term called dry, which is short for don't repeat yourself. 
So whenever you have duplicate your code that means you're doing something wrong. 
So how can we solve this problem.
Well, instead of calling the lower method in each condition, we can call it right here when we get the input from the user, so this input function as you know returns a string, we can immediately call the lower method on this string, and with this command will always be in lowercase, so we don't need to call this method in every condition. 
Look, we remove the duplication and also our conditions are shorter and easier to read. 
There is also one more place we need to modify so, it's right here. 
That is better.
Now, the third command. 
We need one more el if.
If the command equals help, then, we want to show the commands that we support. 
So, here we're going to print a multi line string. 
So we use triple quotes like this, and give the user a guideline like this. 
So start to start the car stop to stop the car, and quit to quit. 
Now finally we need an else part, so if what the user enters is none of these commands, we're going to tell them, hey we don't understand these, else, colon print sorry I don't understand that.
And by the way note that here becomes I'm using double quotes, I can easily use a single quote as an apostrophe, okay? So let's run our program up to this point and see what happens.
Alright, let's type start car is started, beautiful, stop, car is stopped, help, we get this guideline, but there's so much indentation before our commands, we'll fix that in a second. 
And finally let's test the quit command, oops, our program didn't work properly. 
Here is the reason. 
With these if statements, we're comparing the command with start stop, and help. 
Anything else will end up here, so that's why our program says it doesn't understand that. 
So that's why our program says it doesn't understand that command. 
However, after this el statement the control will be moved to the beginning of the loop.
At this point our command is quit, so our loop will complete and the program terminates. 
In other words when we run this program and type quit, our program actually quits but we still see this message which shouldn't appear here. 
How can we solve this problem? Well, we can come back here and just before the else block, add another el if, something like this. el if command equals quit then you can immediately break.
This will solve our problem, but note that we have kind of repeated this expression in two places. 
The reality is that we don't really need this condition on the top, because with these if statements well more accurately with this el if we can jump out of this loop and terminate our program. 
So, we can simplify our condition to something like this. 
True. 
So while true means this block of code is going to get executed repeatedly, until we explicitly break out of it, okay? Now let's test our program one more time. 
So, quit now our program terminates and we don't see that message beautiful. 
So let's fix the last problem. 
You saw that when we typed help, these guidelines appeared with so much in indentation, and here's the reason, look, right here in our code, they are already indented. 
So when we use triple quotes, what we type here will be printed exactly as is. 
So, because we have an indentation here, this indentation will also be printed on the terminal.
So, let's delete these okay, run the program one more time, type help, the indentation is gone. 
Beautiful. 
Now here's a challenge for you. 
I want you to take this program to the next level. 
So right now if we type start we get this message car started. 
And if we type start again we get the same message. 
It would be better if we got a message like car is already started so it doesn't make sense to start a car twice. 
Similarly, if we type stop it says car stopped, if we type it again we get the exact same message, it doesn't make sense to stop the car twice. 
So here's what I need you to do if the car is stopped and the user tries to stop it again, the program should say hey, the car is already stopped, what are you doing? And similarly if the car is already started and the user tries to start it again, the program should yell at the user. 
So go ahead and make the necessary changes to implement this scenario.
Alright to add this to our program, we need to know if the car is started or not. 
So there is one more piece of information we need to store in the memory. 
What is the kind of data we need to store here? A boolean. 
Is the car started or not, it's a matter of yes or no. 
True or false. 
So on the top, here we can define another variable like started and initially we set it to false. 
So the car is not started, right? Now when the user types the start command, here we need to check to see if the car is already started. 
If not the we'll start it or otherwise we'll yell at the user. 
So in this block we'll write another if statement, if it's already started and we print car is already started. 
Otherwise, so if you add an el statement here. 
And at this point, you set started to true. 
So we start the car and we print this message, okay? Now we need to make a similar change for the stop command. 
So if the car is already stopped we need to print a different message. 
If not started, so here we're using the not operator to see if the car is stopped. 
So if it's not started that means it's stopped, okay? So if it stopped we print car is already stopped with double p's, otherwise so else we need to stop the car, how do we do that? We set started to false. 
And then we'll print this message.
As easy as that. 
Let's go ahead and run our program.
So, initially our car is stopped. 
So I'm going to type stop, it says the car is already stopped, so lets start it, okay, now our car is started, let's start it one more time. 
The program is yelling at us. 
So we can not start the car twice. 
Beautiful. 
Now let's stop it it says the car is stopped, let's stop it one more time, we get this message
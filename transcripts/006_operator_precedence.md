#Operator Precedence

Now let me ask you a question, I'm going to clear all this code here to define x and set it to 10 plus 3 times 2. 
What do you think is the result of this expression? This is a very basic math question that unfortunately a lot of people fail to answer.
The answer is 16. 
Because in math we have this concept called operator precedence which means the order of operations. 
So the multiplication operator has a higher precendence which means it's applied first which means 3 x 2 is executed first, the result is 6 and then its added to 10, that's why x showed up as 16 after we run this code, let's verify that. 
So, print x the program, x is 16. 
So this is what we call operator precedence, it's just a basic math concept.
It's not about python programming language. 
So all the other programming languages behave the same way, so here's the order, first we have the exponentiation which is the power, like 2 to the power of 3, hen we have multiplication or division and finally we have addition or subtraction.
This is the order of operations. 
Let me show you another example.
Here I'm going to add the exponentiation operator, so, 2 to the power of 2. 
Once again, what do you think is the result of this expression? Pause the video and think about it for a few seconds.
The answer is 22.
Because the exponentiation operator takes precedence, so first 2 to the power of 2 is executed, the result is 4, then 4 is multiplied by 3, that is 12, and finally 12 is added to 10. 
So x should be 22.
So let's run this program and verify this. 
So I'm going to delete these lines here. 
Run the program, there you go. 
X is 22. 
Now let me bring back these rules here.
We can also use parenthesis to change the order of operations so if we have parenthesis we always takes priority. 
In this case we can add parenthesis around 10 + 3, so this piece of 3 will be executed first, the result is 13, then the exponentiation operator will be executed, so 2 to the power of 2 is 4, and finally 4 is multiplied by 13.
Now here is a little exercise for you. 
I'm going to set x to parenthesis 2 + 3 x 10 minus 3. 
What is the result of this? Pause the video and think about it for a few seconds.
So you learned that parenthesis always overrides the order, so this piece of code is executed first. 
The result of these 5. 
Then, between the multiplication and subtraction, you know that multiplication takes precedence.
So next, 5 will be multiplied by 10, the result is 50 and finally we have subtraction. 
So 50 minus 3 will be 47. 
Let's verify this, print x, run the program there you go, I hope you guessed it right.
So this is all bout operator precedence, it's a very important topic and I see it quite often in Python tests. 
So if you're preparing for a Python test.
#Logical Operators

In this tutorial I'm going to talk to you about the logical operators within Python.
We use these operators in situations where we have multiple conditions. 
Here is an example. 
Let' say we're building an application for processing loans. 
If an applicant has high income and good credit, then they're eligible for a loan. 
So in this example we have two conditions, one is having high income and the other is having good credit. 
So if both these conditions are true, then the applicant is eligible for a loan.
So this is where we use the logical and operator.
We use this operator to combine two conditions, and by the way this is not specific to python programming language, pretty much any programming language that supports if statements also supports the logical operators.
So, back to our program, let's define two variables, has high income, we set this to true.
And another one has good credit, we also set this to true, now our if statement if has high income has true, and has good credit is also true, then we're going to print eligible for null. 
So this is where we're using the and operator. 
So if both these conditions are true then this message will be printed. 
If one of them is false, we're not going to see this message. 
Let's try this out. 
So I'm going to run this program so we see it eligible for loan, but if we change either of these conditions to false, and run the program again look, the message disappears.
So this is the logical and operator. 
We also have the logical or, and we want to use that in situations where we want to do certain things at least one of the conditions is true, for example let's change the rule for this program, such that if the applicant has high income, or good credit, then they're eligible for a loan, so if either or both these conditions are true then the candidate is eligible. 
Now back to our program we can plement this rule by using the logical or operator. 
So we simply replace and with or, now when we run this program we're going to see this message because at least one of our conditions is true, let's take a look. 
So the applicant is eligible for a loan for a loan because they have good credit. 
If you change this to false but set the other condition to true, we still see the same result, but if both these conditions are false then we're not going to see this message anymore. 
So this is the difference between these operators. 
With the logical and operator both conditions should be true, with the logical or operator at least one condition should be true we also have another logical operator called not and that basically inverses any boolean value we give it, if we give it, we give it a true boolean value it converts it to false. 
For example let's make up a new room, if applicant has good credit and doesn't have a criminal record then they're eligible for a loan. 
Let me show you how to implement this. 
So, we go back to our program, in this example we don't need a first variable for let's delete that. 
Let's set this variable to true we also define another variable like has criminal record. 
We set this to false.
Now, we want to check to see if this applicant has good credit and not a criminal record. 
This is where we use the not operator.
So, if they have good credit, and not criminal record. 
So, in this example, has criminal record is set to false, when we use the not operator this basically gets changed to true, so we have two conditions that are true.
Here's ones and here's another one. 
So our applicant is eligible for a loan. 
And when we run this program we see this familiar message. 
However if an applicant has a criminal record, so let's change this to true, now when we run this program we can see our applicant is not eligible because when we apply then operator on this variable, we'll get false. 
So true changes to false.
And we'll end up with two conditions, one that's true and the other is false. 
And that's why this message is not printed. 
So this is all about the logical operators in.
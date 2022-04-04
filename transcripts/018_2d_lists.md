#2D Lists

Run the program, we still get 10.
In this tutorial I'm going to talk to you guys about two dimensional lists in python. 
Two dimensional lists are extremely powerfully and they have a lot if applications in data science and machine learning. 
Here's an example, In math we have a concept called matrix, which is like a rectangular array of numbers, let me show you. 
So we have 1, 2, 3, 4, 5, 6, 7, 8, 9.
So we have a rectangular array of numbers. 
You have rows, and columns. 
So this is a 3 x 3 matrix in math. 
Now we can model this in python using a 2 dimensional list. 
A 2 dimensional list is a list where each item in that list is another list. 
So, you want to define a matrix. 
We set it to a list, each item in this list, is going to be another list, and that list represents the items in each row. 
So, the first item in our list is going to be another list, and in this other list we're going to have the values 1, 2, and 3. 
Now the second item in our matrix list, once again, we have a list, this list represents the items in the second row. 
So, 4, 5, and 6, and finally 7, 8 9. 
So as you can see we have a 2 dimensional list Each item in our outer list is another list.
Okay? So, this is how we can implement a matrix in python, now to access an individual item in our matrix, once again we use square brackets, let me delete this stuff, alright, so how do we access 1 here, well, you start with our list then we add square brackets first we need to go and get the first item in this list.
Right? So we pass 0, now this expression returns another list. 
That is the inner list. 
In this list, let's say you want to access the second item, so, once again we add square brackets, and we pass 1, that is the index of 2 in this list, alright.
So if we print this on the terminal we get 2. 
Okay? So using 2 square brackets we can access individual items in our matrix, and also we can modify these values using this syntax, so, before printing this, let's change this to 20, so matrix of 0, and 1, let's change it to 20, and then print it, there you go, it's modified, now here you can also use nested loops to iterate over all the items in this matrix. 
Let me show you. 
So, we start with a rows for the rows in matrix, so with this loop, we are iterating over our Matrix list, in each iteration row will contain 1 list, 1 item, okay? Now, here we need to use an inner loop. 
So we need to loop over this row which is a list of items. 
We can type out 4 item in row colon and print item. 
Okay? So, let's run this program,
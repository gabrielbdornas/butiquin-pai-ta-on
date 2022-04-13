#Unpacking

no where in your program you accidentally modify that list, then it's better to use a tuple, In this tutorial I'm going to show you a powerful feature we have in python called unpacking.
So lets find a tuple called coordinates and here we pass 3 values, 1, 2, 3. 
So you imagine these are the coordinates for x y and z. 
Now let's say we want to get these values and use them in a few expressions, a few complex expressions in our program. 
Maybe we want to include them as part of a large complex formula. 
So together we'll have to write code like this, coordinates of 0, then let's say we want to multiply this by coordinates of 1, and then multiply it by coordinates of 2, our code is getting a little bit too long, this is just a very simple example. 
But let's say we want to use these values in quite a few places in our program, a better approach is to get these values and store them in separate variables like we can get coordinates of 0, and store it in x, then you can get coordinates of 1 and store it in y.
And similarly we get coordinates of 2, and then store it in z. 
Now we started repeating coordinates of 2 or coordinates of 0 multiple times, we can simply work with these variables, x times y times z, that is better. 
Right? So nothing new so far. 
But in Python we have a powerful feature called unpacking and with that we can achieve the same result with far less code. 
So we can define our variables x, y, and z. 
And set them to our tuple. 
What we have on line 6 is exactly identical to what we have on lines 2-4.
So this is a shorthand to achieve the same result.
So let me delete this and explain how this code works.
When Python interpreter sees this statement, it will get the first item in this tuple and assign it to the variable. 
Then it will get the second item in this tuple, then similarly we get the third item in this tuple and assign it to the third variable we have here, so we are unpacking this tuple into 3 variables. 
Now if we print x you can see x is 1, similarly y is 2, there you go.
So this is unpacking. 
And by the way this is not limited to tuples, we can use this feature for lists as well. 
So, if I change parenthesis to square brackets, now coordinates is a list, so we can unpack our list into 3 variables
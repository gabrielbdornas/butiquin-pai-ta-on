#Lists

to print and l here.
Now in this tutorial we're going to take a closer look at lists.
So, I'm going to define a list of names, let's send them to John Bob Mosh Sarah and Mary. 
So, if you print this list here, what we see on the terminal look exactly like how we define our lists we have square brackets, and in between these square brackets we have our item our items, so we have 5 strings in this list.
So we can also access an individual element using an index just like how we can access an individual character in a string using an index.
So, here we type out square brackets, and specify an index. 
The index of the first item in this list is 0. 
So, let's run this program, there you go, we get Jon now if you want to print out the third element in this list it's index is 2, so names of 2, returns Mosh, now we can also pass a negative index here, so negative 1, refers to the last item in this list, that is Mary, let's run the program, there you go, we see Mary, if you pass negative 2, this returns the second item from the end of the list. 
So let's run the program, there you go, we get sarah, so this is exactly like accessing individual characters in a string. 
We can also use a colon to select a range of items, for example if you pass 2 colon. 
This will get all items starting from the index of 2, that is Mosh here all the way to the end of the string. 
So let's run this program there you go. 
We get this list with 3 items, Mosh, Sarah, and Mary. 
We can also specify an end index, let's say 4, so this will return all the items up to this index, but it doesn't include the item at this index.
So when we run this program we only see Mosh and Sarah, the item I've indexed 4which is the 5th element or 5th item in this list is not returned. 
So Mary
is not returned. 
And also here we have default values, so if you leave out the end index this expression is going to return all the items starting from the index of 2, to the end of the list or if you leave out the start index, this expression asumes 0 as the default index, so it will return all the items from the beginning to the end of the list. 
And by the way, just like strings, these square brackets here, don't modify our original list, they simply return a new list. 
For example, if we pass 2 here, you can see this returns a new list with 3 items.
So if you go back here and print our original list of names right after you can see it's not affected.
So here we want to use square brackets with a colon to select a range of items, we get a new list, and by the way we can also modify any of the elements in this like this. 
Now, let's print our list so, you can see the first item in this list is now data. 
So this is the basics of lists. 
And here's a exercise for you. 
I want you to write a program to find the largest number in your list. 
This is a fantastic exercise for beginners, so go ahead and spend a few minutes on this, then come back and continue watching.
Alright, let's define a list of numbers, numbers, with a bunch of random numbers 3, 6, 2, 8, 4 and 10.
Now to find the largest number in this list. 
We need to define another variable let's call it max, this variable will hold the largest number, now initially you want to assume the first item in this list is the largest number. 
So we set max to numbers of 0. 
We're only assuming that the first item is the largest number. 
Chances are our assumption is wrong. 
So we need to iterate over this list, we need to loop through it, get each item and compare it with max. 
If it's greater than Max, then we need to reset max to that number. 
So in the first iteration we get 3, and max is also 3. 
Is 3 greater than 3. 
No, so we move on, we get the second number, is 6, greater than 3? It is, so we need to reset max to 6. 
Once again, we continue, we get 2, these two greater than 6, no it's not, so we move on, then we get 8, is 8 greater than 6? It is, so we should reset max to 8.
That is pretty easy. 
So here we need a for loop, for number in numbers colon now we need too heck to see if this number is greater than max, so, if number is greater than max, max colon then we need to reset max, so max to this new number, that's all we had to do.
So, let's print max, and run our program we can see the largest number in this list is 10.
It doesn't matter whether this number is at the end of the list or the beginning.
So if I move 10 and put it right at the beginning we should still see the same result. 
Let's run our program, we still see 10, if I put this somewhere in the middle, our
program should still work. 
Let's put it right after 2.
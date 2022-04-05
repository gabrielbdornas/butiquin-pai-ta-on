#Tuples

6, 3,and 1. 
The duplicates are removed.
In this tutorial I'm going to talk to you guys about another important structure.
in Python called tuple. 
Tuples are similar to lists so we can use them to store a list of items. 
But unlike lists we can not modify them, we cannot add new items, we cannot remove existing items, we tuples are immutable. 
We cannot mutate or change them. 
So let me show you. 
So I'm going to start by defining a list of numbers, 1, 2, 3, 4, so we use square brackets to define lists and parenthesis to define tuples, so if we change this to parenthesis, 1, 2, 3. 
Now we have a tuple. 
So if we type numbers.
look here we don't have the append or insert methods, so we cannot add new items to this tuple.
We also don't have remove clear and pop, we cannot remove any of these items here. 
We only have two methods, count, and index. 
We use count to count the number of occurrences in an item, and index, to find the index of the first occurrence, of an item. 
So we can only get information about a tuple, we can't change it.
And by the way, these other methods that you see here, they start with two underscores, we refer to these as magic methods, they're more of an advanced topic, so they go beyond the scope of this tutorial. 
If you're interested to learn bout them. 
You can get my python course, I've covered them in detail.
So similar to lists you can address individual items using squre bracketts,s o we can get the first item like this and then print another terminal, there you go, the first item is 1, but if you try to change the first item we'll get an error, so, numbers of 0, we set it to 10 and run our program there you go. 
We get this type error, because the tuple object does not support item assignment. 
So we cannot mutate or change tuples, they are immutable. 
Now practically speaking, most of the time you'll be using lists, but tuples are also useful. 
If you want to create a list of items and make sure
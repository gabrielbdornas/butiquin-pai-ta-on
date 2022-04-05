#List Methods

the link is below this video, click the link, and get started.
In this tutorial, I'm going to talk to you guys about the list methods, or list functions. 
These are the operations that we can perform in a list. 
So let's define a list of numbers, here we pass a bunch of random numbers, like 5, 2, 1, 7, and 4. 
Now there are a number of things we can do with this list, we can add new items to it, we can remove existing items, we can check for the existence of an item these are the operations that we can perform on a list. 
So, the we type numbers, we can see all these functions or more accurately the methods that are available in our list objects.
So we can call the append method to add a new item to this list. 
Let's say 13. 
Actually, no it's not a good number.
I'm joking I'm not superstitious, so let's add 20, it doesn't really matter and then print our list when we run the program we can see 20 is added at the end of this list but what if you want to add a number somewhere in the middle, or at the beginning of our list? For that we use a different method, that is called insert. 
So, insert, now this method takes 2 values, let me show you. 
So when we open parenthesis look at this little tool tip above the insert method.
You see the first value that we need to pass here is an index, so this is the index at which we want to insert this new item. 
Let's say we want to add an item at the beginning of our list, so we passed our index position of 0, and then the second value is the actual object we want to add to this list. 
Let's say we want to add the number 10, now when we print this list you can see that the number 10 is placed at the beginning of the list and all the other items are pushed to the right. 
We can also remove an item so we call remove and pass the item that we want to remove 5. 
Now we print our list so we see 5 is gone, and we have 2, 1, 7, 4. 
If you want to remove all the items in the list, you can call the clear method, so, clear this method doesn't take any values, so, we simply call it and it empties our list, all the items are removed.
We also have another useful method called hop, and with this we can remove the last item in a list.
Let me show you. 
So, we run our program, you can see the number 4 is removed from the end of our list. 
Now if you want to check for the existence of an item in our list, you can call the index method.
So, we call index and pass a value here, like 5 and this returns the index of the first occurrence of this item. 
So let's print this on the terminal.
We don't need this line anymore. 
So the index of 5 is 0. 
What if we pass a number that doesn't exist in this list? Let's say 50? Run the program, we get an error. 
We get a value error. 
50 is not in the list. 
There is also another way to check for the existence of an item, we can use the in operator. 
So, let me show you we type our 15 in numbers, earlier we used the in operator with a string, we check for the existence of a character or a sequence of a character in a string, now here we're checking for the existence of 50 in the list of numbers, so let's print this, we get a boolean value, false, so unlike the index method, this expression, doesn't generate an error, so it's safer to use this. 
We also have another method for counting the occurances of an item, let's say we have another 5 over here.
Now we can call numbers.count and pass 5 and this should return 2 because we have 2 5s in this list.
Take a look. 
There you go. 
That is pretty useful now if you want to sort your lists you can call sort method. 
So, we call the sort method here, this method doesn't take any values so, look at he return value, that is none, none is an object in python that represents the absence of a value.
So this sort method doesn't really return any values it simply sorts this list, in place, so instead of printing the return value oft his method, we simply call it to sort our list and then print our list. 
Take a look.
Now, all the items are assorted in ascending order. 
We can also sort the items in descending order, so after we sort the list
we can call the reverse method. 
We can simply reverse our list. 
Now let's go ahead and run our program, take a look.
Our numbers are sorted in descending order.
And one last method I want to show you here that is pretty useful is the copy method. 
So copy, with this method you can get a copy of our list. 
So let's define another variable called numbers 2, now numbers 2, is a copy of our original list. 
So if you make any changes to our original list, if you add new items to it, if you remove existing items, these operations are not going to impact our second list.
Let me show you. 
So after we show you a copy of our numbers list let's add a new item to this list, so numbers.apphend ten. 
So the first list is updated, so now we have a new item in our first list, then lets print the second list.
Take a look, we don't have the number 10 here, because these are 2 independent lists. 
So these are all the operations that we can perform on lists. 
We can add new items to a list, we can remove exxisitn items, we can check for the existence of an item, we can sort our list, and copy them. 
Now here's an exercise for this tutorial, I want you to write a program, to remove the duplicates on our list.
Again, this is a fantastic exercise. 
So spend a few minutes on this and then come back and continue watching.
Alright let's say we have a list of numbers with a bunch of duplicates. 
So 2, 2, 4, 6, 6, 3, 4, 6, 1. 
We want to remove the duplicates. 
So we need to define another list let's call that new list. 
Initially we set it to an empty list. 
Then we need to iterate over our first list, get each item, and if we don't have that number in this unix list, then we'll add it to this second list.
As simple as that. 
So, for number in numbers, now we need to check to see if we have this number in the second list. 
So we use the in operator. 
If number not in units so if we don't have an operator in this units list, then we'll need to add it, so units.
apphend number, that's all we have to do.
So, let's go ahead and print the units list there you go. So you have 2, 4,
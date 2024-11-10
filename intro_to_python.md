#!/usr/bin/env python3
## Note: This script requires Python 3.12.7


# **Homework by Hemma Kargl**
## Course: **2024W 300160-1 Practical introduction to programming for biologists**
### Section: Intro to python

```python
# Exercise 1: print() function

# Exercise 1-a
# Let's start with a long time programming tradition and print "Hello World!" by typing it inside print() function.

"""
Replace "type here" on line 2 with "Hello World!"
print("type here")
"""

print('Hello World!')

# Exercise 1-b

# Now try to assign "Hello World!" to the variable my_text.

"""
# You can assign "Hello World!" to the variable below on line 3.

my_text=""
print(my_text)
"""

my_text='Hello World!'
print(my_text)

# Exercise 2: Variables - Practice assigning data to variables with these Python exercises.

# Exercise 2-a
# Below is a good example of mixing numbers and text inside the print() function
# Assign: 3 to variable glass_of_water.

"""
Type here. Assign a number to the variable: glass_of_water
glass_of_water=
print("I drank", glass_of_water, "glasses of water today.")
"""

glass_of_water= 3
print("I drank", glass_of_water, "glasses of water today.")

# Exercise 2-b :
# Let's try to see what happens after assigning a new value to our variable. Note that program gets executed line by line.
# Place the variable: glass_of_water inside the print function and observe what happens.

"""
Fill the print function so it prints glass_of_water
glass_of_water=3
glass_of_water=glass_of_water + 1
print()
"""

glass_of_water=3
glass_of_water=glass_of_water + 1
print(glass_of_water)

# Exercise 3: Data Types - Integer (int), string (str) and float are the most basic and fundamental building blocks of data in Python.

#Exercise 3-a
# Let's check out a simple integer example.

"""
#Assign an integer to the variable, then print it.

men_stepped_on_the_moon=
print()
"""

men_stepped_on_the_moon= 12
print()

# Exercise 3-b
# Now a string example.

"""
#Type a couple of words or a short sentence for your variable, then print it.

my_reason_for_coding=
print()
"""

my_reason_for_coding= "The quick brown fox jumps over the lazy dog."
print()

# Exercise 3-c
# Let's try to see what happens after assigning a new value to our variable. Note that program gets executed line by line.

"""
#Assign a float with 2 decimals to the variable below. If you don't wan't to search the value you can check out Hint 1.

global_mean_sea_level_2018=21

#Type your code here.
global_mean_sea_level_2018=


print(global_mean_sea_level_2018)
"""

global_mean_sea_level_2018=21.36
print(global_mean_sea_level_2018)

# Exercise 9: Strings - Basic string operations as well as many string methods can be practiced through 10+ Python String Exercises we have prepared for you.

# Exercise 9-a
# Assign the string below to the variable in the exercise.
# "It's always darkest before dawn."

"""
#Type your answer here.

str=""

print(str)
"""

str="It's always darkest before dawn."
print(str)

# Exercise 9-b
# By using first, second and last characters of the string, create a new string.

"""
str="It's always darkest before dawn."

#Type your answer here.

ans_1=

print(ans_1)
"""

str="It's always darkest before dawn."
ans_1=str[0]+str[1]+str[-1]
print(ans_1)

# Exercise 9-c
# Replace the (.) with (!)

"""
str="It's always darkest before dawn."

#Type your code here.



print(str)
"""

str="It's always darkest before dawn."
str = str.replace(".", "!")
print(str)

# Exercise 10: len() function - Python’s len function tells the length of an object. It’s definitely a must know and very useful in endless scenarios. Whether it’s manipulating strings or counting elements in a list, len function is constantly used in computer programming.

# Exercise 10-a
# Using len() function find out how many items are in the list.

"""
lst=[11, 10, 12, 101, 99, 1000, 999]

answer_1=


print(answer_1)
"""

lst=[11, 10, 12, 101, 99, 1000, 999]
answer_1=len(lst)
print(answer_1)

# Exercise 10-b
# len() function can also tell the length of a string.
# Find out the length of the string given below.

"""
msg="Be yourself, everyone else is taken."
#Type your code here.

msg_length=


print(msg_length)
"""

msg="Be yourself, everyone else is taken."
msg_length=len(msg)
print(msg_length)

# Exercise 10-c
# How many keys are there in the dictionary?

"""
dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
#Type your answer here.

ans_1=

print(ans_1)
"""

dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
ans_1=len(dict)
print(ans_1)

# Exercise 11: .sort() method - Practice sort method in Beginner Python Exercises and later on you’ll have the opportunity practice sorted function in Intermediate Python Exercises.

# Exercise 11-a
# Sort the list in ascending order with .sort() method.

"""
lst=[11, 100, 99, 1000, 999]

#Type your answer here.



print(lst)
"""

lst=[11, 100, 99, 1000, 999]
lst.sort()
print(lst)

# Exercise 11-b
# This time sort the countries in alphabetic order.

"""
lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]

#Type your code here.



print(lst)
"""

lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
lst.sort()
print(lst)

# Exercise 11-c
# Now sort the list in descending order with .sort() method.

"""
Exercise 11-c
Now sort the list in descending order with .sort() method.
"""

lst=[11, 100, 101, 999, 1001]
lst.sort(reverse = True)
print(lst)

# Exercise 12: .pop() method - A list method pop can be applied to Python list objects. It’s pretty straightforward but actually easy to confuse. These exercises will help you understand pop method better.

# Exercise 12-a: Python pop method of lists and dictionaries
# Pop the last item of the list below.

"""
lst=[11, 100, 99, 1000, 999]

#Type your answer here.

popped_item=
 
print(popped_item)
print(lst)
"""

lst=[11, 100, 99, 1000, 999]
popped_item=lst.pop()
print(popped_item)
print(lst)

# Exercise 12-b: Python pop method to remove last list item
# Remove "broccoli" from the list using .pop and .index methods.

"""
lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]

#Type your code here.


item=


print(lst, item)
"""

# My answer (was not indended like this):
lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
item=lst.pop(-2)
print(lst, item)

# Correction (added using index):
lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
b = lst.index(4)
item=lst.pop(b)
print(lst, item)

# Exercise 12-c: Pop method also saves the item being removed
# Save Italy's GDP in a separate variable and remove it from the dictionary.

"""
GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}

#Type your answer here.

italy_gdp=


print(GDP_2018)
print(italy_gdp, "trillion USD")
"""

GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}
italy_gdp= GDP_2018.pop("Italy")
print(GDP_2018)
print(italy_gdp, "trillion USD")
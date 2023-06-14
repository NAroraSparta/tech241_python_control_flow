```python

# Control flow

# Like giving Python a recipe to follow in certain order

# Conditional Statements
#age =10
age = str(input("input your age:  "))
print(age.lower())

if age >= 18:
    print("You can watch all movies.")
elif age >= 16:
    print("Sorry, you can not watch 18 rated movies, but you can watch all other movies.")
elif age >= 13:
    print("Sorry, you can not watch 18 and 15 rated movies, but you can watch all other movies.")
elif age >= 8:
    print("Sorry, you can not watch 18, 15 and 12 rated movies, but you can watch all other movies.")
else:
    print("You can only watch U rated movies.")
```
```python

#print(str(x) + str(y) + " " + z)
# print(white_space.lower())
```
```python

 # There are no case or switch statements in Python
 # You can only use if and else
```
```python
# # For loops and while loops
#
# # for and foreach in other languages
# # In Python we just use for
#
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Branson", "money": "$0.05"},
    2: {"name": "Masha", "money": "$3.66"},
    3: {"name": "Roscoe", "money": "$1.14"}
}

for num in list_data:
    print(num * 2)

# nested loops
for data in embedded_lists:
    # print(data)
    for num in data:
        # print(num)
        print(num * 2)

#looping through the dictionaries
for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)

# a loop that only returns the money values
for items in dict_data.values():
    print(items["money"])
```
```python
#loops and if statements

for num in list_data:
    if num == 3:
        print("You have found three!")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon!")
```
#
```python
# While loops

# x = 0

# while x < 10:
#     print(f"It's working -> {x}")
#     x += 1

# while x < 10:
#     print(f"It's working -> {x}")
#     if x == 4:
#         break
#     x += 1
```
```python

# Verifying user input

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 117 and int(age) != 0:
        user_prompt = False
    else:
        print("Please enter your age as a digit and under 117")

print(f"Your age is {age}")
```
```python
# Libraries

#Libraries are collections of functions (pre-built code) that do a job for you.
# We can import these libraries to make our own code easier to understand, be less complex and faster to write.

#######  Method 1 to import any library #################
# import random as rand
# print(rand.randint(1, 100))

#######  Method 2 to import any library #################
# from random import randint
# print(randint(1, 100))
#
# ####### Method 3 to import multiple libraries #################
from random import randint, random, randrange
import math

print(random())

num_float = 23.22
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
```

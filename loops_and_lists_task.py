# Make a loop with a range that says hello 10 times (research range please)

for x in range(10):
    print("Hello")

#Create another loop with a range that asks for names and appends to a list called list_names

list_names = []
for names in range(5):
    name = input("What is your name? ")
    list_names.append(name)

print(list_names)


# Make a loop that iterates over each name in list_name and format's it into lowercase in a new list called list_names_lower
list_names_lower = []
for names in range(5):
    name = input("What is your name? ")
    list_names_lower.append(name.lower())

print(list_names_lower)

#Make a list of numbers, iterate over the list of values to find if they are even. Print the even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)



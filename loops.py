# # For loops and while loops
#
# # for and foreach in other languages
# # In Python we just use for
#
# list_data = [1, 2, 3, 4, 5]
# embedded_lists = [[1, 2, 3], [4, 5, 6]]
# dict_data = {
#     1: {"name": "Branson", "money": "$0.05"},
#     2: {"name": "Masha", "money": "$3.66"},
#     3: {"name": "Roscoe", "money": "$1.14"}
# }
#
# for num in list_data:
#     print(num * 2)
#
# # nested loops
# for data in embedded_lists:
#     # print(data)
#     for num in data:
#         # print(num)
#         print(num * 2)
#
# #looping through the dictionaries
# for item in dict_data.values():
#     for embed_value in item.values():
#         print(embed_value)
#
# # a loop that only returns the money values
# for items in dict_data.values():
#     print(items["money"])
#
# #loops and if statements
#
# for num in list_data:
#     if num == 3:
#         print("You have found three!")
#     elif num > 3:
#         print("Gone too far!")
#     else:
#         print("Too soon!")
#
#
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

# Verifying user input

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 117 and int(age) != 0:
        user_prompt = False
    else:
        print("Please enter your age as a digit and under 117")

print(f"Your age is {age}")


user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) <= 117 and int(age) != 0:
        user_prompt = False
    else:
        print("Please enter your age as a digit and between 1 and 117")
if int(age) >= 18:
    print("You can watch all movies.")
elif int(age) >= 16:
    print("Sorry, you can not watch 18 rated movies, but you can watch all other movies.")
elif int(age) >= 13:
    print("Sorry, you can not watch 18 and 15 rated movies, but you can watch all other movies.")
elif int(age) >= 8:
    print("Sorry, you can not watch 18, 15 and 12 rated movies, but you can watch all other movies.")
else:
    print("You can only watch U rated movies.")




# Write a program that asks the user for a number.
# If the number is odd print "The number is odd!" and if it is even print "The number is even".
#
# FizzBuzz - Write a program that prints numbers from 1 - 100
# but for multiples of 3 print "Fizz" and
# for multiples of 5 print "Buzz".
# For multiples of 3 and 5 print "FizzBuzz
#
# Bonus, can you make FizzBuzz use a loop?

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

while number >=1 and number <=100:
   if (number % 3) == 0 and (number % 5) == 0:
       print("FizzBuzz")
   elif number % 3 == 0:
       print("Fizz")
   elif number % 5 == 0:
       print("Buzz")
   else:
       print(number)
   break



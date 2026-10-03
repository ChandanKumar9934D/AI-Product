# Write a program that converts the string "25" into an integer inside a try block. Print the number. If a ValueError occurs, print "Invalid number".

stringNumber='25'

try:
    print(int(stringNumber))

except ValueError:
    print("Invalid number")

# Write a program that divides 10 by 0. Use try and except ZeroDivisionError to print "Cannot divide by zero" instead of letting the program stop with an unhandled error.

try:
    print(10/0)

except ZeroDivisionError:
    print("Cannot divide by zero")
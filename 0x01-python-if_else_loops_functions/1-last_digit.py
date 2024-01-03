#!/usr/bin/python3
import random
number_temp = 0
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    number_temp = 1
l_digit = number % 10
result = "and is greater than 5" if l_digit > 5 else ("and is 0" if l_digit == 0 else "and is less than 6 and not 0")
l_digit = l_digit * -1 if number_temp == 1 else l_digit
number = number * -1 if number_temp == 1 else number
print("Last digit of {} is {} and {}".format(number, l_digit, result))

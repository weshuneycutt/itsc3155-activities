# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.

# Part A. odd_range
# Define a function odd_range(num1, num2) that takes a starting number (num1) and an ending number (num2)
# and returns all odd numbers as an array between num1 (inclusive) and num2 (exclusive)
from pickle import FALSE, TRUE


def odd_range(num1, num2):
  odd_numa = []
  for i in range (num1, num2):
    if i % 2 ==1: 
      odd_numa.append(i)


  return odd_numa

# Part B. has_lower_case
# Define a function has_lower_case(s) that takes a string s
# and checks if string s contains a lower case char.
# The function should return True indicating that string s has a lower case char
# otherwise return False
def has_lower_case(s):
  # YOUR CODE HERE

  for x in range (0, len(s)):
    if ord(s[x]) >= 97 and ord(s[x])<= 122:
      return True
  return False

# Part C. fizz_buzz
# Define a function fizz_buzz(num) that takes an integer num
# and returns a string based on the following criteria:

# if num is divisible by 3 return "Fizz"
# if num is divisible by 5 return "Buzz"
# if num is divisible by 3 and 5 return "FizzBuzz"

# if num is does not meet any of the above criteria or is less than
# or equal to 0 return the num as a string
def fizz_buzz(num):
  # YOUR CODE HERE
  if num % 15 == 0 and num > 0: 
    return "FizzBuzz"
  if num % 5 == 0 and num > 0:
    return "Buzz"
  if num % 3 == 0 and num > 0: 
    return "Fizz" 

  return str(num)

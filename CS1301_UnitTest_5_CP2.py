#Remember that Fibonacci's sequence is a sequence of numbers
#where every number is the sum of the previous two numbers.
#
#Rosieacci numbers are similar to Fibonacci numbers, but
#with two differences:
#
# - Fibonacci numbers are famous, Rosieacci numbers are not.
# - In Rosieacci numbers, the most recent number is added
#   twice. A given Rosieacci number is the sum of two times
#   the preceding number, plus the number before it.
#
#The Rosieacci sequence starts with two 1s (the base cases).
#Then, the third number is the sum of the first and twice the
#second (1 + 1 + 1 = 3). The fourth number is the sum of the
#second and twice the third (1 + 3 + 3 = 7). The fifth number
#is the sum of the third and twice the fourth (3 + 7 + 7 = 17).
#The sixth number is the sum of the fourth and twice the fifth
#(7 + 17 + 17 = 41). And so on.
#
#The first several Rosieacci numbers (and their indices) are
#thus:
#
# 1  1  3  7 17 41 99 239 577 1393 3363 8119
# 1  2  3  4  5  6  7   8   9   10   11   12
#
#Write a function called rosieacci that returns the nth
#Rosieacci number. For example:
#
# rosieacci(5) -> 17
# rosieacci(12) -> 8119
#
#We recommend implementing rosieacci recursively, but it
#is not required.


#Write your code here!

def rosieacci(n):
    # Base cases
    if n == 1 or n == 2:
        return 1
    return rosieacci(n - 1) * 2 + rosieacci(n - 2)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 17, then 8119
print(rosieacci(5))
print(rosieacci(12))




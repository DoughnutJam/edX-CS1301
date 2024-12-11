#Write a function called bananafy. bananafy should take one
#parameter, a string. bananafy should replace every vowel in
#the string with the previous vowel from the alphabet: e should
#become a, i should become e, o should become i, and u should
#become o. a should, in turn, become u. This should be done
#for both capital and lower-case vowels. Then, bananafy should
#return the result.
#
#For example:
#
# bananafy("banana") -> "bununu"
# bananafy("benene") -> "banana"
# bananafy("AEIOU") -> "UAEIO"
# bananafy("Four Score And Seven Years") -> "Fior Scira Und Savan Yaurs"

#Write your function here!

def bananafy(string):
    lower_vowels = ['a','e','i','o','u']
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    new_string = ''

    for letter in string:
        if 97 <= ord(letter) <= 122:
            if letter in lower_vowels:
                try:
                    index_new_letter = lower_vowels.index(letter)+-1
                    new_string += lower_vowels[index_new_letter]
                except IndexError as e:
                    new_string += lower_vowels[-1]
            else:
                new_string += letter

        elif 65 <= ord(letter) <= 90:
            if letter in upper_vowels:
                try:
                    index_new_letter = upper_vowels.index(letter) + -1
                    new_string += upper_vowels[index_new_letter]
                except IndexError as e:
                    new_string += upper_vowels[-1]
            else:
                new_string += letter
        else:
            new_string += letter

    return new_string



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print the same results as in the examples above.

print(bananafy("banana"))
print(bananafy("benene"))
print(bananafy("AEIOU"))
print(bananafy("Four Score And Seven Years"))




#One of the early common methods for encrypting text was the
#Playfair cipher. You can read more about the Playfair cipher
#here: https://en.wikipedia.org/wiki/Playfair_cipher
#
#The Playfair cipher starts with a 5x5 matrix of letters,
#such as this one:
#
# D A V I O
# Y N E R B
# C F G H K
# L M P Q S
# T U W X Z
#
#To fit the 26-letter alphabet into 25 letters, I and J are
#merged into one letter. When decrypting the message, it's
#relatively easy to tell from context whether a letter is
#meant to be an i or a j.
#
#To encrypt a message, we first remove all non-letters and
#convert the entire message to the same case. Then, we break
#the message into pairs. For example, imagine we wanted to
#encrypt the message "PS. Hello, worlds". First, we could
#convert it to PSHELLOWORLDS, and then break it into letter
#pairs: PS HE LL OW OR LD S. If there is an odd number of
#characters, we add X to the end.
#
#Then, for each pair of letters, we locate both letters in
#the cipher square. There are four possible orientations
#for the pair of letters: they could be in different rows
#and columns (the "rectangle" case), they could be in the
#same row but different columns (the "row" case), they could
#be in the same column but different rows (the "column"
#case), or they could be the same letter (the "same" case).
#
#Looking at the message PS HE LL OW OR LD SX:
#
# - PS is the Row case: P and S are in the same row.
# - HE is the Rectangle case: H and E are in different rows
#   and columns of the square.
# - LD is the Column case: L and D are in the same column.
# - LL is the Same case as it's two of the same letter.
#
#For the Same case, we replace the second letter in the pair
#with X, and then proceed as normal. When decrypting, it
#would be easy to see the our result was not intended to be
#PS HELXO WORLDSX, and we would thus assume the X is meant to
#repeat the previous letter, becoming PS HELLO WORLDSX.
#
#What we do for each of the other three cases is different:
#
# - For the Rectangle case, we replace each letter with
#   the letter in the same row, but the other letter's
#   column. For example, we would replace HE with GR:
#   G is in the same row as H but the same column as E,
#   and R is in the same row as E but the same column as
#   H. For another example, CS would become KL: K is in
#   C's row but S's column, and L is in C's column but S's
#   row.
# - For the Row case, we pick the letter to the right of
#   each letter, wrapping around the end of the row if we
#   need to. PS becomes QL: Q is to the right of P, and L
#   is to the right of S if we wrap around the end of the
#   row.
# - For the Column case, we pick the letter below each
#   letter, wrapping around if necessary. LD becomes TY:
#   T is below L and Y is below D.
#
#We would then return the resultant encrypted message.
#
#Decrypting a message is essentially the same process.
#You would use the exact same cipher and process, except
#for the Row and Column cases, you would shift left and up
#instead of right and down.
#
#Write two methods: encrypt and decrypt. encrypt should
#take as input a string, and return an encrypted version
#of it according to the rules above.
#
#To encrypt the string, you would:
#
# - Convert the string to uppercase.
# - Replace all Js with Is.
# - Remove all non-letter characters.
# - Add an X to the end if the length if odd.
# - Break the string into character pairs.
# - Replace the second letter of any same-character
#   pair with X (e.g. LL -> LX).
# - Encrypt it.
#
#decrypt should, in turn, take as input a string and
#return the unencrypted version, just undoing the last
#step. You don't need to worry about Js and Is, duplicate
#letters, or odd numbers of characters in decrypt.
#
#For example:
#
# encrypt("PS. Hello, world") -> "QLGRQTVZIBTYQZ"
# decrypt("QLGRQTVZIBTYQZ") -> "PSHELXOWORLDSX"
#
#HINT: You might find it easier if you implement some
#helper functions, like a find_letter function that
#returns the row and column of a letter in the cipher.
#
#HINT 2: Once you've written encrypt, decrypt should
#be trivial: try to think of how you can modify encrypt
#to serve as decrypt.
#
#To make this easier, we've gone ahead and created the
#cipher as a 2D tuple for you:
CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))



#Add your code here!

def encrypt(string):

    # Attempt 2
    def find_row_column(letter): # Column starts at 0. Use this to find the row and column for each letter in a pair
        for row in range(0, len(CIPHER)):
            if letter in CIPHER[row]:
                return True, row, CIPHER[row].index(letter)

    def same_row(input_pair): # Check to see if the letters in input pair are in the same row
        pair_one_row = find_row_column(input_pair[0])[1]
        pair_two_row = find_row_column(input_pair[1])[1]

        if pair_one_row == pair_two_row:
            # print("Row")
            return True
        else:
            return False

    def same_column(input_pair): # Check to see if the letters in the input pair are in the same column
        pair_one_column = find_row_column(input_pair[0])[2]
        pair_two_column = find_row_column(input_pair[1])[2]

        if pair_one_column == pair_two_column:
            # print("Column")
            return True
        else:
            return False

    def same_letter(input_pair): # Check to see if the letters in the input pair are the same.
        if input_pair[0] == input_pair[1]:
            # print("Same letter")
            return True
        else:
            return False

    def rectangle_case(input_pair): # Check to see if it's a rectangle case
        if not same_row(input_pair) and not same_column(input_pair):
            # print("Rectangle Case")
            return True
        else:
            return False

    # Initial Transformations for base case letter

    upper_string = string.upper()
    replace_j = upper_string.replace('J', 'I')
    non_letter_removal = [letter for letter in replace_j if 65 <= ord(letter) <= 90]
    if len(non_letter_removal) % 2 == 0:
        pass
    else:
        non_letter_removal.append('X')

    # Change the base case into pairs

    character_pairs = []
    for index in range(0, len(non_letter_removal), 2):
        index_2 = index + 1
        pair = str(non_letter_removal[index]) + str(non_letter_removal[index_2])
        character_pairs.append(pair)


    # Checking each case and applying transformations

    encrypted = ''
    for pair in character_pairs:
        new_test_pair = pair
        same_letter_test = same_letter(pair)
        if same_letter_test:
            new_test_pair = f'{pair[0]}X'

        same_row_test = same_row(new_test_pair)
        same_column_test = same_column(new_test_pair)
        rectangle_case_test = rectangle_case(new_test_pair)


        if same_row_test:
            for letter in new_test_pair:
                letter_bool, letter_row, letter_column = find_row_column(letter)
                if letter_column+1 > len(CIPHER[letter_row])-1:
                    encrypted += f'{CIPHER[letter_row][0]}'
                else:
                    encrypted += f'{CIPHER[letter_row][letter_column+1]}'
        elif same_column_test:
            for letter in new_test_pair:
                letter_bool, letter_row, letter_column = find_row_column(letter)
                if letter_row+1 > len(CIPHER)-1:
                    encrypted += f'{CIPHER[0][letter_column]}'
                else:
                    encrypted += f'{CIPHER[letter_row+1][letter_column]}'
        elif rectangle_case_test:
            letter_one_bool, letter_one_row, letter_one_column = find_row_column(new_test_pair[0])
            letter_two_bool, letter_two_row, letter_two_column = find_row_column(new_test_pair[1])
            encrypted += f'{CIPHER[letter_one_row][letter_two_column]}{CIPHER[letter_two_row][letter_one_column]}'
        else:
            print(f'Error with {new_test_pair}')


    return encrypted

def decrypt(string):

    # Attempt 2
    def find_row_column(letter): # Column starts at 0. Use this to find the row and column for each letter in a pair
        for row in range(0, len(CIPHER)):
            if letter in CIPHER[row]:
                return True, row, CIPHER[row].index(letter)

    def same_row(input_pair): # Check to see if the letters in input pair are in the same row
        pair_one_row = find_row_column(input_pair[0])[1]
        pair_two_row = find_row_column(input_pair[1])[1]

        if pair_one_row == pair_two_row:
            # print("Row")
            return True
        else:
            return False

    def same_column(input_pair): # Check to see if the letters in the input pair are in the same column
        pair_one_column = find_row_column(input_pair[0])[2]
        pair_two_column = find_row_column(input_pair[1])[2]

        if pair_one_column == pair_two_column:
            # print("Column")
            return True
        else:
            return False

    def same_letter(input_pair): # Check to see if the letters in the input pair are the same.
        if input_pair[1] == 'X':
            return f'{input_pair[0]}X'
        else:
            return input_pair

    def rectangle_case(input_pair): # Check to see if it's a rectangle case
        if not same_row(input_pair) and not same_column(input_pair):
            # print("Rectangle Case")
            return True
        else:
            return False

    # Initial Transformations for base case letter

    upper_string = string.upper()
    replace_j = upper_string.replace('J', 'I')
    non_letter_removal = [letter for letter in replace_j if 65 <= ord(letter) <= 90]
    if len(non_letter_removal) % 2 == 0:
        pass
    else:
        non_letter_removal.append('X')

    # Change the base case into pairs

    character_pairs = []
    for index in range(0, len(non_letter_removal), 2):
        index_2 = index + 1
        pair = str(non_letter_removal[index]) + str(non_letter_removal[index_2])
        character_pairs.append(pair)


    # Checking each case and applying transformations

    decrypted = ''
    for pair in character_pairs:
        new_test_pair = pair

        same_row_test = same_row(new_test_pair)
        same_column_test = same_column(new_test_pair)
        rectangle_case_test = rectangle_case(new_test_pair)

        if same_row_test:
            new_letters = ''
            for letter in new_test_pair:
                letter_bool, letter_row, letter_column = find_row_column(letter)
                if letter_column-1 < 0:
                    new_letters += f'{CIPHER[letter_row][-1]}'
                else:
                    new_letters += f'{CIPHER[letter_row][letter_column-1]}'

            # print(f'Pair to decrypt {new_test_pair}\n Row\n Test Results {new_letters}')
            decrypted += same_letter(new_letters)

        elif same_column_test:
            new_letters = ''
            for letter in new_test_pair:
                letter_bool, letter_row, letter_column = find_row_column(letter)
                if letter_row-1 < 0:
                    new_letters += f'{CIPHER[-1][letter_column]}'
                else:
                    new_letters += f'{CIPHER[letter_row-1][letter_column]}'

            # print(f'Pair to decrypt {new_test_pair}\n Column\n Test Results {new_letters}')
            decrypted += same_letter(new_letters)

        elif rectangle_case_test:
            new_letters = ''
            letter_one_bool, letter_one_row, letter_one_column = find_row_column(new_test_pair[0])
            letter_two_bool, letter_two_row, letter_two_column = find_row_column(new_test_pair[1])
            new_letters += f'{CIPHER[letter_one_row][letter_two_column]}{CIPHER[letter_two_row][letter_one_column]}'
            # print(f'Pair to decrypt {new_test_pair}\n Rec\n Test Results {new_letters}')
            decrypted += same_letter(new_letters)
        else:

            print(f'Error with {new_test_pair}')



    return decrypted
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: QLGRQTVZIBTYQZ, then PSHELXOWORLDSX
# print(encrypt("PS. Hello, world"))
# print(decrypt("QLGRQTVZIBTYQZ"))
#
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: QLGRQTVZIBTYQZ, then PSHELXOWORLDSX
print(encrypt("PS. Hello, worlds"))
print(decrypt("QLGRQTVZIBTYQZ"))


#In the playground game 500, players compete to earn 500
#points. To win a round, they must also win by at least
#50 points. If a player reaches 500 points but another
#player has more than 450 points, play continues until one
#player has 500 or more points and a 50-point lead on
#the next-highest score.
#
#Write a function called check_winner. check_winner should
#have one parameter, a list of integers. There will be at
#least two integers, but there may be as many as 12.
#
#If one of the integers represents a winning score (meaning
#that it is over 500 and more than 50 points ahead of second
#place), check_winner should return "Winning score: X", where
#X is replaced by the winning score.
#
#If no player has won yet (meaning that either no one is
#over 500 points, or that fewer than 50 points separate
#first and second place), check_winner should return the
#string "Keep playing!"


#Write your function here!

def check_winner(int_list):
    sort_scores = sorted(int_list, reverse=True)
    first_place = sort_scores[0]
    second_place = sort_scores[1]
    score_delta = first_place - second_place
    if first_place >= 500 and score_delta >= 50:
        return f'Winning score: {first_place}'

    return "Keep playing!"




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will output:
#Winning score: 500
#Winning score: 500
#Keep playing!
#Winning score: 575
#Keep playing!
print(check_winner([100, 200, 300, 400, 500]))
print(check_winner([500, 450, 400, 350, 300, 250, 200, 150, 100]))
print(check_winner([500, 470, 320]))
print(check_winner([575, 470]))
print(check_winner([575, 565, 320, 210, 200]))
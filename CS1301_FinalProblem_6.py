# Let's try out a sort of data analysis-style problem. In
# this problem, you're going to have access to a data set
# covering Georgia Tech's all-time football history. The data
# will be a CSV file, meaning that each line will be a comma-
# separated list of values. Each line will describe one game.
# The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent
#
# If Points For is greater than Points Against, then Georgia
# Tech won the game. If Points For is less than Points Against,
# then Georgia Tech lost the game. If the two are equal, then
# the game was a tie.
#
# You can see a subsection of this dataset in season2016.csv
# in the top left, but the actual dataset you'll be accessing
# here will have 1237 games.
#
# Write a function called all_time_record. all_time_record
# should take as input a string representing an opposing team
# name. It should return a string representing the all-time
# record between Georgia Tech and that opponent, in the form
# Wins-Losses-Ties. For example, Georgia Tech has beaten
# Clemson 51 times, lost 28 times, and tied 2 times. So,
# all_time_record("Clemson") would return the string "51-28-2".
#
# We have gone ahead and started the function and opened the
# file for you. The first line of the file are headers:
# Date,Opponent,Location,Points For,Points Against. After that,
# every line is a game.


def all_time_record(opponent):
    opponent_games = {}
    def game_inputs(game_details):
        opp_name = game_details[1]
        gt_points = int(game_details[3])
        opp_points = int(game_details[4])
        return opp_name, gt_points, opp_points

    with open('../resource/lib/public/georgia_tech_football.csv', 'r') as record_file:
        contents = record_file.readlines()[1:]
        for line in contents:
            game_dict = {}
            clean_line = line.strip()
            game_details = clean_line.split(',')
            opponent_name, points_for_gt, points_against_gt = game_inputs(game_details)
            if opponent_name not in opponent_games:
                opponent_games[opponent_name] = {}
                opponent_games[opponent_name]["GT_win"] = 0
                opponent_games[opponent_name]["GT_loss"] = 0
                opponent_games[opponent_name]["GT_tie"] = 0
                if points_against_gt > points_for_gt:
                    opponent_games[opponent_name]["GT_loss"] += 1
                elif points_against_gt < points_for_gt:
                    opponent_games[opponent_name]["GT_win"] += 1
                else:
                    opponent_games[opponent_name]["GT_tie"] += 1
            else:
                if points_against_gt > points_for_gt:
                    opponent_games[opponent_name]["GT_loss"] += 1
                elif points_against_gt < points_for_gt:
                    opponent_games[opponent_name]["GT_win"] += 1
                else:
                    opponent_games[opponent_name]["GT_tie"] += 1

    if opponent_name in opponent_games:
        wins = opponent_games[opponent]["GT_win"]
        loss = opponent_games[opponent]["GT_loss"]
        ties = opponent_games[opponent]["GT_tie"]
        return f"{wins}-{loss}-{ties}"
    else:
        return "0-0-0"


    # return opponent_games
            #
            # if game_details[game_name]["Points for GT"] > game_details[game_name]["Points Against GT"]:
            #     GT_win += 1
            # elif game_details[game_name]["Points for GT"] < game_details[game_name]["Points Against GT"]:
            #     GT_loss += 1
            # else:
            #     GT_tie += 1







    # Add some code here! Don't forget to close the file when
    # you're done reading from it, before returning.


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 51-28-2, 51-33-1, and 29-21-3, each on a separate
# line.
# print(all_time_record("Clemson"))
# print(all_time_record("Duke"))
# print(all_time_record("North Carolina"))


var_1, var_2, var_3 = ("habib", 2, 3)
print(var_1)


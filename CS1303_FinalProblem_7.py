from datetime import datetime
def read_data():
    opponent_games = {}

    def game_inputs(game_details):
        game_date = datetime.strptime(game_details[0], "%Y-%m-%d")
        opp_name = game_details[1]
        loc = game_details[2]
        gt_points = int(game_details[3])
        opp_points = int(game_details[4])
        return game_date, opp_name, loc, gt_points, opp_points

    with open('../resource/lib/public/georgia_tech_football.csv', 'r') as record_file:
        contents = record_file.readlines()[1:]
        for line in contents:
            clean_line = line.strip()
            game_details = clean_line.split(',')
            g_date, opponent_name, location, points_for_gt, points_against_gt = game_inputs(game_details)

            # Data to Dict
            if opponent_name not in opponent_games:
                opponent_games[opponent_name] = []
                opponent_games[opponent_name].append({
                    "Game Date": g_date,
                    "Opponent Name": opponent_name,
                    "Location": location,
                    "Points for GT": points_for_gt,
                    "Points Against GT": points_against_gt
                })
            else:
                opponent_games[opponent_name].append({
                    "Game Date": g_date,
                    "Opponent Name": opponent_name,
                    "Location": location,
                    "Points for GT": points_for_gt,
                    "Points Against GT": points_against_gt
                })

    #First team GT ever played against?
    # min_date = datetime.max
    # min_date_team = None
    # for team, games in opponent_games.items():
    #     for game in games:
    #         if game["Game Date"] < min_date:
    #             min_date = game["Game Date"]
    #             min_date_team = team

    #Points scored on Auburn all-time?
    # points_on_auburn = 0
    # for team, games in opponent_games.items():
    #     if team == "Auburn":
    #         for game in games:
    #             points_on_auburn += game["Points for GT"]

    # Points scored by Auburn all-time?
    # points_by_auburn = 0
    # for team, games in opponent_games.items():
    #     if team == "Auburn":
    #         for game in games:
    #             points_by_auburn += game["Points Against GT"]

    #Georgia Tech's all time record in home games?
    # GT_win = 0
    # GT_loss = 0
    # GT_tie = 0
    # for team, games in opponent_games.items():
    #     for game in games:
    #         if game["Location"] == "Home":
    #             if game["Points for GT"] > game["Points Against GT"]:
    #                 GT_win += 1
    #             elif game["Points for GT"] < game["Points Against GT"]:
    #                 GT_loss += 1
    #             else:
    #                 GT_tie += 1
    # Georgia Tech's all time record in games in 2009?
    # GT_win = 0
    # GT_loss = 0
    # GT_tie = 0
    # for team, games in opponent_games.items():
    #     for game in games:
    #         if game["Game Date"].year == 2009:
    #             if game["Points for GT"] > game["Points Against GT"]:
    #                 GT_win += 1
    #             elif game["Points for GT"] < game["Points Against GT"]:
    #                 GT_loss += 1
    #             else:
    #                 GT_tie += 1
    #
    # return f"{GT_win}-{GT_loss}-{GT_tie}"

    # Georgia Tech's all time record in games in Oct?
    # GT_win = 0
    # GT_loss = 0
    # GT_tie = 0
    # for team, games in opponent_games.items():
    #     for game in games:
    #         if game["Game Date"].month == 10:
    #             if game["Points for GT"] > game["Points Against GT"]:
    #                 GT_win += 1
    #             elif game["Points for GT"] < game["Points Against GT"]:
    #                 GT_loss += 1
    #             else:
    #                 GT_tie += 1
    #
    # return f"{GT_win}-{GT_loss}-{GT_tie}"

    # Georgia Tech's all time record in games in SEC 1933 to 1963?
    # GT_win = 0
    # GT_loss = 0
    # GT_tie = 0
    # for team, games in opponent_games.items():
    #     for game in games:
    #         if 1963 >= game["Game Date"].year >= 1933:
    #             if game["Points for GT"] > game["Points Against GT"]:
    #                 GT_win += 1
    #             elif game["Points for GT"] < game["Points Against GT"]:
    #                 GT_loss += 1
    #             else:
    #                 GT_tie += 1
    #
    # return f"{GT_win}-{GT_loss}-{GT_tie}"
    # Team GT scored the most points?

    # GT_most_points_against_team = None
    # points_scored = 0
    # for team, games in opponent_games.items():
    #     GT_most_points = 0
    #     for game in games:
    #         points_scored += game["Points for GT"]
    #     if points_scored > GT_most_points:
    #         GT_most_points = points_scored
    #         GT_most_points_against_team = team
    #
    # return f"{GT_most_points_against_team}, total points scored by GT {GT_most_points}"

    # Name either team that GT has played but never scored any points against?
    #
    # GT_zero_points_against = []
    # for team, games in opponent_games.items():
    #     GT_points = 0
    #     for game in games:
    #         GT_points += game["Points for GT"]
    #     if GT_points == 0:
    #         GT_zero_points_against.append(team)

    # How many teams has played Georgia Tech and never scored a point?
    # GT_zero_points_against = []
    # for team, games in opponent_games.items():
    #     GT_points = 0
    #     for game in games:
    #         GT_points += game["Points Against GT"]
    #     if GT_points == 0:
    #         GT_zero_points_against.append(team)
    # return len(GT_zero_points_against)

    #Against what team does Georgia Tech have the highest scoring differential (points for minus points against) all-time?

    # max_avg_score_diff = 0
    # max_avg_score_diff_team = None
    # for team, games in opponent_games.items():
    #     if len(games) >= 5:
    #         gt_points = 0
    #         opp_points = 0
    #         game_count = 0
    #         for game in games:
    #             gt_points += game["Points for GT"]
    #             opp_points += game["Points Against GT"]
    #             game_count += 1
    #
    #         delta = gt_points - opp_points
    #         avg_score_diff = delta/game_count
    #
    #         if avg_score_diff > max_avg_score_diff:
    #             max_avg_score_diff = avg_score_diff
    #             max_avg_score_diff_team = team
    #     else:
    #         pass
    # return f"{max_avg_score_diff_team} points differential {avg_score_diff}"
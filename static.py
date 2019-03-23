from datetime import datetime
import os
stat_list = ["passingYards", "passingTouchdowns", "passesIntercepted", "receptions",
             "receivingYards", "receivingTouchdowns", "rushingYards", "rushingTouchdowns",
             "opponentFumblesRecovered", "twoPointConversionPassesGood", "twoPointConversionRushesGood",
             "twoPointConversionPassReceptionsGood", "fumbles", "fumblesRecovered",
             "fieldGoalsMade", "fieldGoalsAttempted"]

twenty_fifth_stats = ["passingYards"]
tenth_stats = ["rushingYards", "receivingYards"]
neg_two_stats = ["passesIntercepted", "fumbles"]
four_stats = ["passingTouchdowns"]
six_stats = ["receivingTouchdowns", "rushingTouchdowns"]
half_stats = ["receptions"]
two_stats = ["twoPointConversionPassesGood", "twoPointConversionRushesGood", "twoPointConversionPassReceptionsGood"]
three_stats = ["fieldGoalsMade"]



dst_stat_list= ['turnovers','timesSacked','points','fieldGoalsBlocked','safeties','fieldGoalsMade','touchdowns', 'passingYardsNet', 'rushingYardsNet']
dst_two_stats=["turnovers",'safeties','fieldGoalsBlocked']

dst_one=["timesSacked"]


import pprint
pp = pprint.PrettyPrinter(indent=4)


aaf_api_url = "http://api.platform.aaf.com/v1/graphql"
player_teams_file = os.path.join(os.getcwd(), "data/player_teams.csv")
schedule_file = os.path.join(os.getcwd(), "data/schedule.csv")
data_dir = os.path.join(os.getcwd(), "data")
start_date = datetime(2019, 2, 11)
verbose = False

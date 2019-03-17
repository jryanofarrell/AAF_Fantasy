stat_list = ["passingYards", "passingTouchdowns", "passesIntercepted", "receptions",
             "receivingYards", "receivingTouchdowns", "rushingYards", "rushingTouchdowns",
             "opponentFumblesRecovered", "twoPointConversionPassesGood", "twoPointConversionRushesGood",
             "twoPointConversionsCompleted", "twoPointConversionPassReceptionsGood",
             "fieldGoalsMade", "fieldGoalsAttempted"]

twenty_fifth_stats = ["passingYards"]
tenth_stats = ["rushingYards", "receivingYards"]
neg_two_stats = ["passesIntercepted", "opponentFumblesRecovered"]
four_stats = ["passingTouchdowns"]
six_stats = ["receivingTouchdowns", "rushingTouchdowns"]
half_stats = ["receptions"]
two_stats = ["twoPointConversionPassesGood", "twoPointConversionRushesGood",
             "twoPointConversionsCompleted", "twoPointConversionPassReceptionsGood"]
three_stats = ["fieldGoalsMade"]
aaf_api_url = "http://api.platform.aaf.com/v1/graphql"
player_teams_file = "/data/player_teams.csv"
schedule_file = "/data/schedule.csv"
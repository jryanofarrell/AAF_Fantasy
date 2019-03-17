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

class Player(object):
    stats = dict()
    player_name = ""
    player_team = ""

    def __init__(self, player_name, player_team,):
        for stat in stat_list:
            self.stats[stat] = 0

    def calc_points(self):
        total_score=0.0
        for stat in twenty_fifth_stats:
            total_score = total_score + self.stats[stat]*0.04
        for stat in tenth_stats:
            total_score = total_score + self.stats[stat]*0.1
        for stat in neg_two_stats:
            total_score = total_score + self.stats[stat]*(-2.0)
        for stat in four_stats:
            total_score = total_score + self.stats[stat]*4.0
        for stat in six_stats:
            total_score = total_score + self.stats[stat]*6.0
        for stat in half_stats:
            total_score = total_score + self.stats[stat]*0.5
        for stat in two_stats:
            total_score = total_score + self.stats[stat]*2.0
        for stat in three_stats:
            total_score = total_score + self.stats[stat]*3.0
        total_score = total_score + (self.stats["fieldGoalsAttempted"]-self.stats["fieldGoalsMade"])*(-1.0)
        return total_score

    def update_player_stats(self, new_stats):
        self.stats = new_stats




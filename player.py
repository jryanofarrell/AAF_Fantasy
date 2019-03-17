import static


class Player(object):
    stats = dict()
    first_name = ""
    last_name = ""
    team = ""

    def __init__(self, first_name, last_name, team):
        for stat in static.stat_list:
            self.stats[stat] = 0
        self.first_name = first_name
        self.last_name = last_name
        self.team = team

    def calc_points(self):
        total_score=0.0
        for stat in static.twenty_fifth_stats:
            total_score = total_score + self.stats[stat]*0.04
        for stat in static.tenth_stats:
            total_score = total_score + self.stats[stat]*0.1
        for stat in static.neg_two_stats:
            total_score = total_score + self.stats[stat]*(-2.0)
        for stat in static.four_stats:
            total_score = total_score + self.stats[stat]*4.0
        for stat in static.six_stats:
            total_score = total_score + self.stats[stat]*6.0
        for stat in static.half_stats:
            total_score = total_score + self.stats[stat]*0.5
        for stat in static.two_stats:
            total_score = total_score + self.stats[stat]*2.0
        for stat in static.three_stats:
            total_score = total_score + self.stats[stat]*3.0
        total_score = total_score + (self.stats["fieldGoalsAttempted"]-self.stats["fieldGoalsMade"])*(-1.0)
        return total_score

    def update_player_stats(self, new_stats):
        self.stats = new_stats

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.team))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.first_name == other.first_name and self.last_name == other.last_name and self.team == other.team




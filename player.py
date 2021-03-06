import static


class Player(object):
    stats = dict()
    first_name = ""
    last_name = ""
    team = ""

    def __init__(self, first_name, last_name, team, pos="NA", verbose=False):
        for stat in static.stat_list:
            self.stats[stat] = 0
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.pos = pos
        self.verbose=verbose

    def calc_points(self):
        total_score=0.0
        if self.verbose:
            print ("Calculating points for player {} - {}".format(self, self.pos))
            static.pp.pprint(self.stats)
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

    def get_pos(self):
        return self.pos

    def get_team(self):
        return self.team

    def get_touchdowns(self):
        if self.verbose:
            print("Getting player touchdowns for {}".format(self))
            static.pp.pprint(self.stats)
        touchdown_stats = ["receivingTouchdowns", "rushingTouchdowns"]
        num_tds = 0
        for td in touchdown_stats:
            num_tds += self.stats[td]
        if self.verbose:
            print("total player touchdowns is {}".format(num_tds))
        return num_tds

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.team))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.first_name == other.first_name and self.last_name == other.last_name and self.team == other.team

    def __str__(self):
        if not self.last_name or not self.team:
            return self.first_name
        else:
            return "{} {} - {}".format(self.first_name, self.last_name, self.team)



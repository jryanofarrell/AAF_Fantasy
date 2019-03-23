import static

class dst(object):
    stats = dict()
    
#todo determine home and away scores within composite

    def __init__(self, name, verbose=False):
        self.name= name
        self.verbose = verbose
        self.stats={}
        self.pos = "DEFENSE"
        self.stats["player_touchdowns"] = 0
        for stat in static.dst_stat_list:
            self.stats[stat]=0

    def update_stats(self, stat_name, stat_value):
        self.stats[stat_name]=stat_value

    def calc_points(self):
        if self.verbose:
            print("Calculating Score for {}".format(self.name))
            static.pp.pprint(self.stats)
        dst_score=0.0

        d_tds = self.stats["touchdowns"] - self.stats["player_touchdowns"]
        dst_score=6*d_tds

        for stat in static.dst_two_stats:
            dst_score= dst_score+self.stats[stat]*2

        for stat in static.dst_one:
            dst_score= dst_score+self.stats[stat]

        score=self.stats['points']
        if score == 0:
            dst_score += 5
        elif score <=6:
            dst_score += 4
        elif score<=13:
            dst_score += 3
        elif score<=17:
            dst_score += 1
        elif score<=27:
            dst_score += 0
        elif score<=34:
            dst_score += -1
        elif score <= 45:
            dst_score += -3
        elif score >=46 :
            dst_score += -5


        return dst_score

    def get_name(self):
        return self.name

    def get_pos(self):
        return self.pos

    def get_team(self):
        return ""

    def update_touchdowns(self, player_dict):
        if self.verbose:
            print("Getting Player TDs for {}".format(self))
        for player_name, player_obj in player_dict.items():
            #print(player_obj.get_team())
            if player_obj.get_team() == self.name:
                self.stats["player_touchdowns"] += player_obj.get_touchdowns()


    def __hash__(self):
        return hash((self.name))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.name == other.name

    def __str__(self):
        return self.name

import static

class dst(object):
    stats = dict()
    
#todo determine home and away scores within composite

    def __init__(self, name):
        self.name= name
        for stat in static.dst_stat_list:
            self.stats[stat]=0

    def update_stats(self, stat_name, stat_value):
        self.stats[stat_name]=stat_value

    def calc_dst_score(self):
        dst_score=0.0

        for stat in static.dst_two_stats:
            dst_score= dst_score+self.stats[stat]*2

        for stat in static.dst_one:
            dst_score= dst_score+self.stats[stat]


        for stat in static.score:
            score=self.stats[stat]
          
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
    
    def __hash__(self):
        return hash((self.name))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.name == other.name



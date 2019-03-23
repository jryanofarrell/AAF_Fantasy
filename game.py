import csv
import static
import player
import os
import re

stf_pos_conv_dict = {
    "QB1": "QUARTERBACK_1",
    "RB1": "RUNNING_BACK_1",
    "WR1": "WIDE_RECEIVER_1",
    "WR2": "WIDE_RECEIVER_2",
    "FLX1": "FLEX_1",
    "TE1": "TIGHT_END_1",
    "DST1": "DEFENSE_1",
    "K1": "KICKER_1",
    "BE1": "BENCH_1",
    "BE2": "BENCH_2",
    "BE3": "BENCH_3"

}
fts_pos_conv_dict = dict((v,k) for k,v in stf_pos_conv_dict.items())

class Game(object):

    def __init__(self, player_dict, game_num, week_num, verbose=False):
        self.player_dict = player_dict
        self.game_num = game_num
        self.week_num = week_num
        self.team1 = None
        self.team2 = None
        self.verbose = verbose

        self.get_team_names()
        self.get_team_players()


    def get_team_names(self):
        vs_string = ""
        with open(static.schedule_file, "r", encoding='utf-8-sig') as csv_file:
            csv_obj = csv.DictReader(csv_file, delimiter=",")
            for row in csv_obj:
                if self.verbose:
                    print(row)
                if row["Schedule"] == "Week {}".format(self.week_num):
                    vs_string = row["Game{}".format(self.game_num)]
                    break
            # if self.verbose:
            #     print(next(csv_obj))
            # vs_string = next(csv_obj)[self.week_num-1][self.game_num]

        self.team1 = Team(vs_string.split("vs")[0].strip(), self.player_dict, verbose=self.verbose)
        self.team2 = Team(vs_string.split("vs")[1].strip(), self.player_dict, verbose=self.verbose)
        if self.verbose:
            print(vs_string)
            print(self.team1)
            print(self.team2)

    def get_team_players(self):

        with open(static.player_teams_file, "r", encoding='utf-8-sig') as csv_file:
            csv_obj = csv.DictReader(csv_file, delimiter=",")
            for row in csv_obj:
                if self.verbose:
                    print(row)
                player1_name = row[self.team1.get_name()]
                player2_name = row[self.team2.get_name()]
                pos = stf_pos_conv_dict[row["Position"]]
                self.team1.add_player(player1_name, pos)
                self.team2.add_player(player2_name, pos)

    def create_score(self):
        csv_file_name = "final_score_week{}_game{}.csv".format(self.week_num, self.game_num)
        csv_file_path = os.path.join(static.data_dir, csv_file_name)
        if os.path.isfile(csv_file_path):
            cnt = 1
            while os.path.isfile(csv_file_path):
                csv_file_name = "final_score_week{}_game{}_copy{}.csv".format(self.week_num, self.game_num,cnt)
                csv_file_path = os.path.join(static.data_dir, csv_file_name)
                cnt = cnt + 1
        with open(csv_file_path, mode='w+') as csv_file:
            t1_name = self.team1.get_name()
            t2_name = self.team2.get_name()
            fieldnames = ['', t1_name, "home_score", "away_score", t2_name]
            writer = csv.DictWriter(csv_file, lineterminator='\n', fieldnames=fieldnames)
            order_score = ["QUARTERBACK_1", "RUNNING_BACK_1", "WIDE_RECEIVER_1", "WIDE_RECEIVER_2",
                           "FLEX_1", "TIGHT_END_1", "DEFENSE_1", "KICKER_1"]
            writer.writeheader()
            for scorer in order_score:
                t1_player = self.team1.get_player(scorer)
                t2_player = self.team2.get_player(scorer)
                writer.writerow({'': fts_pos_conv_dict[scorer],
                                 t1_name: str(t1_player),
                                 'home_score': t1_player.calc_points(),
                                 t2_name: str(t2_player),
                                 'away_score': t2_player.calc_points()
                                 })
            writer.writerow({'': 'Total Score',
                             t1_name: "",
                             'home_score': self.team1.calc_points(),
                             t2_name: "",
                             'away_score': self.team2.calc_points()})
            writer.writerow({'': '',
                             t1_name: "",
                             'home_score': "",
                             t2_name: "",
                             'away_score': ""})
            benches = ["BENCH_1","BENCH_2","BENCH_3"]
            for bench in benches:
                t1_player = self.team1.get_player(bench)
                t2_player = self.team2.get_player(bench)
                writer.writerow({'': fts_pos_conv_dict[bench],
                                 t1_name: str(t1_player),
                                 'home_score': t1_player.calc_points(),
                                 t2_name: str(t2_player),
                                 'away_score': t2_player.calc_points()
                                 })






class Team(object):

    def __init__(self, name, player_dict, verbose=False):
        self.name = name
        self.player_dict = player_dict
        self.team_dict = dict()
        #self.team_dict["DEFENSE_1"] = player.Player("TEMP", "DEFENSE", "TODO")
        self.verbose=verbose

    def get_name(self):
        return self.name

    def add_player(self, player_name, pos):
        #player name in format FirstName LastName - TeamName
        first_name = ""
        last_name = ""
        team_name = ""
        try:
            name = player_name.split("-")[0]
            first_name = name.split()[0].strip()
            last_name = name.replace(first_name, "").strip()
            if "Jr." in last_name:
                last_name = last_name.replace("Jr.", "Jr. ") #for some reason wes saxton jr. has a space after the period
            team_name = player_name.split("-")[-1].strip()
        except Exception as error:
            print("failed to get player_name in name {} due to {}".format(player_name, error))
            first_name = player_name
        player_obj = player.Player(first_name, last_name, team_name, pos)
        if str(player_obj) not in self.player_dict:
            print("failed to find player {} in the player set using a dummy variable".format(player_obj))
        else:
            player_obj = self.player_dict[str(player_obj)]
        team_pos = player_obj.get_pos()
        num_regex = '.*_\d{1}'
        regexp = re.compile(num_regex)
        if not regexp.search(team_pos):
            team_pos = "{}_1".format(team_pos)
        if self.verbose:
            print("Adding player {} with POS {}".format(player_obj, team_pos))
        if "DEFENSI" in team_pos:
            team_pos = "BENCH_1"
        while team_pos in self.team_dict.keys():
            team_pos_num = int(team_pos.split("_")[-1])
            team_pos_num = team_pos_num +1
            team_pos ="{}_{}".format("_".join(team_pos.split("_")[0:-1]), team_pos_num)
            if team_pos in ["RUNNING_BACK_2", "WIDE_RECEIVER_3", "TIGHT_END_2"]:
                team_pos = "FLEX_1"
            elif team_pos in ["QUARTERBACK_2", "DST_2", "KICKER_2", "FLEX_2"] or "DEFENSI" in team_pos:
                team_pos = "BENCH_1"
        self.team_dict[team_pos] = player_obj

    def get_player(self, pos):
        if self.verbose:
            print(self.name)
            print(self.team_dict)
        return self.team_dict[pos]

    def calc_points(self):
        total_score = 0.0
        for pos, player_obj in self.team_dict.items():
            total_score = total_score + player_obj.calc_points()
        return total_score

    def __str__(self):
        return self.name

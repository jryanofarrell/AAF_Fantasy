import data_generator
import static
import utils
import game
import dst
import os

def main():
    week = 4
    date = utils.get_week(week)
    game_ids = data_generator.get_game_ids(verbose=static.verbose, date=date)
    player_dict = dict()
    for cnt, game_id in enumerate(game_ids):
        player_dict = {**player_dict, **data_generator.get_player_stats(game_id["id"], static.stat_list, verbose=False)}# player_set.union(data_generator.get_player_stats(game_id["id"], static.stat_list, verbose=static.verbose))
        if static.verbose:
            print("set len after game {} is {}".format(cnt+1, len(player_dict)))
        player_dict = {**player_dict, **data_generator.get_dst_stats(game_id['id'], static.dst_stat_list, verbose=False)}

    for player_name, player_obj in player_dict.items():
        if isinstance(player_obj, dst.dst):
            player_obj.update_touchdowns(player_dict)


    with open(os.path.join(static.data_dir, "player_list.txt"), "w+") as f:
        for player in player_dict:
            f.write("{}\n".format(player))
    g1 = game.Game(player_dict, 1, week, verbose=False)
    g2 = game.Game(player_dict, 2, week, verbose=False)
    g1.create_score()
    g2.create_score()


main()
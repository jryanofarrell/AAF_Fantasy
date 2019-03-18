import data_generator
import static
import utils
import game


def main():
    week = 5
    date = utils.get_week(week)
    game_ids = data_generator.get_game_ids(verbose=static.verbose, date=date)
    player_dict = dict()
    for cnt, game_id in enumerate(game_ids):
        player_dict = {**player_dict, **data_generator.get_player_stats(game_id["id"], static.stat_list, verbose=True)}# player_set.union(data_generator.get_player_stats(game_id["id"], static.stat_list, verbose=static.verbose))
        if static.verbose:
            print("set len after game {} is {}".format(cnt+1, len(player_set)))
        data_generator.get_dst_stats(game_id['id'], static.dst_stat_list)



    g1 = game.Game(player_dict, 1, week, verbose=True)
    g2 = game.Game(player_dict, 2, week, verbose=True)
    g1.create_score()
    g2.create_score()


main()
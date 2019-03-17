import data_generator
import static

def main():
    date = static.start_date
    game_ids = data_generator.get_game_ids(verbose=static.verbose, date=date)
    player_set = set()
    for cnt, game_id in enumerate(game_ids):
        player_set = player_set.union(data_generator.get_player_stats(game_id["id"], static.stat_list, verbose=static.verbose))
        if static.verbose:
            print("set len after game {} is {}".format(cnt+1, len(player_set)))





main()
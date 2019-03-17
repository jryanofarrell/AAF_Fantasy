import data_generator
import static

def main():
    game_ids = data_generator.get_game_ids(verbose=True)
    data_generator.get_player_stats(game_ids[0]["id"], static.stat_list, verbose=True)




main()
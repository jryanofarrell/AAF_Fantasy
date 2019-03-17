import data_generator
import player

def main():
    game_ids = data_generator.get_game_ids(verbose=True)
    data_generator.get_player_stats(game_ids[0]["id"], player.stat_list, verbose=True)




main()
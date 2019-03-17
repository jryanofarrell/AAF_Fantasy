import requests
import pprint
import utils
from player import Player
import static
pp = pprint.PrettyPrinter(indent=4)


def get_game_ids(date="TODAY", verbose=False):
    date_string_list = utils.get_date_string_list(date)
    if verbose:
        pp.pprint(date_string_list)
    query_string = '''
    {{
      gamesConnection(atOrAfterTime:"{}", beforeTime:"{}"){{
        nodes{{
          awayTeam{{
            name
          }}
          homeTeam{{
            name
          }}
          id
        }}
      }}
    }}
    '''.format(date_string_list[0], date_string_list[1])
    if verbose:
        pp.pprint(query_string)
    game_data = post_req(query_string, verbose=verbose)
    return game_data['data']['gamesConnection']['nodes']


def get_player_stats(game_id, stats, verbose=False):
    query_string = '''
    {{
      node(id: "{}") {{
        ... on Game {{
          playersConnection(first: 200) {{
            edges {{
              node {{
                jerseyNumber
                legalName{{
                  givenName
                  familyName
                }}
              }}
              team {{
                abbreviation
              }}
              stats {{
                {}
              }}
            }}
          }}
        }}
      }}
    }}
    '''.format(game_id, "\n".join(stats))
    if verbose:
        print(query_string)
    players_stats = post_req(query_string, verbose=verbose)
    players_stats = players_stats['data']['node']['playersConnection']['edges']
    player_list = set()
    for player_dict in players_stats:
        name_dict = player_dict['node']['legalName']
        player_team = player_dict['team']['abbreviation']
        player_obj = Player(name_dict['givenName'], name_dict['familyName'], player_team)
        player_obj.update_player_stats(player_dict['stats'])
        player_list.add(player_obj)

    if verbose:
        print("player set is length {}".format(len(player_list)))
    return player_list


def post_req(query_string, verbose=False):
    req = requests.post(static.aaf_api_url, json={'query': query_string})
    try:
        req.raise_for_status()
    except requests.HTTPError as error:
        print("Failed to post query {}".format(query_string))
        print("Failed due to error {}".format(error))
        return {}
    result = req.json()
    if verbose:
        pp.pprint(result)
    return result

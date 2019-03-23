import requests
import pprint
import utils
from player import Player
from dst import dst
import static
pp = pprint.PrettyPrinter(indent=4)


def get_game_ids(date="TODAY", verbose=False):
    date_string_list = utils.get_date_string_list(date, verbose=verbose)
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
                position
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
    full_player_dict = dict()
    for player_dict in players_stats:
        name_dict = player_dict['node']['legalName']
        player_team = player_dict['team']['abbreviation']
        player_pos = player_dict['node']['position']
        player_obj = Player(name_dict['givenName'], name_dict['familyName'], player_team, player_pos, verbose=static.verbose)
        player_obj.update_player_stats(player_dict['stats'])
        full_player_dict[str(player_obj)] = player_obj

    if verbose:
        print("player set is length {}".format(len(full_player_dict)))
        print(full_player_dict)
    return full_player_dict


def get_dst_stats(gameid, stats):
    p_query_string='''
    {{
      node(id: "{}") {{
        ... on Game {{
          homeTeamEdge {{
            node{{abbreviation}}
            ...teamEdge
          }}
          awayTeamEdge {{
            node{{abbreviation}}
            ...teamEdge
          }}
        }}
      }}
    }}
    
    fragment teamEdge on GameTeamEdge {{
      stats {{
      {}
      }}
    }}
    '''.format(gameid,"\n".join(stats))

    gamedata= post_req(p_query_string)
    gamedata= gamedata['data']['node']
    from_opponent_list=['points','turnovers','timesSacked']
    #pp.pprint(gamedata)
    awayteam= dst(gamedata['awayTeamEdge']['node']['abbreviation'])
    hometeam= dst(gamedata['homeTeamEdge']['node']['abbreviation'])
    for stat in from_opponent_list:
        awayteam.update_stats(stat, gamedata['homeTeamEdge']['stats'][stat])
        hometeam.update_stats(stat, gamedata['homeTeamEdge']['stats'][stat])




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

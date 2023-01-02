from constants import TEAMS, PLAYERS


def clean_data():
    cleaned_players = []
    for player_stats in PLAYERS:
        if player_stats['experience'] == "YES":
            experience_bool = True
        else:
            experience_bool = False
        height_int = int(player_stats['height'].split(' ')[0])
        clean_stats = {
            'name':player_stats['name'],
            'guardians':player_stats['guardians'],
            'experience':experience_bool,
            'height':height_int
            }
        cleaned_players.append(clean_stats)
    return cleaned_players


def balance_teams():
    panthers_roster = []
    bandits_roster = []
    warriors_roster = []
    num_players_roster = len(PLAYERS) / len(TEAMS)
    for team in TEAMS:
        for clean_stats in cleaned_players: 
            roster.append(clean_stats['name'])


if __name__ == "__main__":
    # print(clean_data())
    # print(PLAYERS)
    pass

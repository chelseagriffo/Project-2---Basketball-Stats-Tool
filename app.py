from constants import TEAMS, PLAYERS


def clean_data():
    clean_players = []
    for player in PLAYERS:
        if player['experience'] == "YES":
            experience_bool = True
        else:
            experience_bool = False
        height_int = int(player['height'].split(' ')[0])
        clean_player = {
            'name':player['name'],
            'guardians':player['guardians'],
            'experience':experience_bool,
            'height':height_int
            }
        clean_players.append(clean_player)
    return clean_players


def balance_teams(clean_players):
    panthers = []
    bandits = []
    warriors = []
    teams = [panthers, bandits, warriors]
    while len(clean_players) >= 1: 
        for team in teams:
            try:
                team.append(clean_players.pop(0))
            except IndexError:
                break
    return teams
    



if __name__ == "__main__":
    clean_data()
    balance_teams(clean_data())
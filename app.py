from constants import TEAMS, PLAYERS


def clean_data():
    cleaned_players = []
    for player_stats in PLAYERS:
        clean_stats = {
            'name':player_stats['name']
            'guardians':player_stats['guardians']
            if player_stats['experience'] == "YES"
                clean_stats['experience'] = True
            else:
                clean_stats['experience'] = False
            
        }

if __name__ == "__main__":
    pass


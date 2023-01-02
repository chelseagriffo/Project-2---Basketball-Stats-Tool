from constants import TEAMS, PLAYERS
import sys

print(f'BASKETBALL STATS TOOL \n\n')
print('---MENU--- \n')
print('What would you like to do? \nA) Display Team Stats \nB) Quit')

while True:
    choice_use_quit = input('\n\nEnter your choice: ').capitalize()
    print(choice_use_quit)
    if choice_use_quit == 'A': 
        print('\n\nA) Panthers \nB) Bandits \nC) Warriors')
        break
    elif choice_use_quit == 'B':
        print('\nThanks for using the Basketball Stats Tool!')  
        break
    else:
        print("Please enter 'A' or 'B'")
        continue






def clean_data():
    clean_players = []
    for player in PLAYERS:
        if player['experience'] == "YES":
            experience_bool = True
        elif player['experience'] == "NO":
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
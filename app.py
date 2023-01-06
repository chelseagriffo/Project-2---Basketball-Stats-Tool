from constants import TEAMS, PLAYERS
import sys


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
            'guardians':player['guardians'].split(" and "),
            'experience':experience_bool,
            'height':height_int
            }
        clean_players.append(clean_player)
    return clean_players



#The balance_teams function balances the teams so that each team has the same number of experienced vs. inexperienced players
def balance_teams(clean_players):
    panthers = []
    bandits = []
    warriors = []
    teams = [panthers, bandits, warriors]
    experience_yes = []
    experience_no = []
    #This for loop will sort the experience and inexperience players into the 2 lists above.
    for clean_player in clean_players:
        if clean_player['experience'] == True:
            experience_yes.append(clean_player)
        elif clean_player['experience'] == False:
            experience_no.append(clean_player)
    #The following while loop will balance the teams with experienced players.
    while len(experience_yes) >= 1: 
        for team in teams:
                try:
                    team.append(experience_yes.pop(0))
                except IndexError:
                    break
    ##The following while loop will balance the teams with inexperienced players.
    while len(experience_no) >= 1:
        for team in teams:
            try:
                team.append(experience_no.pop(0))
            except IndexError:
                break
    return teams
    

if __name__ == "__main__":
    clean_data()
    balance_teams(clean_data())

    print(f'BASKETBALL STATS TOOL \n\n')
    print('---MENU--- \n')
    print('What would you like to do? \nA) Display Team Stats \nB) Quit')

    #This while loop prompts the user to choose to use the tool to view team stats or quit the tool
    while True:
        choice_use_quit = input('\n\nEnter your choice: ').capitalize()
        if choice_use_quit == 'A': 
            print('\n\nA) Panthers \nB) Bandits \nC) Warriors')
            break
        elif choice_use_quit == 'B':
            print('\nThanks for using the Basketball Stats Tool!')  
            sys.exit()
        else:
            print("Please enter 'A' or 'B'")
            continue

    while True:
        team_choice = input('\n\nFor which team would you like to display stats? Choose a letter: ').capitalize()
        if team_choice == 'A': 
            panthers = balance_teams(clean_data())[0]
            total_players = len(panthers)
            panthers_roster = []
            for clean_player in panthers: 
                panthers_roster.append(clean_player['name'])
            print(f''' 
Team: Panthers Stats
---------------------
Total players: {total_players}

Panthers Roster:  
    ''') 
# Used https://flexiple.com/python/python-print-list/ to learn how to print out a comma separated list
            print(*panthers_roster, sep=", ") 
            break
        elif team_choice == 'B':
            bandits = balance_teams(clean_data())[1]
            total_players = len(bandits)
            bandits_roster = []
            for clean_player in bandits: 
                bandits_roster.append(clean_player['name'])
            print(f''' 
Team: Bandits Stats
---------------------
Total players: {total_players}

Bandits Roster:  
    ''') 
            print(*bandits_roster, sep=", ")
            break
        elif team_choice == 'C':
            warriors = balance_teams(clean_data())[2]
            total_players = len(warriors)
            warriors_roster = []
            for clean_player in warriors: 
                warriors_roster.append(clean_player['name'])
            print(f''' 
Team: Warriors Stats
---------------------
Total players: {total_players}

Warriors Roster:  
    ''') 
            print(*warriors_roster, sep=", ")
            break
        else:
            print("Please enter 'A', 'B', or 'C'")
            continue
    
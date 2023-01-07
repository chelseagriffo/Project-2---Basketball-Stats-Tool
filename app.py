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
            'guardians':", ".join(player['guardians'].split(" and ")),
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
while True:
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
            panthers_experienced = []
            panthers_inexperienced = []
            panthers_heights = []
            panthers_parents = []
            for clean_player in panthers: 
                panthers_roster.append(clean_player['name'])
            for clean_player in panthers:
                if clean_player['experience'] == True:
                    panthers_experienced.append(clean_player['experience'])
                elif clean_player['experience'] == False:
                    panthers_inexperienced.append(clean_player['experience'])
            for clean_player in panthers:
                panthers_heights.append(clean_player['height'])
            for clean_player in panthers:
                panthers_parents.append(clean_player['guardians'])
            print(f''' 
Team: Panthers Stats
---------------------
Total players: {total_players}

# of inexperience players: {len(panthers_inexperienced)}

# of experienced players: {len(panthers_experienced)}

Panthers average height: {sum(panthers_heights)/total_players}
    ''')
            print('Panthers parents:')
            print(*panthers_parents, sep=", ")

            print('\nPanthers Roster:')
            print(*panthers_roster, sep=", ")
            break
        elif team_choice == 'B':
            bandits = balance_teams(clean_data())[1]
            total_players = len(bandits)
            bandits_roster = []
            bandits_experienced = []
            bandits_inexperienced = []
            bandits_heights = []
            bandits_parents = []
            for clean_player in bandits: 
                bandits_roster.append(clean_player['name'])
            for clean_player in bandits:
                if clean_player['experience'] == True:
                    bandits_experienced.append(clean_player['experience'])
                elif clean_player['experience'] == False:
                    bandits_inexperienced.append(clean_player['experience'])
            for clean_player in bandits:
                bandits_heights.append(clean_player['height'])
            for clean_player in bandits:
                bandits_parents.append(clean_player['guardians'])
            print(f''' 
Team: Bandits Stats
---------------------
Total players: {total_players}

# of inexperience players: {len(bandits_inexperienced)}

# of experienced players: {len(bandits_experienced)}

Bandits average height: {sum(bandits_heights)/total_players}
    ''')
            print('Bandits parents:')
            print(*bandits_parents, sep=", ")

            print('\nBandits Roster:')
            print(*bandits_roster, sep=", ")
            break
        elif team_choice == 'C':
            warriors = balance_teams(clean_data())[2]
            total_players = len(warriors)
            warriors_roster = []
            warriors_experienced = []
            warriors_inexperienced = []
            warriors_heights = []
            warriors_parents = []
            for clean_player in warriors: 
                warriors_roster.append(clean_player['name'])
            for clean_player in warriors:
                if clean_player['experience'] == True:
                    warriors_experienced.append(clean_player['experience'])
                elif clean_player['experience'] == False:
                    warriors_inexperienced.append(clean_player['experience'])
            for clean_player in warriors:
                warriors_heights.append(clean_player['height'])
            for clean_player in warriors:
                warriors_parents.append(clean_player['guardians'])
            print(f''' 
Team: Warriors Stats
---------------------
Total players: {total_players}

# of inexperience players: {len(warriors_inexperienced)}

# of experienced players: {len(warriors_experienced)}

Warriors average height: {sum(warriors_heights)/total_players}
    ''')
            print('Warriors parents:')
            print(*warriors_parents, sep=", ")

            print('\nWarriors Roster:')
            print(*warriors_roster, sep=", ")
            break
        else:
            print("Please enter 'A', 'B', or 'C'")
            continue
    while True:
        return_menu_or_quit = input('\n\nWould you like to return to the main menu? Enter YES or NO: ').upper()
        if return_menu_or_quit == 'YES': 
            break
        elif return_menu_or_quit == 'NO':
            print('\nThanks for using the Basketball Stats Tool!')  
            sys.exit()
        else:
            print("Please enter 'YES' or 'NO'")
            continue
        
from constants import TEAMS, PLAYERS
import sys

print(f'BASKETBALL STATS TOOL \n\n')
print('---MENU--- \n')
print('What would you like to do? \nA) Display Team Stats \nB) Quit')

#This while loop prompts the user to choose to use the tool to view team stats or quit the tool
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
    (balance_teams(clean_data()))
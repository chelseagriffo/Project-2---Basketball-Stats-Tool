from constants import TEAMS, PLAYERS

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



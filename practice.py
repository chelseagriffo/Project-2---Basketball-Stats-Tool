from constants import TEAMS, PLAYERS


num_players_roster = int(len(PLAYERS) / len(TEAMS))
stop = num_players_roster
start = 0
for i in range(start, stop):
    print(start)
    print(stop)
    start += num_players_roster
    stop += num_players_roster
    print(i)



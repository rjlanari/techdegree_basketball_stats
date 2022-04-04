import constants
import random

def experience_list(all_players):
    experienced = []
    not_experienced = []
    for player in all_players:
        if player["experience"] == "YES":
            experienced.append(player)
        else:
            not_experienced.append(player)
    return experienced, not_experienced
     

def balance_teams(list_1, list_2):
    count = 0
    len_list1 = len(list_1)
    len_list2 = len(list_2)
    team_panthers = [] 
    team_bandits = []
    team_warriors = []
    while count < len_list1:
        team_panthers.append(list_1.pop(random.randint(0, len(list_1)-1)))
        team_bandits.append(list_1.pop(random.randint(0, len(list_1)-1)))
        team_warriors.append(list_1.pop(random.randint(0, len(list_1)-1)))
        count += 3
    count = 0
    while count < len_list2:
        team_panthers.append(list_2.pop(random.randint(0, len(list_2)-1)))
        team_bandits.append(list_2.pop(random.randint(0, len(list_2)-1)))
        team_warriors.append(list_2.pop(random.randint(0, len(list_2)-1)))
        count += 3    
    return team_panthers, team_bandits, team_warriors

print((len(constants.PLAYERS)))



list1 = experience_list(constants.PLAYERS)[0]
list2 = experience_list(constants.PLAYERS)[1]

print(len(list1))



print(balance_teams(list1, list2))



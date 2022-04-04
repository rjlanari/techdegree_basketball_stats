import constants

def experience_list(all_players):
    experienced = []
    not_experienced = []
    for player in all_players:
        if player["experience"] == "YES":
            experienced.append(player)
        else:
            not_experienced.append(player)
    return experienced, not_experienced


list1 = experience_list(constants.PLAYERS)[0]
list2 = experience_list(constants.PLAYERS)[1]

print(list1)

print(list2)
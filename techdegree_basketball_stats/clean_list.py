import constants

def clean_list(players_list):
    cleaned = [] #create the empty list
    for player in players_list:
        fixed_player = {} #create the empty dictionaries
        fixed_player["name"] = player["name"]
        guardians_list = player["guardians"].split(" and ")
        fixed_player["guardians"] = guardians_list
        if player["experience"] == "YES":
            fixed_player["experience"] = True
        if player['experience'] == "NO":
            fixed_player["experience"] = False
        height_sep = player["height"].split(" ") #split the hight in a list
        fixed_player["height"] = int(height_sep[0])
        cleaned.append(fixed_player) #put the dictionaries in the list       
    return cleaned         
 
fixed1 = clean_list(constants.PLAYERS)

print(fixed1)

height_list = []
for player in fixed1: 
    height_list.append(player["height"])
avg_height = (sum(height_list)) / int(len(height_list))
#print("Average height: {}".format(avg_height))
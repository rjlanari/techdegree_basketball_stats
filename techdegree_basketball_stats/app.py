import constants
import random
import sys

num_players_team = len(constants.PLAYERS) / len(constants.TEAMS)



if __name__ == "__main__":
    
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
    
    
    
    def experience_list(all_players):
        experienced = []
        not_experienced = []
        for player in all_players:
            if player["experience"] == True:
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
    
    
    def display_stats (num, team, name):
        
        print("Team: {} Stats \n-------------------------------".format(name))
        num_players = int(num) 
        print("Total of players: {}".format(num_players))
        experienced = 0
        for player in team:
            if player["experience"] == True:
                experienced += 1
        print("Total experienced: {}".format(experienced))
        inexperienced = len(team)- experienced
        print("Total experienced: {}".format(inexperienced))
        
        height_list = []
        for player in team: 
            height_list.append(player["height"])
            avg_height = (sum(height_list)) / int(len(height_list))
        print("Average height: {}".format(avg_height))
        
        names_line = [] #putting the names in one line
        for player in team: #for each player in the 
            names_line.append(player["name"]) #put all names in a list
        print("\n\nPlayers on Team:\n")
        print(', '.join(names_line))
        
        guardians_list = []
        for player in team:
            guardians_list.append(", ".join(player["guardians"]))
        print("\nGuardians:\n")
        print(', '.join(guardians_list))
            
    
    cleaned_list = clean_list(constants.PLAYERS)
    list1 = experience_list(cleaned_list)[0]
    list2 = experience_list(cleaned_list)[1]
    cleaned_list = clean_list(constants.PLAYERS)   
    team1, team2, team3 = balance_teams(list1,list2)

    
    
    while True:
        print("\n\nBASQUETBALL TEAM STATS TOOL\n\n---- MENU ----\n\nHere are your choices:\nA) Display Team Stats\nB) Quit")
        option_choices = input("\nEnter an Option:  ")
        if option_choices.lower() == "a":
            print("\n\n1) Panthers\n2) Bandits\n3) Warriors")
            option_teams = input("\n\nEnter an Option:  ")
            name_team = constants.TEAMS[int(option_teams)-1]
            if option_teams == "1":
                chosed_team = team1
            if option_teams == "2":
                chosed_team = team2
            if option_teams == "3":
                chosed_team = team3
            display_stats(num_players_team, chosed_team, name_team)
            input("\n\nPress ENTER to continue...")
            continue  
        
        elif option_choices.lower() == "b":
            sys.exit("\nSee you next time!")
    
    
    
    

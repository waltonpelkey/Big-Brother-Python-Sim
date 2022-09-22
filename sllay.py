import random

# Creates player object to be defined later
    # Player: Name, Competition Ability, Gender, ID, Relationship Values
class Player():

    name = ""
    comp_ability = 0
    gender = ""
    comp_prob = 0
    ID = 0
    relationships = {}

    # Allows for player objects to be made
    def __init__(self, name, comp_ability, gender, ID, relationships):
        self.name = name
        self.comp_ability = comp_ability
        self.gender = gender
        self.ID = ID
        self.relationships = relationships

    # Allows for player relationships to be updated
    def update_relationships(self, new_relationships):
        self.relationships = new_relationships




# Defining all ten players (change to input later)
player1 = Player("Paula", 1, "female", 1, {})
player2 = Player("Anthony", 1, "male", 2, {})
player3 = Player("Leonard", 1, "male", 3, {})
player4 = Player("Krista", 1, "female", 4, {})
player5 = Player("Nico", 1000000, "male", 5, {})
player6 = Player("Alex", 1, "female", 6, {})
player7 = Player("Izabella", 1, "female", 7, {})
player8 = Player("Ken", 1, "other", 8, {})
player9 = Player("Lavi", 1, "male", 9, {})
player10 = Player("Axe", 1, "other", 10, {})

# Defining all relationship values between all ten players (starts at 0 by default)
player1.update_relationships({player2: 0, player3: 0, player4: 0, player5: 0, player6: 0, player7: 0, player8: 0, player9: 0, player10: 0})
player2.update_relationships({player1: 0, player3: 0, player4: 0, player5: 0, player6: 0, player7: 0, player8: 0, player9: 0, player10: 0})
player3.update_relationships({player1: 0, player2: 0, player4: 0, player5: 0, player6: 0, player7: 0, player8: 0, player9: 0, player10: 0})
player4.update_relationships({player1: 0, player2: 0, player3: 0, player5: 0, player6: 0, player7: 0, player8: 0, player9: 0, player10: 0})
player5.update_relationships({player1: 0, player2: 0, player3: 0, player4: 0, player6: 0, player7: 0, player8: 0, player9: 0, player10: 0})
player6.update_relationships({player1: 0, player2: 0, player3: 0, player4: 0, player5: 0, player7: 0, player8: 0, player9: 0, player10: 0})
player7.update_relationships({player1: 0, player2: 0, player3: 0, player4: 0, player5: 0, player6: 0, player8: 0, player9: 0, player10: 0})
player8.update_relationships({player1: 0, player2: 0, player3: 0, player4: 0, player5: 0, player6: 0, player7: 0, player9: 0, player10: 0})
player9.update_relationships({player1: 0, player2: 0, player3: 0, player4: 0, player5: 0, player6: 0, player7: 0, player8: 0, player10: 0})
player10.update_relationships({player1: 0, player2: 0, player3: 0, player4: 0, player5: 0, player6: 0, player7: 0, player8: 0, player9: 0})

# Full list of players to be used in functions and changed as players are eliminated
list_of_players = [player1, player2, player3, player4, player5,
     player6, player7, player8, player9, player10]


# Randomly selects a head of household based off competition ability (I think I didn't write this)
def HOH():

    # Loop through list of players, used to add comp abilities to randomize comp winner
    HCOMPTOTAL = 0
    for x in list_of_players:
        HCOMPTOTAL += x.comp_ability
        x.comp_prob = HCOMPTOTAL

    # Randomly chooses a number between 1 and the total of everyones comp.abilities
    # Uses the randomly generated number within the range to compare to the range that each comp ability enhabits and outputs the winner of the competition
    ability_to_beat = random.randint(1, HCOMPTOTAL)
    
    for player in list_of_players:
        comp_ability_var = 0
        for index in range(0, list_of_players.index(player)+1):
            comp_ability_var += list_of_players[index].comp_ability
        if ability_to_beat <= comp_ability_var:
            return player

# Takes in the head of household and returns a list containing their two nominations based off relationship values
def NOMS(hoh):

    # Finds the amount of people who share the lowest relationship value
    lowest_relationship = min(hoh.relationships.values())
    lowest_list=list(hoh.relationships.values())
    num_of_lowest_relationships = lowest_list.count(lowest_relationship)

    # Creates lists to be used later in definitions
    possible_noms = []
    noms = []
    
    # Function to select nomination if there are multiple people with lowest relationship value
    def multiple_lowest_select(noms, hoh):

        for player in hoh.relationships.keys():

            if hoh.relationships[player] == lowest_relationship:

                possible_noms.append(player)

        random_nom1 = random.randrange(0, (len(possible_noms)))
        random_nom2 = random.randrange(0, (len(possible_noms)))

        while random_nom1 == random_nom2:

            random_nom2 = random.randrange(0, (len(possible_noms)))
        
        noms.append(possible_noms[random_nom1])
        noms.append(possible_noms[random_nom2])

    # Function to select all nominees in the list (only use if there are exactly one or two)
    def select_all_lowest(noms, hoh):
        for player in hoh.relationships.keys():

            if hoh.relationships[player] == lowest_relationship:

                noms.append(player)
    
    # Function to select the second nomination if there was exactly one then there was multiple lowest
    def after_one_select_multiple(noms, hoh):
        for player in hoh.relationships.keys():

            if hoh.relationships[player] == lowest_relationship:

                possible_noms.append(player)

        random_nom = random.randrange(0, (len(possible_noms)))
        
        noms.append(possible_noms[random_nom])


    # Checks if there are exactly two people with the lowest relationship value, calls appropriate function
    if num_of_lowest_relationships == 2:

        select_all_lowest(noms,hoh)
        

    # Checks if there are more than one person with the lowest relationship value, calls appropriate function
    elif num_of_lowest_relationships > 1: 

        multiple_lowest_select(noms,hoh)
        

    # Checks if there is exactly one person with the lowest relationship value, calls appropriate function
    elif num_of_lowest_relationships == 1:

        select_all_lowest(noms,hoh)
        
        # Selects the second nomination
        while len(noms) != 2:

            # Increases relationship by one every loop to find the second highest relationship value
            lowest_relationship += 1
            num_of_lowest_relationships = lowest_list.count(lowest_relationship)

            # Goes through previous steps to select second person
            if num_of_lowest_relationships == 2:

                select_all_lowest(noms,hoh)
                
            
            elif num_of_lowest_relationships > 1:

                # Must call a different function to select only one second nomination (multiple_lowest_select ≠ after_one_select_multiple)
                after_one_select_multiple(noms,hoh)
                

            elif num_of_lowest_relationships == 1:

                select_all_lowest(noms,hoh)
                
    for key in hoh.relationships.keys():
        if key in noms:
            key.relationships[hoh] -= 2
        else:
            key.relationships[hoh] += 1
            
    return noms

# Takes in the head of household and two nominees and returns a list containing the hoh, noms, and three other players selected randommly
def VETO_PICKS(head_of_household, nominations):

    # # Finds the amount of people who share the highest relationship value of the HOH
    # highest_relationship = max(hoh.relationships.values())
    # highest_list1=list(hoh.relationships.values())
    # num_of_highest_relationships = highest_list1.count(highest_relationship)

    # # Finds the amount of people who share the highest relationship value of the first nominee
    # highest_relationship = max(nominations[0].relationships.values())
    # highest_list2=list(nominations[0].relationships.values())
    # num_of_highest_relationships = highest_list2.count(highest_relationship)

    # # Finds the amount of people who share the highest relationship value of the second nominee
    # highest_relationship = max(nominations[1].relationships.values())
    # highest_list3=list(nominations[1].relationships.values())
    # num_of_highest_relationships = highest_list3.count(highest_relationship)

    # Creates lists to be used later in definitions
    

    possible_veto_picks = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
    unwanted_picks = {head_of_household, nominations[0], nominations[1]}
    possible_veto_picks = [ele for ele in possible_veto_picks if ele not in unwanted_picks] 

    playing_in_veto = [head_of_household, nominations[0], nominations[1]]

    # Function to do the first draw (HOH)
    def veto_pick():

        random_player_index = random.randrange(0, (len(possible_veto_picks)))

        playing_in_veto.append(possible_veto_picks[random_player_index])
        possible_veto_picks.remove(possible_veto_picks[random_player_index])

    veto_pick()
    veto_pick()
    veto_pick()
    

    
    return playing_in_veto


# Function testing
"""for x in range(5):
    head_of_household = HOH()
    print(head_of_household.name, "is the new HOH!")
    nominations = NOMS(head_of_household)
    print(nominations[0].name, "and", nominations[1].name, "have been nominated")
    print("\n")"""

# Testing nomination relationship updates
head_of_household = HOH()
nominations = NOMS(head_of_household)
veto_picks = VETO_PICKS(head_of_household, nominations)
list = []
print(head_of_household.name, "is the new HOH!")
print(nominations[0].name, "and", nominations[1].name, "have been nominated!")
VETO_PICKS(head_of_household, nominations)
for i in range(6):
    list.append(veto_picks[i].name)
print(list, " is playing in veto!")

# possible_veto_picks = [player1, player2, player3, player4, player5,
#      player6, player7, player8, player9, player10]
# unwanted_picks = {head_of_household, nominations[0], nominations[1]}
# possible_veto_picks = [ele for ele in possible_veto_picks if ele not in unwanted_picks]

# print(possible_veto_picks)
# print(VETO_PICKS(HOH(), NOMS(HOH())))

# print(HOH().name, "and", nominations[0].name, "and", nominations[1].name, "and", random_veto_player1.name, "and", random_veto_player2.name, "and", random_veto_player3.name, "are competing in veto!")

def VETO():

    # Loop through list of players playing in veto, used to add comp abilities to randomize comp winner
    VCOMPTOTAL = 0
    for y in veto_picks:
        VCOMPTOTAL += y.comp_ability
        y.comp_prob = VCOMPTOTAL

    # Randomly chooses a number between 1 and the total of everyones comp.abilities
    # Uses the randomly generated number within the range to compare to the range that each comp ability enhabits and outputs the winner of the competition
    ability_to_beat_others = random.randint(1, VCOMPTOTAL)
    
    for player in veto_picks:
        comp_ability_var = 0
        for index in range(0, veto_picks.index(player)+1):
            comp_ability_var += veto_picks[index].comp_ability
        if ability_to_beat_others <= comp_ability_var:
            return player

veto_winner = VETO()
print(veto_winner.name, "is the winner of the veto!")

# Nico def VETO_CEREMONY():

    
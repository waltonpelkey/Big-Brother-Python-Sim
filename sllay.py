from ast import If
from cmd import IDENTCHARS
from nturl2path import pathname2url
import random
from tkinter import W
from unicodedata import name

# this class gives all the players in the game and gives them their attributes in the game
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
player1 = Player("Paula", 100000, "female", 1, {})
player2 = Player("Anthony", 1, "male", 2, {})
player3 = Player("Leonard", 5, "male", 3, {})
player4 = Player("Krista", 4, "female", 4, {})
player5 = Player("Nico", 3, "male", 5, {})
player6 = Player("Alex", 3, "female", 6, {})
player7 = Player("Izabella", 5, "female", 7, {})
player8 = Player("Ken", 4, "other", 8, {})
player9 = Player("Lavi", 1, "male", 9, {})
player10 = Player("Axe", 2, "other", 10, {})

# Defining all relationship values between all ten players (starts at 0 by default)
player1.update_relationships({player2: -200, player3: -100, player4: 0, player5: 0, player6: 0, player7: 0, player8: 0, player9: 0, player10: 0})
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




# Old (single) nomination function (waiting for approval from lead dev to delete)
""" def NOM1(hoh):
    lowest_relationship = min(hoh.relationships.values())
    lowest_list=list(hoh.relationships.values())
    res = lowest_list.count(lowest_relationship)
    possible_noms = []

    if res > 1:
        for player in hoh.relationships.keys():
            if hoh.relationships[player] == lowest_relationship:
                possible_noms.append(player)
        random_nom = random.randrange(0, (len(possible_noms) + 1))
        return possible_noms[random_nom]
    elif res == 1: 
        for player in hoh.relationships.keys():
            if hoh.relationships[player] == lowest_relationship:
                return player """




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
        return noms

    # Checks if there are more than one person with the lowest relationship value, calls appropriate function
    elif num_of_lowest_relationships > 1: 

        multiple_lowest_select(noms,hoh)
        return noms

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
                return noms
            
            elif num_of_lowest_relationships > 1:

                # Must call a different function to select only one second nomination (multiple_lowest_select ≠ after_one_select_multiple)
                after_one_select_multiple(noms,hoh)
                return noms

            elif num_of_lowest_relationships == 1:

                select_all_lowest(noms,hoh)
                return noms


# Function testing
print(HOH().name, "is the new HOH!")
nominations = NOMS(HOH())
print(nominations[0].name, "and", nominations[1].name, "have been nominated")

# New Problems Now That We Have Solved These
# 1. Nomination Ceremony Relationships 
    # If you were nominated you're opinion of the HOH goes down by 2 
    # If you were not nominated you're opinion of the HOH goes up by 1
# 2. Veto Draw Ceremony
# At the veto ceremony the players draw out of a hat to choose who is competing in the veto competition
# Six players compete in every veto competition, 3 of those being the HOH, The 2 nominees, And three other randomly selected houseguests
# When randomly selecting the HOH draws out of the hat, then the two nominees. There is one chip in the bag which contains something called Houseguests Choice
# When Houseguests Choice is chosen the player who drew it picks the person who they have the highest relationship with to compete in the challenge
# When someone picks using Houseguests Choice the chosen player gets +1 relationship with the person who chose them
# Note (There is only one Houseguest Choice in the bag so it can only be selected once)
# 3. Veto Competition
# Same as the HOH where it totals all players comp abilities playing the veto and then picks a number between the range and associates that number with a winner. 
# This means we should probably at the Veto Draw ceremony define all the players in the competition within a list
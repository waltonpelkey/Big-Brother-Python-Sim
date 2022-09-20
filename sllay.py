from ast import If
from cmd import IDENTCHARS
from nturl2path import pathname2url
import random
from tkinter import W
from unicodedata import name

n = 10

# this class gives all the players in the game and gives them their attributes in the game

class Player():

    name = ""
    comp_ability = 0
    gender = ""
    comp_prob = 0
    ID = 0
    relationships = {}

    def __init__(self, name, comp_ability, gender, ID, relationships):
        self.name = name
        self.comp_ability = comp_ability
        self.gender = gender
        self.ID = ID
        self.relationships = relationships

    def update_relationships(self, new_relationships):
        self.relationships = new_relationships


# player info: name, compitition ability, gender, ID, relationship values

player1 = Player("Paula", 2, "female", 1, {})
player2 = Player("Anthony", 1, "male", 2, {})
player3 = Player("Leonard", 5, "male", 3, {})
player4 = Player("Krista", 4, "female", 4, {})
player5 = Player("Nico", 3, "male", 5, {})
player6 = Player("Alex", 3, "female", 6, {})
player7 = Player("Izabella", 5, "female", 7, {})
player8 = Player("Ken", 4, "other", 8, {})
player9 = Player("Lavi", 1, "male", 9, {})
player10 = Player("Axe", 2, "other", 10, {})

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


L = [player1, player2, player3, player4, player5,
     player6, player7, player8, player9, player10]
HCOMPTOTAL = 0
# Loop through list of players, used to add comp abilities to randomize comp winner
for x in L:
    HCOMPTOTAL = x.comp_ability + HCOMPTOTAL
    x.comp_prob = HCOMPTOTAL


# Real ~> Real
# Randomly chooses a number between 1 and the total of everyones comp.abilities
a = random.randint(1, HCOMPTOTAL)

# uses the randomly generated number within the range to compare to the range that each comp ability enhabits and outputs the winner of the competition

# Real ~> String
# Consumes the randomly generated integer from 1 to the comp total and checks which player it corresponds to and produces
# a printed string declaring the HOH


def HOH():
    for player in L:
        koala = 0
        for index in range(0, L.index(player)+1):
            koala += L[index].comp_ability
        if a <= koala:
            print(f'{player.name} is the new HOH!')
            return player

def NOM1(hoh):
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
                return player

print(NOM1(HOH()).name)
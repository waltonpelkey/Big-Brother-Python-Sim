# Big-Brother-Python-Sim

A Big Brother Simulator based off the TV show. Given user inputted characters will run simulations and give you a winner.

TODO LIST:
- [ ] Nomination Ceremony Relationships 
  - If you were nominated you're opinion of the HOH goes down by 2 (-2)
  - If you were not nominated you're opinion of the HOH goes up by 1 (+1)
- [ ] Veto Draw Ceremony
  - At the veto ceremony the players draw out of a hat to choose who is competing in the veto competition
  - Six players compete in every veto competition, 3 of those being the HOH, The 2 nominees, And three other randomly selected houseguests
  - When randomly selecting the HOH draws out of the hat, then the two nominees. There is one chip in the bag which contains something called Houseguests Choice
  - When Houseguests Choice is chosen the player who drew it picks the person who they have the highest relationship with to compete in the challenge
  - When someone picks using Houseguests Choice the chosen player gets +1 relationship with the person who chose them
  - There is only one Houseguest Choice in the bag so it can only be selected once
- [ ] Veto Competition
  - Same as the HOH where it totals all players comp abilities playing the veto and then picks a number between the range and associates that number with a winner.
  - This means we should probably at the Veto Draw ceremony define all the players in the competition within a list
- [ ] Veto Ceremony
  - 3 Potential Cases for Veto Winner: HOH, NOM, Other
  - Cases
  - HOH:  
  - if the players on the block are their lowest two relationships the HOH wins the veto they will not change their nominations
  - if there is a tie for lowest two relationships within the HOH's relationships then the HOH will randomly choose between changing the nomination or keeping it the same 50/50, if the HOH randomly chooses to change the nominations then it will randomly choose to replace 
  - 
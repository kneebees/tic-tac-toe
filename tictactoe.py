## Multiplayer Tic Tac Toe game

#import random
import random

#create the tic tac toe board
toe = [['   ', '|', '   ', '|', '   ', ' 1', '\n-----------\n'], ['   ', '|', '   ', '|', '   ', ' 2', '\n-----------\n'], ['   ', '|', '   ', '|', '   ', ' 3\n'], [' A  ', ' B  ', ' C ']]
#Create a variable to store where the symbols are so that they aren't placed in the same spot
guessed = []
#create a variable called game to store how the game ends
game = ''
#variable to store whether the player wants to be x or o
xo1 = ''
#variables to store different options of coordinates
abc = ['A', 'B', 'C']
num = ['1', '2', '3']
abcnum = ["A1", 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
abc123 = ''
#variable called play which stores the names of the players
play = ["Player 1", "Player 2"]
#variable that stores the order of the players (who goes first)
plays = []
#variables that keep what symbol is for which player
player1 = ''
player2 = ''

#create function to print out gameboard
def gameboard():
  print("\n")
  for tac in toe:
    for tic in tac:
      print(tic, end = '')
  print("\n")

def reverseroles(play):
  if play == "Player 1":
    play = play.replace("Player 1", "Player 2")
  elif play == "Player 2":
    play = play.replace("Player 2", "Player 1")

#intro
print("Welcome to Tic Tac Toe. This is a multiplayer game requiring 2 players. A player will be chosen at random to go first. To select an area, enter the number(y axis) and the letter(x axis) that it corresponds to. To win, you have to get 3 of your symbol in a row (horizontal, vertical, or diagonal). \n*If you get a draw, just continue putting inputting symbols until the board is filled.")
#print gameboard
gameboard()
#ask for what the symbol will be
while True:
  xo1 = input("\nWould you like to be player x or player o? ").upper()
  if xo1 == "O":
    player1 = " O "
    player2 = " X "
    break
  elif xo1 == "X":
    player1 = " X "
    player2 = " O "
    break
  else:
    print("Type x or o. Try again.")
print("That means that Player 2 is {}.".format(player2))
#randomly choose which player will fo first
play = random.choice(play)
print("{} will go first.".format(play))
#tell the program what the order will be
if play == "Player 1":
  plays = [player1, player2]
elif play == "Player 2":
  plays = [player2, player1]
#keep on running the rounds until they are broken (win/draw)
while True:
  #start a round
  for player in plays:
    while True:
      abc123 = input("\n{}: Where would you like to place your {}? ".format(play, player)).upper()
      if abc123 in guessed:
        print("A piece is already in this spot. Try again.")
      elif abc123 not in abcnum:
        print("Your answer was invalid. Type in a letter and number as indicated on the board. ")
      if abc123 in abcnum and abc123 not in guessed:
        abc124 = list(abc123)
        guessed.append(abc123)
        break
    axisabc = -2
    for i in abc:
      axis123 = 0
      axisabc += 2
      if i in abc124:
        for j in num:
          if j in abc124:
            toe[axis123][axisabc] = player
            gameboard()
          axis123 += 1
    if play == "Player 1":
      play = play.replace("Player 1", "Player 2")
    elif play == "Player 2":
      play = play.replace("Player 2", "Player 1")
    for i in range(3):
      if toe[i][0] == player and toe[i][2] == player and toe[i][4] == player:
        game = "end"
      elif toe [0][0] == player and toe[1][0] == player and toe[2][0] == player:
        game = "end"
      elif toe [0][2] == player and toe[1][2] == player and toe[2][2] == player:
        game = "end"
      elif toe [0][4] == player and toe[1][4] == player and toe[2][4] == player:
        game = "end"
      elif toe[0][0] == player and toe[1][2] == player and toe[2][4] == player:
        game = "end"
      elif toe[0][4] == player and toe[1][2] == player and toe[2][0] == player:
        game = "end"
    if '   ' not in toe[0] and '   ' not in toe[1] and '   ' not in toe[2]:
      game = "draw"
    if game == 'end' or game == 'draw':
      break
  if game == "end":
    if play == "Player 1":
      print("Player 2 has won the game. ")
      break
    elif play == "Player 2":
      print("Player 1 has won the game. ")
      break
  if game == "draw":
    print("The game has ended in a draw.")
    break

# 
# Author: Helen Hua
# Date: December 27 2021
# Summary: A game of tic tac toe in Python. First to 3 in a row wins 

# Function that prints the playing board
def print_board():
  section_a = "  +---+---+---+"

  # Print the first line of numbers
  print("    1   2   3   ")
  for row in range(3):
    print(section_a)
    #resets section_b to an empty string for each row
    num = str(row+1)
    section_b = num + " "
    for col in range(3):
      section_b += ("| " + str(board[row][col]) + " ")
     
    # Prints row B the last line on the right of each B row
    print(section_b + "|")
   
  #After the loops iterate, print the final section d once to close the board off
  print(section_a)

# Returns true if there is 3 in a row left to input piece
def left(array, row, col, x_or_o):
  counter = 0
  while col >= 0:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    col-=1

  if(counter==3):
    return True;
  
  return False;

# Returns true if there is 3 in a row above input piece
def up(array, row, col, x_or_o):
  counter = 0
  while row >= 0:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    row-=1
  
  if(counter==3):
    return True;
  
  return False;

# Returns true if there is 3 in a row top left diagonal to input piece
def top_left(array, row, col, x_or_o):
  counter = 0
  while row >= 0 and col >= 0:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    row-=1
    col-=1

  if(counter==3):
    return True;
  
  return False;

# Returns true if there is 3 in a row top right diagonal to input piece
def top_right(array, row, col, x_or_o):
  counter = 0
  while row >= 0 and col <= 2:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    row-=1
    col+=1
 
  if(counter==3):
    return True;
  
  return False; 

# Returns true if there is 3 in a row
def win(array, x_or_o):
  # Initiate the win state as false to begin
  win = False
  
  # Traverses through the board array and looks for X or O depending on its argument then initiates a score keeping counter to 1. If any cases are true, then win will be true too
  for row in range(0, 3, 1):
    for col in range(0,3,1):
      
      if array[row][col] == x_or_o:
        
        if left(array, row, col, x_or_o):
          win = True

        if up(array, row, col, x_or_o):
          win = True

        if top_left(array, row, col, x_or_o) or top_right(array, row, col, x_or_o):
          win = True

  return win            

# Main code

# Initiation of board
board = [
  [' ',' ',' '],
  [' ',' ',' '],
  [' ',' ',' ']
]

#Initiates the round counter to 1
counter = 1
game_won = False
welcome_message = """Welcome to Helen's Tic Tac Toe game! 

Get 3 in a row before your opponent to win the game!

"""

# Starts the game off by printing a welcome message and the board by calling the print board function
print(welcome_message)
print_board()

# Continues iterating through the game until there is a winner or the entire board is filled after 9 turns
while(not game_won and counter <= 9):
  
  # Alternates between player O and player X's turns depending on the turn number
  if counter % 2 == 1:
    turn = 'O'
  else:
    turn = 'X'
  
  #scan col input from user
  user_input = input("Enter the row: ")
  
  # Finds the index that corresponds to the input
  row = int(user_input) - 1

  user_input2 = input("Enter the col: ")
  col = int(user_input2) - 1

  # Prints error statement if a coordinate does not exist
  if(row >= 3 or row<0 or col >= 3 or col < 0):
    print("Box does not exist. Please try again");
    counter-=1

  # If the input coordinate is empty, then fill it with the user's character (either X or O)
  elif board[row][col] == ' ':
    board[row][col] = turn

  # If the box is occupied print message
  else:
    print("The box is already filled, please enter another box")
    counter-=1   
  
  #Prints the board so the user can see what they inputted
  print_board()
  
  # Check for a winner
  game_won = win(board, turn)
  
  # If no winner, at the end of each turn, inrease the counter by one 
  counter+=1

# If no one wins by round 9, then print tie. If there is a winner, print winner message
if(counter > 9):
  print("It's a tie!")

else:
  print("Game over! Player " + turn + " is the winner!")

print("======= TIC - TAC - TOE=======")
#declaration of board
board=["-","-","-",
       "-","-","-",
       "-","-","-",]
#GLOBAL DECLARATIONS
#to know the status of the game
game_still_on=True

#initially declared as none
winner=None

#comes handy in further process
current_player="x"

#its like a main function game_on
def game_on():
    #function call to display board
    display_board()
    while game_still_on:
        #to know the turn of the player "x" or "o"
        whose_turn(current_player)
        #checks whether the game is over
        if_game_over()
        #for flipping of the players
        opp_player()
    #to determine the winner   
    if winner=="x" or winner=="o":
        print(winner+" Won the Tic-Tac-toe.")
    elif winner==None:
        print("Its a Tie.\n")
    
def display_board():
    #function defn to print the board
    print("\n")
    print(board[0]+"|"+board[1]+"|"+board[2]+ "   1 | 2 | 3")
    print(board[3]+"|"+board[4]+"|"+board[5]+ "   4 | 5 | 6")
    print(board[6]+"|"+board[7]+"|"+board[8]+ "   7 | 8 | 9")
    print("\n")

def whose_turn(player):
    #display's whose turn
    print(player+" 's turn")
    position=input("Choose a position from 1 to 9: ")
    #Validation-important
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("Choose a position from 1 to 9: ")
        position=int(position)-1
        if board[position]=="-":
            valid=True
        else:
            print("You cannot insert there, Go again")
    #assign the value contained in player in the board
    board[position]=player
    display_board()
           
def if_game_over():
    #check if there is win
    check_win()
    #check if there is tie
    check_tie()
           
def check_win():
    #declared globally
    global winner
    #checking in row
    row_winner=check_row()
    #hecking in coloumn
    coloumn_winner=check_coloumn()
    #checking in diagonal
    diagonal_winner=check_diagonal()
    if row_winner:
        winner=row_winner
    elif coloumn_winner:
        winner=coloumn_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
           
def check_row():
    #declared globally
    global game_still_on
    #check if they are equal
    row_1=board[0]==board[1]==board[2]!="-"
    row_2=board[3]==board[4]==board[5]!="-"
    row_3=board[6]==board[7]==board[8]!="-"
    #check if anyone of them is equal
    if row_1 or row_2 or row_3:
        game_still_on=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_coloumn():
    #declared globally
    global game_still_on
    #check if they are equal
    col_1=board[0]==board[3]==board[6]!="-"
    col_2=board[1]==board[4]==board[7]!="-"
    col_3=board[2]==board[5]==board[8]!="-"
    #check if anyone of them is equal
    if col_1 or col_2 or col_3:
        game_still_on=False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None

def check_diagonal():
    #declared globally
    global game_still_on
    dia_1=board[0]==board[4]==board[8]!="-"
    dia_2=board[2]==board[4]==board[6]!="-"
    #as there are 2 diagonals check if anyone is equal
    if dia_1 or dia_2:
        game_still_on=False
    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
    else:
        return None

def check_tie():
    #check if there is a tie
    global game_still_on
    if "-" not in board:
        game_still_on=False
        return True
    else:
        return False

def opp_player():
    #declared globally
    global current_player
    #fliping of the player from "x" to "o" and vice-versa
    if current_player=="x":
        current_player="o"
    elif current_player=="o":
        current_player="x"

#start of the execution 
game_on()

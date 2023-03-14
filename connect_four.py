import random
import sys

board=[]
game_state=True
player_turn=True
winner=None
name=input("Enter name: ")
print("You select X, the computer selects O")

def create_empty_board():
    for i in range(6):
        board.append(['_']*6)
def print_board():
    print('\n')
    for row in board:
        print(' '.join(row))

def check_column(col):
    return board[0][col]=="_"

def add_piece(col, row, piece):
    board[row][col]=piece

def check_winner(piece):
    #horizontally
    for row in range(6):
        for col in range(3):
            if board[row][col]==piece and board[row][col+1]==piece and board[row][col+2]==piece and board[row][col+3]==piece:
                return True
    #perpendicularly
    for row in range(3):
        for col in range(6):
            if board[row][col]==piece and board[row+1][col]==piece and board[row+2][col]==piece and board[row+3][col]==piece:
                return True
    #diagonally
    for row in range(3):
        for col in range(4):
            if board[row][col]==piece and board[row+1][col+1]==piece and board[row+2][col+2]==piece and board[row+3][col+3]==piece:
                return True
    for row in range(3):
        for col in range(3,6):
            if board[row][col]==piece and board[row+1][col-1]==piece and board[row+2][col-2]==piece and board[row+3][col-3]==piece:
                return True
    return False

def check_board_full():
    for col in range(6):
        if check_column(col):
            return False
        return True

def get_row(col):
    for row in range(5,-1,-1):
        if board[row][col]=='_':
            return row

def computer_move():
        # preventing the player from winning
        # horizontally
    for row in range(6):
        for col in range(3):
            if board[row][col]==board[row][col+1]=='X' and board[row][col+2]==board[row][col+3]=='_' \
                or board[row][col]==board[row][col+1]==board[row][col+2]=='X' and board[row][col+3]=='_':
                    return col+3
            elif board[row][col]==board[row][col+1]=='_' and board[row][col+2]==board[row][col+3]=='X' \
                or board[row][col]=='_' and board[row][col+1]==board[row][col+2]==board[row][col+3]=='X':
                    return col
            elif board[row][col+1]=='_' and board[row][col]==board[row][col+2]==board[row][col+3]=='X':
                    return col+1
        # perpendicularly
    for row in range(3):
        for col in range(6):
            if board[row][col]==board[row+1][col]=='X' and board[row+2][col]==board[row+3][col]=='_'\
                or board[row+3][col]==board[row+2][col]=='_' and board[row+1][col]==board[row][col]=='X' \
                or board[row][col]==board[row+1][col]==board[row+2][col]=='X' and board[row+3][col]=='_':
                    return col
        # diagonally
    for row in range(3):
        for col in range(3, 6):
            if board[row][col]==board[row+1][col-1]=='X' and board[row+2][col-2]==board[row+3][col-3]=='_' \
                or board[row][col]==board[row+1][col-1]==board[row+2][col-2]=='X' and board[row+3][col-3]=='_':
                    return col-3
            elif board[row][col]==board[row+1][col-1]==board[row+3][col-3]=='X' and board[row+2][col-2]=='_':
                    return col-2
            elif board[row][col]==board[row+1][col-1]=='_' and board[row+2][col-2]==board[row+3][col-3]=='X':
                    return col
            elif board[row+1][col-1]=='_' and board[row+2][col-2]==board[row][col]==board[row+3][col-3]=='X':
                    return col-1
    for row in range(3):
        for col in range(3):
            if board[row][col]==board[row+1][col+1]=='X' and board[row+2][col+2]==board[row+3][col+3]=='_' \
                or board[row][col]==board[row+1][col+1]==board[row+2][col+2]=='X' and board[row+3][col+3]=='_':
                    return col+3
            elif board[row][col]==board[row+1][col+1]==board[row+3][col+3]=='X' and board[row+2][col+2]=='_':
                    return col+2
            elif board[row][col]==board[row+1][col+1]=='_' and board[row+2][col+2]==board[row+3][col+3]=='X':
                    return col
            elif board[row+1][col+1]=='_' and board[row+2][col+2]==board[row][col]==board[row+3][col+3]=='X':
                    return col+1
    if col==-1:
        #computer win search:
        #horizontally
        for row in range(6):
            for col in range(3):
                if board[row][col]==board[row][col+1]=='O' and board[row][col+2]==board[row][col+3]=='_'\
                    or board[row][col]==board[row][col+1]==board[row][col+2]=='O' and board[row][col+3]=='_':
                        return col+3
                elif board[row][col]==board[row][col+1]=='_' and board[row][col+2]==board[row][col+3]=='O':
                        return col
                elif board[row][col+1]=='_' and board[row][col]==board[row][col+2]==board[row][col+3]=='O':
                        return col+1
        #perpendicularly
        for row in range(3):
            for col in range(6):
                if board[row][col]==board[row+1][col]=='O' and board[row+2][col]==board[row+3][col]=='_' \
                    or board[row+3][col]==board[row+2][col]=='_' and board[row+1][col]==board[row][col]=='O'\
                    or board[row][col]==board[row+1][col]==board[row+2][col]=='O' and board[row+3][col]=='_':
                        return col
        #diagonally
        for row in range(3):
            for col in range(3, 6):
                if board[row][col]==board[row+1][col-1]=='O' and board[row+2][col-2]==board[row+3][col-3]=='_'\
                    or board[row][col]==board[row+1][col-1]==board[row+2][col-2]=='O' and board[row+3][col-3]=='_':
                        return col-3
                elif board[row][col]==board[row+1][col-1]==board[row + 3][col-3]=='O' and board[row+2][col-2]=='_':
                        return col-2
                elif board[row][col]==board[row+1][col-1]=='_' and board[row+2][col-2]==board[row+3][col-3]=='O':
                        return col
                elif board[row+1][col-1]=='_' and board[row+2][col-2]==board[row][col]==board[row+3][col-3]=='O':
                        return col-1
        for row in range(3):
            for col in range(3):
                if board[row][col]==board[row+1][col+1]=='O' and board[row+2][col+2]==board[row+3][col+3]=='_'\
                    or board[row][col]==board[row+1][col+1]==board[row+2][col+2]=='O' and board[row+3][col+3]=='_':
                        return col+3
                elif board[row][col]==board[row+1][col+1]==board[row+3][col+3]=='O' and board[row+2][col+2]=='_':
                        return col+2
                elif board[row][col]==board[row+1][col+1]=='_' and board[row+2][col+2]==board[row+3][col+3]=='O':
                        return col
                elif board[row+1][col+1]=='_' and board[row+2][col+2]==board[row][col]==board[row+3][col+3]=='O':
                        return col+1
    while True:
        if col==-1:
            col=random.randint(0, 5)
        if check_column(col):
            return col

def change_turn():
    global player_turn
    player_turn=not player_turn

def play():
    create_empty_board()
    print_board()

    player_wins=0
    computer_wins=0
    global game_state
    global player_turn
    global name

    while True:
        while game_state:
            if player_turn:
                choice=int(input(print(f'{name}, Select a column (1-6):')))
                choice-=1
                if check_column(choice):
                    row=get_row(choice)
                    add_piece(choice, row, 'X')
                    print_board()

                    if check_winner('X'):
                        print(f'{name}, you won! Congratulations!')
                        player_wins+=1
                        game_state=False
                        answer=input("Play on? (t/f): ")
                        if answer.lower()=='t':
                            game_state=True
                            player_turn=True
                            board.clear()
                            create_empty_board()
                            print_board()
                            continue
                        else:
                            game_state = False
                            break
                    elif check_board_full():
                        print('Tie!')
                        game_state=False
                        answer=input("Play on? (t/f): ")
                        if answer.lower()=='t':
                            game_state= True
                            player_turn=True
                            board.clear()
                            create_empty_board()
                            print_board()
                            continue
                        else:
                            game_state=False
                            sys.exit(0)
                    else:
                        change_turn()
                else:
                    print('\The column is full, try again.')
            else:
                col=computer_move()
                if check_column(col):
                    row=get_row(col)
                    add_piece(col, row, 'O')
                    print_board()

                    if check_winner('O'):
                        print("Komputer wygrywa!")
                        computer_wins+=1
                        game_state=False
                        answer=input("Play on? (t/f): ")
                        if answer.lower()=='t':
                            game_state=True
                            player_turn=True
                            board.clear()
                            create_empty_board()
                            print_board()
                            continue
                        else:
                            game_state=False
                            sys.exit(0)
                        break
                    else:
                        if check_board_full():
                            print('Tie!')
                            game_state=False
                            answer=input("Play on? (t/f): ")
                            if answer.lower()=='t':
                                game_state=True
                                player_turn=True
                                board.clear()
                                create_empty_board()
                                print_board()
                                continue
                            else:
                                game_state=False
                                sys.exit(0)
                            break
                        else:
                            change_turn()

            print(f'\n{name}: {player_wins}\nComputer: {computer_wins}')
play()

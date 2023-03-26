from IPython.display import clear_output
import os

def clear_scr():
    if os.name == 'posix':
        os.system('clear')
def game():
    winner = ''
    board = [
        ' ',' ',' ',
        ' ',' ',' ',
        ' ',' ',' ']
    clear_scr()
    show_board(board)
    player_1 = True
    
    while board.count(' ') > 0:
        
        choice = int(input('Player {}:Choose a position'.format('1' if player_1 else '2')))
        if board[choice-1] != ' ':
            print('already filled')
            continue
        board[choice-1] = 'X' if player_1 else 'O'
        
        clear_output()
        clear_scr()
        show_board(board)
        player_1 = not player_1
        winner = check_winner(board)

        if winner:
            break
        
        
    print('Game Finished.{}'.format('Winner is {}'.format(winner) if winner else 'It\'s a draw'))

        
def show_board(board):
    print('''
    -------------
    | {} | {} | {} |
    -------------
    | {} | {} | {} |
    -------------
    | {} | {} | {} |
    -------------
    
    '''.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6],board[7], board[8]))
    
def check_winner(board):
    if board[0] == board[1] == board[2] != ' ':
        winner = '1' if board[0] == 'X' else '2'
        print('Player {} is winner'.format(winner))
        return winner
    elif board[0] == board[3] == board[6] != ' ':
        winner = '1' if board[0] == 'X' else '2'
        print('Player {} is winner'.format(winner))
        return winner
    elif board[0] == board[4] == board[8] != ' ':
        winner = '1' if board[0] == 'X' else '2'
        print('Player {} is winner'.format())
        return winner
    elif board[1] == board[4] == board[7] != ' ':
        winner = '1' if board[1] == 'X' else '2'
        print('Player {} is winner'.format(winner))
        return winner
    elif board[2] == board[4] == board[6] != ' ':
        winner = '1' if board[2] == 'X' else '2'
        print('Player {} is winner'.format(winner))
        return winner
    
    elif board[2] == board[5] == board[8] != ' ':
        winner = '1' if board[2] == 'X' else '2'
        print('Player {} is winner'.format(winner))
        return winner
    elif board[3] == board[4] == board[5]!=' ':
        winner = '1' if board[3] == 'X' else '2'
        print('Player {} is winner'.format(winner))
        return winner
    elif board[6] == board[7] == board[8]!=' ':
        winner = '1' if board[6] == 'X' else '2'
        print('Player {} is winner'.format(winner))
        return winner

game()

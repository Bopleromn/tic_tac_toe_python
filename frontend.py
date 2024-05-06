import backend
import time
import random


def main():
    while True:
        user_player: str = input('За кого будете играть: X или O? ').strip().upper()
        if user_player == backend.X or user_player == backend.O:
            break
        else:
            print('Выберите существующего игрока')
            
    board = backend.initial_state()
    
    print('Игра началась')
    print_board(board)
    
    while not backend.terminal(board):
        current_player: str = backend.player(board)
        
        if current_player == user_player:
            while True:
                coords: str = input(f'Ваш ход ({current_player}), введите координаты на доске через запятую: ')
                
                try:
                    board = backend.result(board, action=tuple((int(coord.strip()) for coord in coords.strip().split(','))))
                    
                    print_board(board)
                    break
                except:
                    print('Введены неверные координаты. Попробуйте еще раз')
                    continue
        else:
            print(f'Ход игрока {current_player}')
            time.sleep(0.5)
            
            action: tuple = backend.minimax(board) if board != backend.initial_state() else tuple(random.sample(range(0, 2), 2))
            board = backend.result(board, action) 
            
            print_board(board)
            
    print(f'Игра окончена! ', end='')
    
    winner = backend.winner(board)
    
    if winner is not None:
        print(f'Вы победили ({current_player})') if user_player == winner else print(f'Вы проиграли, победитель: {current_player}')   
    else:
        print('Ничья')
    
    
def print_board(board):
    for row in board:
        for j, sym in enumerate(row):
            if j < 2:
                print(' |', end='') if sym == backend.EMPTY else print(f'{sym}|', end='')
            elif sym != backend.EMPTY:
                print(sym, end='')
            
        print()
    
    
main()
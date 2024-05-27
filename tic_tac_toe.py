def print_board(board):
    print("  0 1 2")
    for idx, row in enumerate(board):
        print(f"{idx} {' '.join(row)}")

def check_winner(board, player):
    # Проверка строк
    for row in board:
        if all(s == player for s in row):
            return True
    # Проверка столбцов
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # Проверка диагоналей
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Игрок {current_player}, введите номер строки (0, 1, 2): "))
            col = int(input(f"Игрок {current_player}, введите номер столбца (0, 1, 2): "))

            if row not in range(3) or col not in range(3):
                print("Неправильный ввод. Пожалуйста, введите числа от 0 до 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Игрок {current_player} победил!")
                    break
                if is_board_full(board):
                    print_board(board)
                    print("Ничья!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Эта клетка уже занята. Попробуйте еще раз.")
        except ValueError:
            print("Неправильный ввод. Пожалуйста, введите числа.")

if __name__ == "__main__":
    tic_tac_toe()
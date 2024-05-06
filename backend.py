from copy import deepcopy


X = "X" 
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count: int = 0
    o_count: int = 0

    for row in board:
        for symbol in row:
            if symbol == X:
                x_count += 1
            elif symbol == O:
                o_count += 1

    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()

    for i, row in enumerate(board):
        for j, symbol in enumerate(row):
            if symbol is EMPTY:
                result.add((i, j))

    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i: int = action[0]
    j: int = action[1]

    if board[i][j] is not EMPTY or i > 2 or i < 0 or j > 2 or j < 0:
        raise Exception(board, action)

    board_copy = deepcopy(board)

    board_copy[i][j] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    symbols = [X, O]

    for symbol in symbols:
        # three symbols in a row horizontally
        if (board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol) or (
            board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol) or (
            board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol):
            return symbol
        # three symbols in a row vertically
        elif (board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol) or (
            board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol) or (
            board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol):
            return symbol
        # three symbols in a row diagnoly
        elif (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol) or (
            board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol):
            return symbol

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return True if winner(board) is not None or len(actions(board)) == 0 else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return { X: 1, O: -1, None: 0 }.get(winner(board))


def minimax(board) -> set:
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    outcomes = {}

    for action in actions(board):
        outcomes[action] = get_best_outcome(result(board, action))

    return [action for action in outcomes if outcomes[action] == (max(outcomes.values()) if player(board) == X else min(outcomes.values()))][0]


def get_best_outcome(board) -> int:
    if terminal(board):
        return utility(board)

    results = []

    for action in actions(board):
        results.append(get_best_outcome(result(board, action)))

    return min(results) if player(board) is O else max(results)
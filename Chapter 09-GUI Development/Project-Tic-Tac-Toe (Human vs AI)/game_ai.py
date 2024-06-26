import random
from game_mechanics import check_winner, EMPTY_SPOT, X_PLAYER, O_PLAYER


def get_random_ai_move(board):
    available_spots = [index for index, spot in enumerate(board) if spot == EMPTY_SPOT]
    return random.choice(available_spots)


def test_move(board, player, position):
    temp_board = board.copy()
    temp_board[position] = player
    return check_winner(temp_board) == player


def get_rules_based_ai_move(computer_player, board):
    # Try for a Win
    for i in range(9):
        if board[i] == EMPTY_SPOT and test_move(board, computer_player, i):
            return i

    # Block Opponent
    human_player = X_PLAYER if computer_player == O_PLAYER else O_PLAYER
    for i in range(9):
        if board[i] == EMPTY_SPOT and test_move(board, human_player, i):
            return i

    # Try Center or Corners
    corners = [0, 2, 6, 8]
    if board[4] == EMPTY_SPOT:
        return 4  # Prefer the center
    random.shuffle(corners)
    for i in corners:
        if board[i] == EMPTY_SPOT:
            return i

    # Pick Randomly
    return random.choice([i for i in range(9) if board[i] == EMPTY_SPOT])

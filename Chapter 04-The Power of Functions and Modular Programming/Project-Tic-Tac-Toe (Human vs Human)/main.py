from game_mechanics import check_winner, check_draw, initialize_board, X_PLAYER, O_PLAYER
from game_ui import display_board, get_human_player_move, display_help


def play_game():

    while True:
        board = initialize_board()  # Initialize the board
        current_player = X_PLAYER  # Start with player 'X'
        game_is_playing = True

        display_help(board.copy())

        while game_is_playing:
            display_board(board)  # Display the board

            move = get_human_player_move(current_player, board)
            if move is None:
                break

            board[move] = current_player  # Update the board with the player's move

            if check_winner(board):  # Check for win
                display_board(board)
                print(f"Congratulations, Player {current_player}! You've won the game.")
                game_is_playing = False
            elif check_draw(board):  # Check for draw
                display_board(board)
                print("The game is a draw!")
                game_is_playing = False
            else:
                current_player = O_PLAYER if current_player == X_PLAYER else X_PLAYER  # Switch players

        print("Game over.")

        again = input("Would you like to play (Y/N)?").upper()  # Play Again?
        if again == "N":
            break


if __name__ == "__main__":
    play_game()

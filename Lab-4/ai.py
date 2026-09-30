import random


class AI:
    def choose_column(self, board, me="O", opponent="X"):

        legal = [c for c in range(7) if board.grid[0][c] == "."]

        if not legal:
            return None

        # Check for an immediate winning move.
        for col in legal:
            row = board.drop(col, me)

            if board.winner(me):
                board.grid[row][col] = "."
                return col

            board.grid[row][col] = "."

        # Check if the opponent has an immediate winning move.
        for col in legal:
            row = board.drop(col, opponent)

            if board.winner(opponent):
                board.grid[row][col] = "."
                return col

            board.grid[row][col] = "."

        # Otherwise, choose any legal column.
        return random.choice(legal)
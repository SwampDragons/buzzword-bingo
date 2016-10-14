import random
from buzzwords import buzzwords


class Board:
    def __init__(self, username):
        self.username = username
        random.seed()
        self.words = random.sample(buzzwords, 25)
        self.words[12] = 'saucederps'  # free space! replace with saucederps img
        self.clicked_words = []

    def __str__(self):
        return str(self.words)

    def check_for_win(self):
        """Determine whether clicked_list contains any bingos."""
        # clicked list should be a 25-element list of booleans.  E.g.
        # [True, False, True, True, False ...]

        # Bingo board indexing looks like this when mapped to 2D:

        # 0  1  2  3  4
        # 5  6  7  8  9
        # 10 11 12 13 14
        # 15 16 17 18 19
        # 20 21 22 23 24

        bingos = [# horizontal bingos
                  range(0, 5),
                  range(5, 10),
                  range(15, 20),
                  range(20, 25),
                  # vertical bingos
                  range(0, 25, 5),
                  range(1, 25, 5),
                  range(2, 25, 5),
                  range(3, 25, 5),
                  range(4, 25, 5),
                  range(5, 30, 5),
                  # diagonal bingos
                  range(0, 25, 6),
                  range(4, 24, 4)]

        index = 0
        clicked_indices = []
        for status in self.clicked_words:
            if status is True:
                clicked_indices.append(index)
            if index is 12:  # saucederps is free!
                clicked_indices.append(index)
            index += 1

        for bingo in bingos:
            bingoed = all(x in bingo for x in clicked_indices)
            if bingoed:
                # will use this list to generate the list of winning words
                return bingo

        return []

    def get_clicked_words(self, clicked_list):
        clicked_list.sort()
        clicked_words = []
        index = 0
        for word in self.words:
            if index in clicked_list:
                clicked_words.append(word)
            index += 1
        return clicked_words

    def get_winning_words(self, bingo):
        return self.get_clicked_words(bingo)


class Game:
    """ Game object represents a game.  Each session is a session ID."""

    def __init__(self):
        self.words = buzzwords
        self.boards = {}

    def get_board(self, username):
        if username in self.boards:
            return self.boards[username]
        else:
            return self.generate_board(username)

    def generate_board(self, username):
        board = Board(username)
        self.boards[username] = board

        return board

    def win(self, username):
        """ Checks if a session is a winner.
        """
        board = self.boards[username]
        if not board:
            # no such session
            return False
        bingo = board.check_for_win()
        if bingo:
            print bingo
            return board.get_winning_words(bingo)

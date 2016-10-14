import random
import buzzwords


class Board:
    def __init__(self, seed, dim, words):
        self.rng = random.Random()
        self.seed = seed
        self.rng.seed(seed)
        self.dim = dim
        self.cells = []
        self.cells = [[ self.new_word(words) for i in range(dim)] for j in range(dim)]
        self.claims = [[ False for i in range(dim)] for j in range(dim)]

    def session_id(self):
        return self.seed

    def new_word(self, words):
        while True:
            word = self.rng.choice(words)
            if not self.has_word(word):
                return word

    def has_word(self, word):
        for row in self.cells:
            for w in row:
                if w == word:
                    return True
        return False

    def claim(self, word):
        """ Claims a word for a given session.  Returns True if the word
            is on the board, False otherwise.
        """
        for row in range(self.dim):
            for col in range(self.dim):
                if self.cells[row][col] == word:
                    self.claims[row][col] = True
                    return True
        return False

    def winner(self):
        """ Returns array of winning words if the board is a winner
        False otherwise.
        """
        # Check rows, then columns, then diagonals.
        # Rows first:
        for row in range(self.dim):
            win = True
        winwords = []
        for col in range(self.dim):
            if not self.claims[row][col]:
                win = False
                break
        winwords.append(self.cells[row][col])
        if win:
            return winwords

        # Columns next
        for col in range(self.dim):
            win = True
        winwords = []
        for row in range(self.dim):
            if not self.claims[row][col]:
                win = False
                break
        winwords.append(self.cells[row][col])
        if win:
            return winwords

        # Diagonal \ next
        win = True
        winwords = []
        for x in range (0, self.dim):
            if not self.claims[x][x]:
                win = False
                break
        winwords.append(self.cells[x][x])
        if win:
                return winwords

        # Diagonal / next
        win = True
        winwords = []
        for x in range(self.dim):
            if not self.claims[x][self.dim-x-1]:
                win = False
                break
        winwords.append(self.cells[x][self.dim-x-1])
        if win:
                return winwords

        return False

    def words(self):

        return self.cells

    def draw(self):
        print "Seed", self.seed
        print "Words"
        # w = self.words
        for i in range(self.dim):
            for j in range(self.dim):
                print self.cells[i][j],
            print
        if self.winner():
            print "WINNER"
            for i in range(self.dim):
                for j in range(self.dim):
                    print self.claims[i][j],
        print


class Game:

    """ Game object represents a game.  Each session is a session ID.
    """

    def __init__(self):
        self.rng = random.Random()
        # maybe we don't need all this?
        self.seed = self.rng.getrandbits(32)
        self.rng.seed(self.seed)
        self.words = buzzwords.buzzwords
        self.dim = 5
        self.boards = {}

    def generate(self):

        session = self.rng.getrandbits(32)
        board = Board(session, self.dim, self.words)
        self.boards[session] = board

        return board

    def claim(self, session, word):

        """ Claims a word for a session.
        """
        board = self.boards[session]
        if not board:
            # invalid session
            return False
        if not board.claim(word):
            # word not found on board
            return False

        return True

    def win(self, session):
        """ Checks if a session is a winner.
        """
        board = self.boards[session]
        if not board:
            # no such session
            return False
        return board.winner()

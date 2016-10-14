class Board:
    def __init__(seed, dim, words):
        self.rng = random.Random()
        self.seed = seed
        self.rng.seed(seed)
        self.dim = dim
        for row in range (0, dim):
            for col in range (0, dim):
                self.words[row][col] = self.rng.choice(words)
                self.claims[row][col] = false

    def session_id():
        return self.seed

    def claim(word):
        """ Claims a word for a given session.  Returns true if the word
            is on the board, false otherwise.
        """
        for row in range (0, self.dim):
            for col in range (0, self.dim):
                if self.words[row][col] == word:
                    claims[row][col] = true
                    return true
        return false

    def winner():
        """ Returns true if the board is a winner, false otherwise.
        """
        # Check rows, then columns, then diagonals.
        # Rows first:
        for row in range (0, self.dim):
            winner = true
            for col in range (0, self.dim):
                if not self.claims[row][col]:
                    winner = false
                    break
            if winner:
                return true
        # Columns next
        for col in range (0, self.dim):
            winner = false
            for row in range (0, self.dim):
                if not self.claims[row][col]:
                    winner = false
                    break
            if winner:
                return true
        # Diagonal \ next
        winner = true
        for x in range (0, self.dim):
            if not self.claims[x][x]:
                winner = false
                break
        if winner:
                return true

        # Diagonal / next
        winner = true
        for x in range (0, self,dim):
            if not self.claims[x][self.dim-x-1]:
                winner = false
                break
        if winner:
                return true

        reutrn false

    # word list is array in self.words


class Game:

    """ Game object represents a game.  Each session is a session ID.
    """

    def __init__(self):
        self.rng = random.Random()
        # maybe we don't need all this?
        self.seed = self.rng.getrandbits(32)
        self.rng.seed(self.seed)
        self.words = buzzwords
        self.rows = 5
        self.cols = 5
        self.boards = {}

    def generate():

        session = self.rng.getrandbits(32)
        board = Board(session, self.rows, self.cols, words)
        self.boards[session] = board

        return board
 

    def claim(session, word):

        """ Claims a word for a session.
        """
        board = self.boards[session]
        if not board:
            # invalid session
            return false
        if not board.claim(word):
            # word not found on board
            return false

        return true
        
    def win(session):
        """ Checks if a session is a winner.
        """
        board = self.boards[session]
        if not board:
            # no such session
            return false
        return board.winner()


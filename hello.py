from flask import *
from buzzwords import buzzwords
import random

app = Flask(__name__)


def validate(clicked_list):
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
    for status in clicked_list:
        if status is True:
            clicked_indices.append(index)
        index += 1

    for bingo in bingos:
        bingoed = all(x in bingo for x in clicked_indices)
        if bingoed:
            return bingo


@app.route("/")
def hello():
    random.seed()
    words = random.sample(buzzwords, 25)
    words[12] = 'saucederps' # free space! replace with saucederps img
    return render_template('view.html',buzzwords=words)

if __name__ == "__main__":
    app.run(debug=True)
from flask import *
from buzzwords import buzzwords
import random
import game

app = Flask(__name__)


@app.route("/")
def hello():
    random.seed()
    words = random.sample(buzzwords, 25)
    words[12] = 'saucederps'  # free space! replace with saucederps img
    return render_template('view.html', buzzwords=words)

if __name__ == "__main__":
    app.run(debug=True)

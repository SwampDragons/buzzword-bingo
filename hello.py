from flask import *
from game import Game

app = Flask(__name__)

thisgame = Game()


@app.route("/checkbingo/<username>", methods=['POST'])
def checkbingo(username):
    # Load list of clicked words
    clicked_json = request.form.getlist('list')
    clicked_list = json.loads(clicked_json[0])
    user_board = Game.get_board(username)


@app.route("/<username>")
def hello(username):
    user_board = thisgame.get_board(username)
    return render_template('view.html', buzzwords=user_board.words)

if __name__ == "__main__":
    app.run(debug=True)

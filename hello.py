from flask import *
from game import Game

app = Flask(__name__)

thisgame = Game()


@app.route("/", methods=['GET'])
def hello_world():
    return "It's working and it automatically updates! ...one more check."


@app.route("/checkbingo/<username>", methods=['POST'])
def checkbingo(username):
    clicked_json = request.form.getlist('list')
    clicked_list = json.loads(clicked_json[0])
    user_board = thisgame.get_board(username)
    user_board.clicked_words = clicked_list
    winning_words = thisgame.win(username)
    if winning_words:
        return "%s won with the following words: %s " % (username, ', '.join(winning_words))
    return ""

@app.route("/<username>")
def hello(username):
    user_board = thisgame.get_board(username)
    return render_template('view.html', buzzwords=user_board.words)

if __name__ == "__main__":
    app.debug = True
    app.run(threaded=True)

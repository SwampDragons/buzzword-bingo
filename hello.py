from flask import *
from buzzwords import buzzwords
import random
import game

app = Flask(__name__)

@app.route("/checkbingo", methods=['POST'])
def checkbingo():
    # MEGAN fix this shiz
    clicked_json = request.form.getlist('list')
    clicked_list = json.loads(clicked_json[0])

@app.route("/")
def hello():
    random.seed()
    words = random.sample(buzzwords, 25)
    words[12] = 'saucederps'  # free space! replace with saucederps img
    return render_template('view.html', buzzwords=words)

if __name__ == "__main__":
    app.run(debug=True)

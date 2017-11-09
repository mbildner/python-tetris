from flask import Flask, render_template
from tetris import Tetris
import json

app = Flask(__name__)

game = None
action_report = None

@app.route("/")
def new_game():
    return render_template('games/new.html')

@app.route("/game/state")
def game_state():
    return json.dumps(action_report.state)

@app.route("/game/move/<direction>", methods=['POST'])
def move_piece(direction):
    if direction not in ['up', 'down', 'left', 'right', 'drop']:
        raise 'Move is invalid'

    global game, action_report
    action_report = game.move_piece(direction)
    return json.dumps(action_report.state)
    

@app.route("/game/start", methods=['POST'])
def start_game():
    global game

    game = Tetris()
    game.start()
    
    global action_report
    action_report = game.move_piece('up')

    return json.dumps(action_report.state)


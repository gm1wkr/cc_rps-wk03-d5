from flask import render_template, request, redirect


from app import app
from models.game import Game
from models.player import Player

@app.route("/")
def index():
    return render_template("index.html", title="Welcome")


@app.route("/<player_1_choice>/<player_2_choice>")
def play_from_url(player_1_choice, player_2_choice):
    player_1 = Player("Player One", player_1_choice)
    player_2 = Player("Player Two", player_2_choice)
    winner = Game.decide_winner(player_1, player_2)

    return render_template(
                            "winner.html", 
                            title="Who Won?", 
                            winner=winner, 
                            player_1=player_1, 
                            player_2=player_2
                        )

@app.route("/play")
def play_game():
    return render_template("play.html", title="Beat the Computer...")

@app.route("/play", methods=["POST"])
def play_computer():
    # handled form data
    name = request.form['name']
    choice = request.form['choice']
    player = Player(name, choice)
    computer = Game.computer_player()
    print(computer)
    winner = Game.decide_winner(player, computer)
    return render_template(
                        "winner.html", 
                        title="Who Won?", 
                        winner=winner, 
                        player_1=player, 
                        player_2=computer
                    )
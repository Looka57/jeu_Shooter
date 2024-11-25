from flask import Flask, render_template
import threading
import subprocess

app = Flask(__name__)

def run_pygame():
    # Lancer le jeu Pygame en tant que processus séparé
    subprocess.run(["python", "game/main.py"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start-game")
def start_game():
    # Lancer le jeu dans un thread
    game_thread = threading.Thread(target=run_pygame)
    game_thread.start()
    return "Le jeu a été lancé ! Revenez pour démarrer une nouvelle partie."

if __name__ == "__main__":
    app.run(debug=True)

from flask import Blueprint, render_template, request, jsonify
from app.models import Player
from app.ai.chat import chat_with_ai
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('lobby.html')

@main.route('/game')
def game():
    return render_template('game.html')

@main.route('/leaderboard')
def leaderboard():
    players = Player.query.order_by(Player.score.desc()).limit(10).all()
    return render_template('leaderboard.html', players=players)

@main.route('/ai_chat', methods=['POST'])
def ai_chat():
    data = request.get_json()
    message = data.get('message')
    reply = chat_with_ai(message)
    return jsonify({"reply": reply})

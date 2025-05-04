from app import socketio, db
from flask_socketio import emit, join_room, leave_room
from app.models import Player
from app.ai.skins import generate_snake_skin
from app.ai.tts import generate_victory_voice
from app.ai.bots import SnakeBot

players_online = {}
bots = {}

@socketio.on('join_game')
def handle_join(data):
    username = data['username']
    room = data['room']

    join_room(room)
    players_online.setdefault(room, []).append(username)

    player = Player.query.filter_by(username=username).first()
    if not player:
        skin_path = generate_snake_skin(username)   # 🎨 Generate skin
        player = Player(username=username, skin_url=skin_path)
        db.session.add(player)
        db.session.commit()

    emit('player_joined', {'username': username}, to=room)

    # Spawn bot if only 1 player
    if len(players_online[room]) == 1:
        spawn_bot_in_room(room)

@socketio.on('player_move')
def handle_move(data):
    room = data['room']
    emit('update_game_state', data, to=room)

@socketio.on('leave_game')
def handle_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    players_online[room].remove(username)

    emit('player_left', {'username': username}, to=room)

    if len(players_online[room]) == 1:
        spawn_bot_in_room(room)

def spawn_bot_in_room(room):
    """Spawn a bot into the room"""
    bot_name = f"Bot_{room}"
    bots[room] = SnakeBot()
    players_online[room].append(bot_name)
    emit('player_joined', {'username': bot_name}, to=room)

@socketio.on('player_win')
def handle_win(data):
    username = data['username']

    # Award score
    player = Player.query.filter_by(username=username).first()
    if player:
        player.score += 100
        db.session.commit()

    # 🎤 Generate TTS Victory voice
    victory_audio_url = generate_victory_voice(f"Congratulations {username}, you win!")
    emit('victory_voice', {'audio_url': victory_audio_url}, to=request.sid)

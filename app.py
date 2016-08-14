from flask import Flask, render_template
from flask_login import current_user, LoginManager, \
    login_user, logout_user
from flask_socketio import SocketIO, emit, join_room
from user import User
from game import Game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ayy lmao'
socketio = SocketIO(app)
login_manager = LoginManager()

pending_games = []
games = []
users = []


# TODO Mel - Add a hook for receiving move data,
# and also one to send data about new players and where they are
# @socketio.on('update')
# def on_update(data):

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.username == user_id:
            return user


@socketio.on('login')
def on_login(data):
    username = data['username']
    for user in users:
        if username == user.username:
            login_user(user)
            emit('login', {'authenticated': True})
            return
    user = User(username)
    users.append(user)
    login_user(user)
    emit('login', {'authenticated': True})


@socketio.on('leave')
def on_leave(data):
    logout_user()
    emit('login', {'authenticated': False})


@socketio.on('join')
def on_join(join):
    if current_user.is_anonymous():
        return

    game = None
    if not pending_games:
        game = Game(current_user)
        pending_games.append(game)
    else:
        game = pending_games[0]
        pending_games.pop(0)
        games.append(pending_games[0])
        game.add_player(current_user)

    join_room(game.id)
    current_user.join_game(game.id)

    emit('join', {'game_id': game.id})


@socketio.on('pick')
def on_pick(pick):
    character_ids = pick['char_ids']
    for game in games:
        if game.id == current_user.game:
            game.user_picks(current_user, character_ids)
            if game.is_ready():
                game_data = {"grid": game.map.grid, "players": list()}
                for i, player in enumerate(game.players):
                    game_data['players'].append(player.username)

                game_data['teams'] = {
                    game.players[0]: [
                        gameplayer.__dict__ for gameplayer in game.team1],
                    game.players[1]: [
                        gameplayer.__dict__ for gameplayer in game.team2],
                }
                game_data['teams'][game.players[0]].pop('game', None)
                game_data['teams'][game.players[1]].pop('game', None)
                emit('start', game_data, room=game.id)


@app.route("/")
def index():
    return render_template('index.html')


@socketio.on('connect')
def on_connect():
    print('connected')
    if current_user.is_authenticated:
        emit('login', {'authenticated': True, 'user': current_user.to_dict()})
    else:
        emit('login', {'authenticated': False})


if __name__ == "__main__":
    login_manager.init_app(app)
    socketio.run(app, host="0.0.0.0")

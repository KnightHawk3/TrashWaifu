from flask import Flask, render_template
from flask_login import current_user, LoginManager, \
    login_user, logout_user
from flask_socketio import SocketIO, emit
from user import User
from game import Game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ayy lmao'
socketio = SocketIO(app)
login_manager = LoginManager()

pending_games = []
games = []
users = []


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
            emit('login', {'authenticated': True,
                           'user': current_user.to_dict()})
            return
    user = User(username)
    users.append(user)
    login_user(user)
    emit('login', {'authenticated': True, 'user': current_user.to_dict()})


@socketio.on('leave')
def on_leave(data):
    logout_user()
    emit('login', {'authenticated': False})


@socketio.on('join')
def on_join(join):
    if current_user.is_anonymous():
        return

    if pending_games == []:
        game = Game(current_user)
        pending_games.append(game)
        game = game.__dict__
        game.pop('map', None)
        for i, player in enumerate(game['players']):
            game['players'][i] = player.username
        print(game)
        emit('join', {'game': game, 'pending': True})
    else:
        pending_games[0].add_player(current_user)
        game = pending_games[0].__dict__
        game.pop('map', None)

        for i, player in enumerate(game['players']):
            if type(game['players'][i]) is str:
                pass
            else:
                game['players'][i] = player.username

        print(game)
        emit('join', {'game': game, 'pending': False})


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
    socketio.run(app)

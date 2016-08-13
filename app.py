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


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@socketio.on('login')
def on_login(data):
    username = data['username']
    login_user(User(username))
    emit('login', {'authenticated': True, 'user': current_user.to_dict()})


@socketio.on('leave')
def on_leave(data):
    logout_user()
    emit('login', {'authenticated': False})


@socketio.on('join')
def on_join(join):
    if pending_games == []:
        game = Game(current_user)
        pending_games.append(game)
        emit('join', {'game': game.__dict__, 'pending': True})
    else:
        pending_games[0].add_player(current_user)
        emit('join', {'game': game.__dict__, 'pending': False})


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

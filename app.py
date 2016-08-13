from flask import Flask, render_template
from flask_login import current_user, LoginManager, \
    login_user, logout_user
from flask_socketio import SocketIO, emit
from user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ayy lmao'
socketio = SocketIO(app)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@socketio.on('login')
def on_login(data):
    username = data['username']
    login_user(User(username))
    emit('login', {'authenticated': True, 'user': current_user})


@socketio.on('leave')
def on_leave(data):
    logout_user()
    emit('login', {'authenticated': False})


@app.route("/")
def index():
    return render_template('index.html')


@socketio.on('connect')
def on_connect():
    print('connected')
    if current_user.is_authenticated:
        emit('login', {'authenticated': True, 'user': current_user})
    else:
        emit('login', {'authenticated': False})

if __name__ == "__main__":
    login_manager.init_app(app)
    socketio.run(app)

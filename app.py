from flask import Flask, render_template, request
from flask_login import current_user
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ayy lmao'
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')


@socketio.on('connect')
def on_connect():
    print('connected')
    emit('login', {'message': False})

if __name__ == "__main__":
    socketio.run(app)

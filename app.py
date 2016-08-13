from flask import Flask, render_template, request
from flask_login import current_user
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ayy lmao'
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')

@socketio.on_error_default
def default_error_handler(e):
    print(request.event["message"]) # "my error event"
    print(request.event["args"])    # (data,)

@socketio.on('connect')
def on_connect(connect):
    if current_user.is_authenticated:
        emit('login', {'message': True})
    else:
        print("testgoku");
        emit('login', {'message': False})

if __name__ == "__main__":
    socketio.run(app)

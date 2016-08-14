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


@socketio.on('update')
def on_update(data):
    player = current_user
    game_ref = None
    player_ref = None
    for game in games + pending_games:
        if game.id == data['game']:
            game_ref = game
    if game_ref is None:
        # ???
        return

    for player in game_ref.players:
        if current_user.username == player:
            player_ref = player

    for waifu in data['move']:
        if player_ref.username == game_ref.players[0]:
            for wif in game_ref.team1:
                if wif.charactertype.name == waifu:
                    wif.try_move((data['move'][waifu][0],
                                  data['move'][waifu][1]))
        if player_ref.username == game_ref.players[1]:
            for wif in game_ref.team2:
                if wif.charactertype.name == waifu:
                    wif.try_move((data['move'][waifu][0],
                                  data['move'][waifu][1]))


@socketio.on('attack')
def on_attack(data):
    game_ref = None
    player_ref = None
    for game in games + pending_games:
        if game.id == data['game']:
            game_ref = game
    if not game_ref:
        return

    for player in game_ref.players:
        if current_user.username == player:
            player_ref = player
    if not player_ref:
        return

    team_index = 1 if game_ref.players.index(current_user.username) == 1 else 0
    our_character = None
    for character in game_ref.get_team(team_index):
        if character.charactertype.name.lower() == str(data['attacked']).lower():
            our_character = character
    if not our_character:
        return

    enemy_team_index = 1 if game_ref.players.index(current_user.username) == 0 else 0
    enemy_character = None
    for character in game_ref.get_team(enemy_team_index):
        if character.charactertype.name.lower() == str(data['attacked']).lower():
            enemy_character = character
    if not enemy_character:
        return

    our_character.attack(enemy_character)


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
    print("Joined " + current_user.username + " " + str(current_user))
    if current_user.is_anonymous():
        return

    game = None
    if not pending_games:
        game = Game(current_user)
        pending_games.append(game)
    else:
        game = pending_games[0]
        games.append(pending_games[0])
        pending_games.pop(0)
        game.add_player(current_user)

    join_room(game.id)
    current_user.join_game(game.id)

    emit('join', {'game_id': game.id})


@socketio.on('pick')
def on_pick(pick):
    character_ids = pick['char_ids']
    for game in pending_games + games:
        if game.id == current_user.game:
            game.user_picks(current_user, character_ids)
            if game.is_ready():
                game.setup()

                game_data = {"grid": game.map.grid, "players": list()}
                for i, player in enumerate(game.players):
                    game_data['players'].append([i, player])

                team1 = list()
                for gameplayer in game.team1:
                    team1.append({"character": gameplayer.charactertype.name, "position": gameplayer.position})

                team2 = list()
                for gameplayer in game.team2:
                    team2.append({"character": gameplayer.charactertype.name, "position": gameplayer.position})

                game_data['teams'] = [
                    team1,
                    team2,
                ]
                print(game_data)
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

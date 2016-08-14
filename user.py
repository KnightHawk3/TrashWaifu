class User:
    def __init__(self, username):
        self.username = username
        self.game = None

    def join_game(self, game):
        self.game = game

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    def to_dict(self):
        return {'username': self.username}

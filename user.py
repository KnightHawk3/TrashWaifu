class User:
    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    @classmethod
    def get_id(self):
        return self.username

    def to_dict(self):
        return {'username': self.get_id()}

import generation
import uuid


class Game:
    def __init__(self, name, player):
        self.name = name
        generate = generation.Generator(30, 20)
        self.map = generate.export_array_grid()
        self.players = [player]
        self.id = uuid.uuid1()

    def add_player(self, player):
        self.players.append(player)

    def setup(self):
        pass


class GamePlayer:
    def __init__(self, player, position):
        self.player = player
        self.position = position

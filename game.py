import generation
import uuid


class Map:
    def __init__(self, generator):
        self.grid = generator.export_array_grid()
        self.generator = generator

    def is_valid_player_spawn(self, x, y):
        pass


class Game:
    def __init__(self, player):
        generate = generation.Generator(30, 20)
        self.map = Map(generate)
        self.players = [player]
        self.id = uuid.uuid1()
        self.pending = True

    def add_player(self, player):
        if self.pending:
            self.players.append(player)
            return True
        else:
            return False

    def setup(self):
        # Find the first team.
        for x in range(self.map.generator.width):
            for y in range(self.map.generator.height):
                if self.map.is_valid_player_spawn(x, y):
                    pass


class GamePlayer:
    def __init__(self, player, position):
        self.player = player
        self.position = position

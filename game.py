import generation
import uuid


class Map:
    def __init__(self, generator):
        self.grid = generator.export_array_grid()
        self.generator = generator

    def is_valid_player_spawn(self, x, y):
        spaces = 0
        for xx in range(5):
            for yy in range(5):
                if self.grid.is_passable(x + xx - 2, y + yy - 2):
                    spaces += 1
        return spaces >= 4

    def is_passable(self, x, y):
        return self.grid[x][y] == 0


class Game:
    def __init__(self, player):
        generate = generation.Generator(27, 14)
        self.map = Map(generate)
        self.players = [player]
        self.id = str(uuid.uuid1())
        self.pending = True

        self.team1 = []
        self.team2 = []

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
                    for xx in range(5):
                        for yy in range(5):
                            if self.map.is_passable(x + xx - 2, y + yy - 2):
                                self.team1.append(GamePlayer(self.players[0], (x + xx - 2, y + yy - 2)))
        # Find the second team.
        for x in reversed(range(self.map.generator.width)):
            for y in reversed(range(self.map.generator.height)):
                if self.map.is_valid_player_spawn(x, y):
                    for xx in range(5):
                        for yy in range(5):
                            if self.map.is_passable(x + xx - 2, y + yy - 2):
                                self.team2.append(GamePlayer(self.players[1], (x + xx - 2, y + yy - 2)))


class GamePlayer:
    def __init__(self, player, position):
        self.player = player
        self.position = position

import generation
import uuid
import json
import character


class Map:
    def __init__(self, generator):
        self.grid = generator.export_array_grid()
        self.generator = generator

    def is_valid_player_spawn(self, x, y):
        spaces = 0
        for xx in range(5):
            for yy in range(5):
                if self.is_passable(x + xx - 2, y + yy - 2):
                    spaces += 1
        return spaces >= 4

    def is_passable(self, x, y):
        if x >= len(self.grid) or y >= len(self.grid[x]):
            return False
        return self.grid[x][y] == 0

    def __repr__(self):
        return json.dumps(self.__dict__)


class Game:
    def __init__(self, player):
        generate = generation.Generator(27, 14)
        self.map = Map(generate)
        self.players = [player]
        self.id = str(uuid.uuid1())
        self.ready_to_start = [False, False]
        self.picks = [[], []]

        self.team1 = []
        self.team2 = []

    def add_player(self, player):
        if len(self.players) < 2:
            self.players.append(player)
            return True
        else:
            return False

    def user_picks(self, player, picks):
        index = self.players.index(player)
        for pick in picks:
            self.picks[index].append(character.characters.get(str(pick).lower()))
        self.picks[index] = picks
        self.ready_to_start[index] = True

    def is_ready(self):
        overall_ready = True
        for ready in self.ready_to_start:
            if not ready:
                overall_ready = False
        return overall_ready

    def setup(self):
        # Find the first team.
        team1_id = 0
        for x in range(self.map.generator.width):
            for y in range(self.map.generator.height):
                if self.map.is_valid_player_spawn(x, y):
                    for xx in range(5):
                        for yy in range(5):
                            if self.map.is_passable(x + xx - 2, y + yy - 2):
                                self.team1.append(GamePlayer(self, self.picks[team1_id],
                                                             self.players[0], (x + xx - 2, y + yy - 2)))
                                team1_id += 1
        team2_id = 0
        # Find the second team.
        for x in reversed(range(self.map.generator.width)):
            for y in reversed(range(self.map.generator.height)):
                if self.map.is_valid_player_spawn(x, y):
                    for xx in range(5):
                        for yy in range(5):
                            if self.map.is_passable(x + xx - 2, y + yy - 2):
                                self.team2.append(GamePlayer(self, self.picks[team2_id],
                                                             self.players[1], (x + xx - 2, y + yy - 2)))
                                team2_id += 1


class GamePlayer:
    def __init__(self, game, charactertype, player, position):
        self.game = game
        self.charactertype = charactertype
        self.player = player
        self.position = position

        # TODO Spawn Player

    def try_move(self, position):
        if self.game.map.is_passable(position[0], position[1]):
            self.position = position

            # TODO Update position

            return True
        return False


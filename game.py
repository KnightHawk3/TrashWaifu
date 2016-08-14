import generation
import uuid
import json


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
                                self.team1.append(GamePlayer(self, self.players[0], (x + xx - 2, y + yy - 2)))
        # Find the second team.
        for x in reversed(range(self.map.generator.width)):
            for y in reversed(range(self.map.generator.height)):
                if self.map.is_valid_player_spawn(x, y):
                    for xx in range(5):
                        for yy in range(5):
                            if self.map.is_passable(x + xx - 2, y + yy - 2):
                                self.team2.append(GamePlayer(self, self.players[1], (x + xx - 2, y + yy - 2)))

    def __repr__(self):
        return json.dumps(self.__dict__)


class GamePlayer:
    def __init__(self, game, player, position):
        self.game = game
        self.player = player
        self.position = position

        # TODO Spawn Player

    def try_move(self, position):
        if self.game.map.is_passable(position[0], position[1]):
            self.position = position

            # TODO Update position

            return True
        return False


class ElementType:

    KUUDERE = ("Kuudere", None)
    YANDERE = ("Yandere", KUUDERE)
    DEREDERE = ("Deredere", YANDERE)
    TSUNDERE = ("Tsundere", DEREDERE)
    OTAKU = ("Otaku", TSUNDERE)

    def __init__(self, name, weakness):
        self.name = name
        self.weakness = weakness
        if weakness == ElementType.TSUNDERE:
            ElementType.KUUDERE.weakness = self


class CharacterType:

    EXCONATA = ("Exconata", 5, 3, ElementType.OTAKU, 1, 5)
    LOISE = ("Loise", 3, 2, ElementType.OTAKU, 5, 2)
    MAYO = ("Mayo", 5, 2, ElementType.TSUNDERE, 1, 7)
    WINERY = ("Winery", 4, 5, ElementType.TSUNDERE, 2, 2)
    BLEAKU = ("Bleaku", 6, 1, ElementType.DEREDERE, 5, 3)
    MOYURI = ("Moyuri", 2, 8, ElementType.DEREDERE, 2, 3)
    RAM = ("RAM", 5, 5, ElementType.KUUDERE, 1, 1)
    RAY = ("Ray", 3, 6, ElementType.KUUDERE, 2, 4)
    DONTNO = ("Dontno", -1, -1, ElementType.YANDERE, 2, 3)
    STABBER = ("Stabber", 7, 1, ElementType.YANDERE, 1, 6)

    def __init__(self, name, attack, defence, element, attack_range, speed):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.element = element
        self.attack_range = attack_range
        self.speed = speed

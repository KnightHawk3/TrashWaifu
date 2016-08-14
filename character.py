class ElementType:
    def __init__(self, name, weakness):
        self.name = name
        self.weakness = weakness
        if weakness == TSUNDERE:
            KUUDERE.weakness = self


KUUDERE = ElementType("Kuudere", None)
YANDERE = ElementType("Yandere", KUUDERE)
DEREDERE = ElementType("Deredere", YANDERE)
TSUNDERE = ElementType("Tsundere", DEREDERE)
OTAKU = ElementType("Otaku", TSUNDERE)


class CharacterType:
    def __init__(self, name, attack, defence, element, attack_range, speed):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.element = element
        self.attack_range = attack_range
        self.speed = speed


EXCONATA = CharacterType("Exconata", 5, 3, OTAKU, 1, 5)
LOISE = CharacterType("Loise", 3, 2, OTAKU, 5, 2)
MAYO = CharacterType("Mayo", 5, 2, TSUNDERE, 1, 7)
WINERY = CharacterType("Winery", 4, 5, TSUNDERE, 2, 2)
BLEAKU = CharacterType("Bleaku", 6, 1, DEREDERE, 5, 3)
MOYURI = CharacterType("Moyuri", 2, 8, DEREDERE, 2, 3)
RAM = CharacterType("RAM", 5, 5, KUUDERE, 1, 1)
RAY = CharacterType("Ray", 3, 6, KUUDERE, 2, 4)
DONTNO = CharacterType("Dontno", -1, -1, YANDERE, 2, 3)
STABBER = CharacterType("Stabber", 7, 1, YANDERE, 1, 6)

characters = {
    "exconata": EXCONATA,
    "loise": LOISE,
    "mayo": MAYO,
    "winery": WINERY,
    "bleaku": BLEAKU,
    "moyuri": MOYURI,
    "ram": RAM,
    "ray": RAY,
    "dontno": DONTNO,
    "stabber": STABBER
}

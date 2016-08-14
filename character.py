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
    def __init__(self, name, attack, defence, element, attack_range, speed):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.element = element
        self.attack_range = attack_range
        self.speed = speed


EXCONATA = CharacterType("Exconata", 5, 3, ElementType.OTAKU, 1, 5)
LOISE = CharacterType("Loise", 3, 2, ElementType.OTAKU, 5, 2)
MAYO = CharacterType("Mayo", 5, 2, ElementType.TSUNDERE, 1, 7)
WINERY = CharacterType("Winery", 4, 5, ElementType.TSUNDERE, 2, 2)
BLEAKU = CharacterType("Bleaku", 6, 1, ElementType.DEREDERE, 5, 3)
MOYURI = CharacterType("Moyuri", 2, 8, ElementType.DEREDERE, 2, 3)
RAM = CharacterType("RAM", 5, 5, ElementType.KUUDERE, 1, 1)
RAY = CharacterType("Ray", 3, 6, ElementType.KUUDERE, 2, 4)
DONTNO = CharacterType("Dontno", -1, -1, ElementType.YANDERE, 2, 3)
STABBER = CharacterType("Stabber", 7, 1, ElementType.YANDERE, 1, 6)

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

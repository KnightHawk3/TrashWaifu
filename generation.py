import random
from math import floor, ceil


class Leaf:
    MIN_LEAF_SIZE = 6

    leftChild = None
    rightChild = None
    room = None
    halls = None

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.has_desks = random.random() > 0.5

    def split(self):
        if self.leftChild or self.rightChild:
            return False

        horizontal_split = random.random() > 0.5
        if self.width > self.height and self.width / self.height >= 1.25:
            horizontal_split = False
        elif self.height > self.width and self.height / self.width >= 1.25:
            horizontal_split = True

        max_size = (self.height if horizontal_split else self.width) - self.MIN_LEAF_SIZE
        if max_size <= self.MIN_LEAF_SIZE:
            return False

        split = random.randrange(self.MIN_LEAF_SIZE, max_size)

        if horizontal_split:
            self.leftChild = Leaf(self.x, self.y, self.width, split)
            self.rightChild = Leaf(self.x, self.y + split, self.width, self.height - split)
        else:
            self.leftChild = Leaf(self.x, self.y, split, self.height)
            self.rightChild = Leaf(self.x + split, self.y, self.width - split, self.height)

        return True

    def has_split(self):
        return self.leftChild or self.rightChild

    def collides(self, x, y):
        if self.x <= x < self.x + self.width:
            if self.y <= y < self.y + self.height:
                return True
        return False

    def is_wall(self, x, y):
        is_edge = self.x == x or self.x + self.width == x or self.y == y or self.y + self.height == y
        dx = x - self.x
        dy = y - self.y
        if self.width > 9:
            if dx == ceil(self.width / 4) or dx == floor(self.width / 4) \
                    or dx == ceil((self.width / 4) * 3) or dx == floor((self.width / 4) * 3):
                return False
        else:
            if dx == ceil(self.width / 2) or dx == floor(self.width / 2):
                return False
        if self.height > 9:
            if dy == ceil(self.height/4) or dy == floor(self.height/4) \
                    or dy == ceil((self.height / 4) * 3) or dy == floor((self.height / 4) * 3):
                return False
        else:
            if dy == ceil(self.height/2) or dy == floor(self.height/2):
                return False
        return is_edge

    def is_desk(self, x, y):
        return self.has_desks and x % 2 == 0 and y % 2 == 0

    def get_lowest_leaves(self, leaves):
        if self.has_split():
            self.leftChild.get_lowest_leaves(leaves)
            self.rightChild.get_lowest_leaves(leaves)
        else:
            leaves.append(self)


class Generator:
    leaves = []

    def __init__(self, width, height, max_leaf_size=20):
        self.max_leaf_size = max_leaf_size
        self.width = width
        self.height = height
        self.leaves.clear()

        self.root_leaf = Leaf(0, 0, self.width, self.height)

        self.leaves.append(self.root_leaf)

        split_hasnt_failed = True
        while split_hasnt_failed:
            split_hasnt_failed = False
            for leaf in self.leaves:
                if not leaf.has_split():
                    if leaf.width > self.max_leaf_size or leaf.height > self.max_leaf_size or random.random() > 0.25:
                        if leaf.split():
                            self.leaves.append(leaf.leftChild)
                            self.leaves.append(leaf.rightChild)
                            split_hasnt_failed = True

    def export_array_grid(self):
        grid = list()
        for x in range(self.width):
            row = list()
            for y in range(self.height):
                low_leaves = list()
                self.root_leaf.get_lowest_leaves(low_leaves)
                for leaf in low_leaves:
                    if leaf.collides(x, y):
                        wall = leaf.is_wall(x, y) or x == 0 or y == 0 or x == self.width-1 or y == self.height-1
                        desk = leaf.is_desk(x, y)
                        data_bit = 0
                        if wall:
                            data_bit = 1
                        elif desk:
                            data_bit = 2
                        row.append(data_bit)
            grid.append(row)
        return grid

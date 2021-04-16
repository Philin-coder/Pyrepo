class AirCastle:
    def __init__(self, height, clouds, color):
        self.height = height
        self.clouds = clouds
        self.color = color


def change_height(self, value):
    self.value = value
    if self.height + self.value < 0:
        return 0
    else:
        return self.height + self.value


def __call__(self, prosp):
    self.prosp = prosp
    return self.height // self.prosp * self.clouds


def __str__(self):
    return f'The AirCastle at an altitude of {self.height} meters is {self.color} with {self.clouds} clouds.'


def __add__(self, number):
    self.clouds += number
    self.height += number // 5
    return self.clouds, self.height


def __gt__(self, other):
    if self.clouds == other.clouds:
        if self.height == other.height:
            return self.color > other.color
        else:
            return self.height > other.height
    else:
        return self.clouds > other.clouds


def __lt__(self, other):
    if self.clouds == other.clouds:
        if self.height == other.height:
            return self.color < other.color
        else:
            return self.height < other.height
    else:
        return self.clouds < other.clouds


def __ge__(self, other):
    if self.clouds == other.clouds:
        if self.height == other.height:
            return self.color >= other.color
        else:
            return self.height >= other.height
    else:
        return self.clouds >= other.clouds


def __le__(self, other):
    if self.clouds == other.clouds:
        if self.height == other.height:
            return self.color <= other.color
        else:
            return self.height <= other.height
    else:
        return self.clouds <= other.clouds


def __eq__(self, other):
    if self.clouds == other.clouds:
        if self.height == other.height:
            return self.color == other.color
        else:
            return self.height == other.height
    else:
        return self.clouds == other.clouds


def __ne__(self, other):
    if self.clouds == other.clouds:
        if self.height == other.height:
            return self.color != other.color
        else:
            return self.height != other.height
    else:
        return self.clouds != other.clouds

class Pawn(object):
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return ('♙', '♟')[self.color]


class Board(object):
    def __init__(self):
        self.board = [['.']*8]*8

    def __repr__(self):
        res=''
        for i in range(8):
            res+=''.join(self.board[i])+"\n"
        return res
    


print(Board())

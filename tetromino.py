from random import randrange

class Tetromino(object):
    def __init__(self, rotations, current, x, y):
        self.rotations = rotations
        self.current = current
        self.x = x
        self.y = y
 
    @staticmethod
    def random():
        p = randrange(0, 7)

        if p == 0:
          return Tetromino.T()
        elif p == 1:
          return Tetromino.J()
        elif p == 2:
          return Tetromino.L()
        elif p == 3:
          return Tetromino.Z()
        elif p == 4:
          return Tetromino.S()
        elif p == 5:
          return Tetromino.Block()
        elif p == 6:
          return Tetromino.Line()

    @staticmethod
    def T():
        return Tetromino(
                rotations=[
                    [
                        [0, 0, 1, 0],
                        [0, 1, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                        ],
                    [
                        [0, 0, 1, 0],
                        [0, 0, 1, 1],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0]
                        ],
                    [
                        [0, 0, 0, 0],
                        [0, 1, 1, 1],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0]
                        ],
                    [
                        [0, 0, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0]
                        ]
                    ],
                current=0,
                x=0,
                y=0
                )

    @staticmethod
    def J():
        return Tetromino(
                rotations=[
                    [
                        [0, 0, 1, 0],
                        [0, 0, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0]
                        ],
                    [
                        [0, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 1, 1],
                        [0, 0, 0, 0]
                        ],
                    [
                        [0, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0]
                        ],
                    [
                        [0, 0, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0]
                        ]
                    ],
                current=0,
                x=0,
                y=0
                )

    @staticmethod
    def L():
        return Tetromino(
                rotations=[[
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 1],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 0, 0],
                    [0, 0, 1, 0],
                    [1, 1, 1, 0],
                    [0, 0, 0, 0]
                    ]],
                current=0,
                x=0,
                y=0
                )


    @staticmethod
    def Z():
        return Tetromino(
                rotations=[[
                    [0, 0, 1, 0],
                    [0, 1, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 0, 0],
                    [1, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 1, 0],
                    [0, 1, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 0, 0],
                    [1, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                    ]], 
                current=0,
                x=0,
                y=0
                )


    @staticmethod
    def S():
        return Tetromino(
                rotations=[[
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [1, 1, 0, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [1, 1, 0, 0],
                    [0, 0, 0, 0]
                    ]], 
                current=0,
                x=0,
                y=0
                )

    @staticmethod
    def Block():
        return Tetromino(
                rotations=[[
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]
                    ]],
                current=0,
                x=0,
                y=0
                )


    @staticmethod
    def Line():
        return Tetromino(
                rotations=[[
                    [0, 0, 0, 1],
                    [0, 0, 0, 1],
                    [0, 0, 0, 1],
                    [0, 0, 0, 1]
                    ],
                [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0]
                    ],
                [
                    [0, 0, 0, 1],
                    [0, 0, 0, 1],
                    [0, 0, 0, 1],
                    [0, 0, 0, 1]
                    ],
                [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0]
                    ]],
                current=0,
                x=0,
                y=0
                )




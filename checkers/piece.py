import pygame
from .constants import RED, WHITE, GREY, SQUARE_SIZE

class Piece:
    PADDING = 10
    OUTLINE = 2


    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        
        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col * SQUARE_SIZE + 0.5*SQUARE_SIZE
        self.y = self.row * SQUARE_SIZE + 0.5*SQUARE_SIZE

    def make_king(self):
        self.king = True

    def draw(self, win):
        RADIUS = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), RADIUS+self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), RADIUS)

    def __repr__(self):
        return str(self.color)


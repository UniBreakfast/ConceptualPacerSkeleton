from cui3toolbox import *
from keychoice import key_choice

class Board:

    def __init__(self, color, width, height, pos_x=1, pos_y=1):
        
        self.color  = color
        self.width  = width
        self.height = height
        
        self.pos_x  = pos_x
        self.pos_y  = pos_y


    def draw(self):

        total_x = self.pos_x+self.width
        total_y = self.pos_y+self.height

        for row in range(self.height):
            curto(self.pos_y+row, self.pos_x)
            if row == self.height-1 and total_y == H and total_x == W:
                print(end=self.color+(self.width-1)*' '+RC)
            else:
                print(end=self.color+self.width*' '+RC)
        curto()

        


    def __call__(self):

        while True:
            self.draw()
            choice = key_choice('Up', 'Down', 'Right', 'Left', 'silent')
            if   choice == 'Up'   : self.pos_y-=1 if self.pos_y>0 else 0
            elif choice == 'Down' : self.pos_y+=1 if self.pos_y<H-self.height else 0
            elif choice == 'Right': self.pos_x+=1 if self.pos_x<W-self.width  else 0
            elif choice == 'Left' : self.pos_x-=1 if self.pos_x>0 else 0
            



board1 = Board(B_DIM_CYAN, 25, 14)
board1()


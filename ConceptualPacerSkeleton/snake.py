import colorama as cr
cr.init()

from msvcrt import getch



UP = '\x1b[1A'
DOWN = '\x1b[1B'
RIGHT = '\x1b[1C'
LEFT = '\x1b[1D'
CLEAR = '\x1b[1J'+'\x1b[0J'

print('@'+LEFT, end='')
while True:
    move = getch()
    if move == b'H':
        print('@'+LEFT+UP, end='@'+LEFT)
    elif move == b'P':
        print('@'+LEFT+DOWN, end='@'+LEFT)
    elif move == b'M':
        print('@'+LEFT+RIGHT, end='@'+LEFT)
    elif move == b'K':
        print('@'+LEFT+LEFT, end='@'+LEFT)
    elif move == b'k':
        quit()
    elif move == b'S':
        print(CLEAR, end='@'+LEFT)










#print(cur_pos(10,10)+'1 line down')
#cur_pos = lambda y, x: '\x1b[%d;%dH' % (y, x)
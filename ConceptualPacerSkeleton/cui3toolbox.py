
W=MAX_WIDTH = 80;     H=MAX_HEIGHT = 50

import colorama; colorama.init()

F_WHITE   = '\x1b[37;1m';  F_DIM_WHITE   = '\x1b[37m';  B_DIM_WHITE   = '\x1b[47m'
F_YELLOW  = '\x1b[33;1m';  F_DIM_YELLOW  = '\x1b[33m';  B_DIM_YELLOW  = '\x1b[43m'
F_GREEN   = '\x1b[32;1m';  F_DIM_GREEN   = '\x1b[32m';  B_DIM_GREEN   = '\x1b[42m'
F_CYAN    = '\x1b[36;1m';  F_DIM_CYAN    = '\x1b[36m';  B_DIM_CYAN    = '\x1b[46m'
F_BLUE    = '\x1b[34;1m';  F_DIM_BLUE    = '\x1b[34m';  B_DIM_BLUE    = '\x1b[44m'
F_MAGENTA = '\x1b[35;1m';  F_DIM_MAGENTA = '\x1b[35m';  B_DIM_MAGENTA = '\x1b[45m'
F_RED     = '\x1b[31;1m';  F_DIM_RED     = '\x1b[31m';  B_DIM_RED     = '\x1b[41m'
F_GREY    = '\x1b[30;1m';  F_BLACK       = '\x1b[30m';  B_BLACK       = '\x1b[40m'

color_dic = {
'\x1b[37;1m' : 'F_WHITE',   '\x1b[37m' : 'F_DIM_WHITE',   '\x1b[47m' : 'B_DIM_WHITE',
'\x1b[33;1m' : 'F_YELLOW',  '\x1b[33m' : 'F_DIM_YELLOW',  '\x1b[43m' : 'B_DIM_YELLOW',
'\x1b[32;1m' : 'F_GREEN',   '\x1b[32m' : 'F_DIM_GREEN',   '\x1b[42m' : 'B_DIM_GREEN',
'\x1b[36;1m' : 'F_CYAN',    '\x1b[36m' : 'F_DIM_CYAN',    '\x1b[46m' : 'B_DIM_CYAN',
'\x1b[34;1m' : 'F_BLUE',    '\x1b[34m' : 'F_DIM_BLUE',    '\x1b[44m' : 'B_DIM_BLUE',
'\x1b[35;1m' : 'F_MAGENTA', '\x1b[35m' : 'F_DIM_MAGENTA', '\x1b[45m' : 'B_DIM_MAGENTA',
'\x1b[31;1m' : 'F_RED',     '\x1b[31m' : 'F_DIM_RED',     '\x1b[41m' : 'B_DIM_RED',
'\x1b[30;1m' : 'F_GREY',    '\x1b[30m' : 'F_BLACK',       '\x1b[40m' : 'B_BLACK'}

RC=RESET_COLORS = '\x1b[40;37;22m'

U=UP = '\x1b[1A';   D=DOWN = '\x1b[1B';   R=RIGHT = '\x1b[1C';   L=LEFT = '\x1b[1D'

def up   (y=1):   print(end='\x1b['+str(y)+'A')
def down (y=1):   print(end='\x1b['+str(y)+'B')
def right(x=1):   print(end='\x1b['+str(x)+'C')
def left (x=1):   print(end='\x1b['+str(x)+'D')
def home (   ):   print(end='\r')

def ups(y=1):
    for i in range(y): up()


def u(y):       return    '\x1b['+str(y)+'A'
def d(y):       return    '\x1b['+str(y)+'B'
def r(x):       return    '\x1b['+str(x)+'C'
def l(x):       return    '\x1b['+str(x)+'D'

def horz(x):
    if   x>0:   print(end='\x1b['+str(    x )+'C')
    elif x<0:   print(end='\x1b['+str(abs(x))+'D')
def vert(y):
    if   y>0:   print(end='\x1b['+str(    y )+'B')
    elif y<0:   print(end='\x1b['+str(abs(y))+'A')

def curto(y=0, x=0):     print(end='\x1b['+str(y+1)+';'+str(x+1)+'H')

end=None
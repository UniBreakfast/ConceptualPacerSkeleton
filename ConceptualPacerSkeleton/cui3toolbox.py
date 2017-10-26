
W=MAX_WIDTH = 80;     H=MAX_HEIGHT = 50

import colorama; colorama.init()

F_WHITE   = '\x1b[37;1m';  F_DIM_WHITE   = '\x1b[37;2m';  B_DIM_WHITE   = '\x1b[47m'
F_YELLOW  = '\x1b[33;1m';  F_DIM_YELLOW  = '\x1b[33;2m';  B_DIM_YELLOW  = '\x1b[43m'
F_GREEN   = '\x1b[32;1m';  F_DIM_GREEN   = '\x1b[32;2m';  B_DIM_GREEN   = '\x1b[42m'
F_CYAN    = '\x1b[36;1m';  F_DIM_CYAN    = '\x1b[36;2m';  B_DIM_CYAN    = '\x1b[46m'
F_BLUE    = '\x1b[34;1m';  F_DIM_BLUE    = '\x1b[34;2m';  B_DIM_BLUE    = '\x1b[44m'
F_MAGENTA = '\x1b[35;1m';  F_DIM_MAGENTA = '\x1b[35;2m';  B_DIM_MAGENTA = '\x1b[45m'
F_RED     = '\x1b[31;1m';  F_DIM_RED     = '\x1b[31;2m';  B_DIM_RED     = '\x1b[41m'
F_GREY    = '\x1b[30;1m';  F_BLACK       = '\x1b[30;2m';  B_BLACK       = '\x1b[40m'

color_dic = {
'\x1b[37;1m' : 'F_WHITE',  '\x1b[37;2m' : 'F_DIM_WHITE',  '\x1b[47m' : 'B_DIM_WHITE',
'\x1b[33;1m' : 'F_YELLOW', '\x1b[33;2m' : 'F_DIM_YELLOW', '\x1b[43m' : 'B_DIM_YELLOW',
'\x1b[32;1m' : 'F_GREEN',  '\x1b[32;2m' : 'F_DIM_GREEN',  '\x1b[42m' : 'B_DIM_GREEN',
'\x1b[36;1m' : 'F_CYAN',   '\x1b[36;2m' : 'F_DIM_CYAN',   '\x1b[46m' : 'B_DIM_CYAN',
'\x1b[34;1m' : 'F_BLUE',   '\x1b[34;2m' : 'F_DIM_BLUE',   '\x1b[44m' : 'B_DIM_BLUE',
'\x1b[35;1m' : 'F_MAGENTA','\x1b[35;2m' : 'F_DIM_MAGENTA','\x1b[45m' : 'B_DIM_MAGENTA',
'\x1b[31;1m' : 'F_RED',    '\x1b[31;2m' : 'F_DIM_RED',    '\x1b[41m' : 'B_DIM_RED',
'\x1b[30;1m' : 'F_GREY',   '\x1b[30;2m' : 'F_BLACK',      '\x1b[40m' : 'B_BLACK'}

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

def blank_chmp(y=H, x=W):
   return [[(None, None, None)]*x for row in range(y)]

def underlay_chmp(y=H, x=W, char='.', b_color=B_BLACK, f_color=F_DIM_WHITE):
    return (((b_color, f_color, char),)*x,)*y

def write_to_chmp(charmap, text, pos_y, pos_x, colors=None):
    if colors:
        for i, char in enumerate(text):
            charmap[pos_y][pos_x+i] = (colors[0], colors[1], char)
    else:
        for i, char in enumerate(text):
            charmap[pos_y][pos_x+i] = (charmap[pos_y][pos_x+i][0], 
                                       charmap[pos_y][pos_x+i][1], char)

def topview_chmp(charmap, underlay):
    topview = blank_chmp()
    for y, row in enumerate(charmap):
        for x, char in enumerate(row):
            if char[2]!=None:  topview[y][x] = char
            else:  topview[y][x] = underlay[y][x]
    return topview

from itertools import chain
def linear_chmp(charmap):
    return list(chain(*charmap))

def disredund_chmp(linear_charmap):
    first_match=True
    for i, char in enumerate(linear_charmap[1:]):
        if first_match:
            if char[0] == linear_charmap[i][0] and char[1] == linear_charmap[i][1]:
                linear_charmap[i+1] = [linear_charmap[i+1][2]]
                first_match=False
                j = i
        else:
            if char[0] == linear_charmap[j][0] and char[1] == linear_charmap[j][1]:
                linear_charmap[i+1] = [linear_charmap[i+1][2]]
            else:
                first_match=True

def show_chmp(linear_charmap):
    char_list=[]
    for char in linear_charmap:
            char_list.append(''.join(char))

    del char_list[-1]
    curto()
    print(end=''.join(char_list))
    curto()


end=None
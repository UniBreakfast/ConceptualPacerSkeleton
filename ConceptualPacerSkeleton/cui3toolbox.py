

import colorama; colorama.init()


WHITE   = '\x1b[37;1m';   SILVER   = '\x1b[37;2m';   _SILVER   = '\x1b[47m'
YELLOW  = '\x1b[33;1m';   OLIVE    = '\x1b[33;2m';   _OLIVE    = '\x1b[43m'
GREEN   = '\x1b[32;1m';   LAUREL   = '\x1b[32;2m';   _LAUREL   = '\x1b[42m'
CYAN    = '\x1b[36;1m';   TEAL     = '\x1b[36;2m';   _TEAL     = '\x1b[46m'
BLUE    = '\x1b[34;1m';   NAVY     = '\x1b[34;2m';   _NAVY     = '\x1b[44m'
MAGENTA = '\x1b[35;1m';   EGGPLANT = '\x1b[35;2m';   _EGGPLANT = '\x1b[45m'
RED     = '\x1b[31;1m';   MAROON   = '\x1b[31;2m';   _MAROON   = '\x1b[41m'
GREY    = '\x1b[30;1m';   BLACK    = '\x1b[30;2m';   _BLACK    = '\x1b[40m'

WT = WHITE  ;  SV = SILVER  ;  _SV = _SILVER
YL = YELLOW ;  OL = OLIVE   ;  _OL = _OLIVE
GN = GREEN  ;  LR = LAUREL  ;  _LR = _LAUREL
CN = CYAN   ;  TL = TEAL    ;  _TL = _TEAL
BL = BLUE   ;  NV = NAVY    ;  _NV = _NAVY
MG = MAGENTA;  EG = EGGPLANT;  _EG = _EGGPLANT
RD = RED    ;  MR = MAROON  ;  _MR = _MAROON
GR = GREY   ;  BK = BLACK   ;  _BK = _BLACK


color_dic = {
'\x1b[37;1m' : 'WHITE',  '\x1b[37;2m' : 'SILVER',  '\x1b[47m' : '_SILVER',
'\x1b[33;1m' : 'YELLOW', '\x1b[33;2m' : 'OLIVE',   '\x1b[43m' : '_OLIVE',
'\x1b[32;1m' : 'GREEN',  '\x1b[32;2m' : 'LAUREL',  '\x1b[42m' : '_LAUREL',
'\x1b[36;1m' : 'CYAN',   '\x1b[36;2m' : 'TEAL',    '\x1b[46m' : '_TEAL',
'\x1b[34;1m' : 'BLUE',   '\x1b[34;2m' : 'NAVY',    '\x1b[44m' : '_NAVY',
'\x1b[35;1m' : 'MAGENTA','\x1b[35;2m' : 'EGGPLANT','\x1b[45m' : '_EGGPLANT',
'\x1b[31;1m' : 'RED',    '\x1b[31;2m' : 'MAROON',  '\x1b[41m' : '_MAROON',
'\x1b[30;1m' : 'GREY',   '\x1b[30;2m' : 'BLACK',   '\x1b[40m' : '_BLACK'   }

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


W=MAX_WIDTH = 80;     H=MAX_HEIGHT = 50

def blank_chmp(y=H, x=W):
   return [[(None, None, None)]*x for row in range(y)]

def underlay_chmp(y=H, x=W, char='.', b_color=B_BLACK, f_color=F_GREY):
    return (((b_color, f_color, char),)*x,)*y

def write_to_chmp(charmap, text, pos_y, pos_x, colors=None):
    if type(text) is str:
        if colors:
            for i, char in enumerate(text):
                charmap[pos_y][pos_x+i] = (colors[0], colors[1], char)
        else:
            for i, char in enumerate(text):
                charmap[pos_y][pos_x+i] = (charmap[pos_y][pos_x+i][0], 
                                           charmap[pos_y][pos_x+i][1], char)
    else:
        for j, line in enumerate(text):
            for i, char in enumerate(line):
                charmap[pos_y+j][pos_x+i] = char

def topview_chmp(charmap, underlay):
    topview = blank_chmp(len(charmap), len(charmap[0]))
    for y, row in enumerate(charmap):
        for x, char in enumerate(row):
            if char[2]!=None:  topview[y][x] = char
            else:  topview[y][x] = underlay[y][x]
    return topview

def crop_chmp(charmap, width=MAX_WIDTH, height=MAX_HEIGHT, 
              position_x=0, position_y=0):
    y_cropped_chmp = charmap[position_y:position_y+height]
    x_cropped_chmp = []
    for line in y_cropped_chmp: x_cropped_chmp.append(line[position_x:position_x+width])
    return x_cropped_chmp

from itertools import chain
def linear_chmp(charmap):
    linear = list(chain(*charmap))
    return linear

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
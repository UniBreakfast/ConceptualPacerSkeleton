
# импортирую функцию для быстрого преобразования
# двухмерной последовательности в одномерную
from itertools import chain


# импортирую свои модули для работы с цветами и позиционирования курсора в консоли
from cui4colors import *
from cui4cursor import *


# 2 константы (и алиасы для них), задающие пропорции окна консоли по умолчанию
H=MAX_HEIGHT = 50;     W=MAX_WIDTH = 80

# альтернатива: пропорции задаёт пользователь перед началом работы с программой
#try: H=MAX_HEIGHT = int(input(' введите целое положительное число, по умолчанию 50\n'
#                              'Высота окна консоли в строках = '))
#except: print('выбор непонятен, взято значение по умолчанию 50')
#try: W=MAX_WIDTH = int(input(' введите целое положительное число, по умолчанию 80\n'
#                             'Ширина окна консоли в символах = '))
#except: print('выбор непонятен, взято значение по умолчанию 80')


# 
class CharMap(list):
    
    def __init__(self, height=MAX_HEIGHT, width=MAX_WIDTH,
                 filler=None, background_color=None, text_color=None, spacing=None,
                 vertical_spacing=0, horizontal_spacing=0, spacing_color=None):
        self.h = height
        self.w = width

        if not (spacing or vertical_spacing or horizontal_spacing): 
            no_spacing = True
        else: 
            no_spacing = False

        if not filler:
            charmap = [[(None, None, None)]*width for row in range(height)]

        elif len(filler)==1 and no_spacing:
            charmap = [[(background_color, text_color, filler)]*width 
                       for row in range(height)]

        elif len(filler)>1 and no_spacing:
            charmap = CharMap(height, width)
            for row in range(height):
                for pattern in range(0, width, len(filler)):
                    charmap.inscribe(filler, row, pattern, 
                                     background_color, text_color, 'crop')

        else: 
            charmap = CharMap(height, width, spacing, background_color, spacing_color)
            for row in range(vertical_spacing, height, vertical_spacing+1):
                for pattern in range(horizontal_spacing, width, len(filler)+
                                     horizontal_spacing):
                    charmap.inscribe(filler, row, pattern, 
                                     background_color, text_color, 'skip')





        list.__init__(self, charmap)


    def inscribe(self, text, position_y=0, position_x=0,
                 background_color=None, text_color=None,
                 exceeds=('crop', 'wrap', 'indent', 'extend', 'fit', 'skip')):
        y=position_y;   b_col=background_color
        x=position_x;   t_col=text_color

        if exceeds == 'fit' and x+len(text) > self.w and len(text) <= self.w:
            x = self.w-len(text)

        elif exceeds == 'skip' and x+len(text) > self.w: return

        elif exceeds == 'extend':
            extended_self = CharMap(self.h, x+len(text))
            extended_self.stamp(self)
            extended_self.inscribe(text, y, x, b_col, text_color)
            self.clear()
            self+=extended_self
            self.w = extended_self.w
            return

        if background_color and text_color:
            for i, char in enumerate(text):
                try:
                    self[y][x+i] = (b_col, t_col, char)
                except:
                    if exceeds == 'crop': break
                    elif exceeds == 'wrap': y+=1; x=0-i
                    elif exceeds == 'indent': y+=1; x=position_x-i
                    self[y][x+i] = (b_col, t_col, char)

        elif background_color:
            for i, char in enumerate(text):
                try:
                    self[y][x+i] = (b_col, self[y][x+i][1], char)
                except:
                    if exceeds == 'crop': break
                    elif exceeds == 'wrap': y+=1; x=0-i
                    elif exceeds == 'indent': y+=1; x=position_x-i
                    self[y][x+i] = (b_col, self[y][x+i][1], char)
                
        elif text_color:
            for i, char in enumerate(text):
                try:
                    self[y][x+i] = (self[y][x+i][0], t_col, char)
                except:
                    if exceeds == 'crop': break
                    elif exceeds == 'wrap': y+=1; x=0-i
                    elif exceeds == 'indent': y+=1; x=position_x-i
                    self[y][x+i] = (self[y][x+i][0], t_col, char)

        else:
            for i, char in enumerate(text):
                try:
                    self[y][x+i] = (self[y][x+i][0], self[y][x+i][1], char)
                except:
                    if exceeds == 'crop': break
                    elif exceeds == 'wrap': y+=1; x=0-i
                    elif exceeds == 'indent': y+=1; x=position_x-i
                    self[y][x+i] = (self[y][x+i][0], self[y][x+i][1], char)


    def stamp(self, charmap, position_y=0, position_x=0,
              exceeds=('crop', 'extend', 'fit', 'skip')):
        y=position_y; x=position_x
        
        if exceeds == 'fit':
            if y+charmap.h > self.h and charmap.h <= self.h:
               y = self.h - charmap.h
            if x+charmap.w > self.w and charmap.w <= self.w:
               x = self.w - charmap.w

        elif exceeds == 'skip' and (y+charmap.h>self.h or x+charmap.w>self.w): return

        elif exceeds == 'extend':
            extended_self = CharMap(y+charmap.h, x+charmap.w)
            extended_self.stamp(self)
            extended_self.stamp(charmap, y, x)
            self.clear()
            self+=extended_self
            self.h = extended_self.h;   self.w = extended_self.w
            return

        for j, line in enumerate(charmap):
            for i, char in enumerate(line):
                try:
                    self[y+j][x+i] = char
                except:
                    if exceeds == 'crop': break
                    raise IndexError('charmap does not fit')


    def crop(self, new_height=None, new_width=None, position_y=0, position_x=0):
        y=position_y;   x=position_x
        
        new_height = new_height if new_height else self.h-y
        new_width  = new_width  if new_width  else self.w-x

        y_cropped_charm = self[y:y+new_height]
        cropped_charm = []
        for line in y_cropped_charm: cropped_charm.append(line[x:x+new_width])
        self.clear()
        self+=cropped_charm
        self.h = len(self);     self.w = len(self[0])


    def show(self, position_y=0, position_x=0, relative=True):
        y=position_y;   x=position_x

        preshow = self
        if y or x:
            preshow = CharMap(y+self.h, x+self.w)
            preshow.stamp(self, y, x)
        
        if preshow.w<W:
            extended_preshow = CharMap(preshow.h, W)
            extended_preshow.stamp(preshow)
            preshow = extended_preshow
        
        if preshow.h<H:
            extended_preshow = CharMap(H, preshow.w)
            extended_preshow.stamp(preshow)
            preshow = extended_preshow

        if preshow.w-W or preshow.h-H: preshow.crop(H, W)

        linear = list(chain(*preshow))
        first_match=True
        for i, char in enumerate(linear[1:]):
            if first_match:
                if char[0] == linear[i][0] and char[1] == linear[i][1]:
                    linear[i+1] = [linear[i+1][2]]
                    first_match=False
                    j = i
            else:
                if char[0] == linear[j][0] and char[1] == linear[j][1]:
                    linear[i+1] = [linear[i+1][2]]
                else:
                    first_match=True
        char_list=[]
        
        right=0; down=0; cur_x=0
        for char in linear:
            
            if char[0] is None:
                if   right<W-1-cur_x: right+=1
                else: down+=1; right=0; cur_x=0
            else: 
                charstring = (d(down)+'\r')*bool(down)+r(right)*bool(right)+''.join(char)
                cur_x = cur_x+right+1
                if cur_x==80: cur_x=0
                right=0; down=0
                char_list.append(charstring)

        if not relative: curto()
        else: print()
        
        print(end=''.join(char_list))
        

    def show_instead(self, position_y=0, position_x=0):
        y=position_y;   x=position_x
        
        preshow = self
        if y or x:
            preshow = CharMap(y+self.h, x+self.w)
            preshow.stamp(self, y, x)
        
        if preshow.w<W:
            extended_preshow = CharMap(preshow.h, W)
            extended_preshow.stamp(preshow)
            preshow = extended_preshow
        
        if preshow.h<H:
            extended_preshow = CharMap(H, preshow.w)
            extended_preshow.stamp(preshow)
            preshow = extended_preshow

        if preshow.w-W or preshow.h-H: preshow.crop(H, W)

        linear = list(chain(*preshow))
        first_match=True
        for i, char in enumerate(linear[1:]):
            if first_match:
                if char[0] == linear[i][0] and char[1] == linear[i][1]:
                    linear[i+1] = [linear[i+1][2]]
                    first_match=False
                    j = i
            else:
                if char[0] == linear[j][0] and char[1] == linear[j][1]:
                    linear[i+1] = [linear[i+1][2]]
                else:
                    first_match=True
        char_list=[]
        first_None=True
        for char in linear:
            charstring = ''.join((cell for cell in char if not cell is None))
            if charstring:
                first_None=True
            elif first_None: 
                charstring = RC+' '
                first_None=False
            else: charstring = ' '
            char_list.append(charstring)
        
        del char_list[-1]
        
        curto()
        print(end=''.join(char_list))
        curto()

    def __call__(self, position_y=0, position_x=0):
        self.show_instead(position_y, position_x)



def charm_transparent(y=H, x=W):
   return [[(None, None, None)]*x for row in range(y)]

def underlay_chmp(y=H, x=W, char='.', b_color=BLACK_, f_color=GREY):
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
        charstring = ''.join((cell for cell in char if not cell is None))
        charstring = charstring if charstring else RC+' '
        char_list.append(charstring)

    del char_list[-1]
    curto()
    print(end=''.join(char_list))
    curto()

####   для тестирования   ##########################################################

if __name__ == '__main__':
    pass

    a = CharMap(20, 23, '1', MR_, RD, '.', 2, 3, GR)
    a()
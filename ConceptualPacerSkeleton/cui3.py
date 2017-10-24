from keychoice   import *
from cui3toolbox import *
from cui3abstracts import *



# Центр, управляющий всем происходящим.
class Control(Disposing, Selecting):
    def __init__(self):
        self.boards = []
        self.layers = [Layer(self)]
        self.viewports = [ViewPort(self)]
        self.curr_vport = 0
        self.key_pool = []
        self.kyy_dic = {}

    def __call__(self):
        self.viewports[self.curr_vport]()


# Двухмерные массивы - символьные карты, слои, на которые выводятся доски.
class Layer:
    def __init__(self, control):
        self.in_view = []
        self.boards = []
        self.control = control



# "Илюминатор", через который пользователь видит часть overlayer-a.
class ViewPort(Movable, Resizable, Disposable, Disposing, Selectable, Selecting):
    def __init__(self, control):
        self.control = control

    def __call__(self):
        overview = blank_charmap()


#Пары цветов - цвет фона и цвет шрифта.
class ColorPair:

    def __init__(self, background, foreground):
        
        self.background = background
        self.foreground = foreground

    def __repr__(self):
        return self.background+self.foreground+ \
    '('+color_dic[self.background]+', '+color_dic[self.foreground]+')'+RESET_COLORS

    def __str__(self):
        return self.background+self.foreground

# Палитры - наборы расцветки по умолчанию для доски и всех её элементов.
class Palette:

    def __init__(self, board_colors           =ColorPair(B_DIM_GREEN,  F_DIM_WHITE),
                       field_colors           =ColorPair(B_BLACK,      F_DIM_WHITE),
                       button_colors          =ColorPair(B_DIM_YELLOW, F_DIM_WHITE),
                       selected_field_colors  =ColorPair(B_DIM_BLUE,   F_WHITE),
                       selected_button_colors =ColorPair(B_DIM_RED,    F_YELLOW)):
        
        if type(board_colors) is ColorPair:
            self.board_colors           = board_colors
        elif type(board_colors) is tuple and len(board_colors) == 2:
            self.board_colors           = ColorPair(*board_colors)
        if type(field_colors) is ColorPair:
            self.field_colors           = field_colors
        elif type(field_colors) is tuple and len(field_colors) == 2:
            self.field_colors           = ColorPair(*field_colors)
        if type(button_colors) is ColorPair:
            self.button_colors          = button_colors
        elif type(button_colors) is tuple and len(button_colors) == 2:
            self.button_colors          = ColorPair(*button_colors)
        if type(selected_field_colors) is ColorPair:
            self.selected_field_colors  = selected_field_colors
        elif type(selected_field_colors) is tuple and len(selected_field_colors) == 2:
            self.selected_field_colors  = ColorPair(*selected_field_colors)
        if type(selected_button_colors) is ColorPair:
            self.selected_button_colors = selected_button_colors
        elif type(selected_button_colors) is tuple and len(selected_button_colors) == 2:
            self.selected_button_colors = ColorPair(*selected_button_colors)



# Доски, на которых расположены смысловые элементы (аналог окон Windows).
class Board:
    def __init__(self, title=None, palette=Palette(), width=None, height=None, pos_x=None, pos_y=None):
        
        self.palette    = palette
        self.w = width
        self.h = height
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.framelines = []
        self.hotkeys    = []
        
        self.selected_item_id   = 1
        self.selectable_id      = 0
        self.key_dic            = {}



    def __repr__(self):
        return '''{board_colors           : %s,
 field_colors           : %s,
 button_colors          : %s,
 selected_field_colors  : %s,
 selected_button_colors : %s}''' \
                   % (repr(self.board_colors),
                      repr(self.field_colors),
                      repr(self.button_colors),
                      repr(self.selected_field_colors),
                      repr(self.selected_button_colors))




# Горячие клавиши
class HotKey:
    pass


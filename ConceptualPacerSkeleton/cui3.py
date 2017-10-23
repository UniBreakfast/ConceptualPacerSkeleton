from keychoice   import *
from cui3toolbox import *



# Центр, управляющий всем происходящим.
class Control:
    def __init__(self):
        self.boards = []
        self.space_w = MAX_WIDTH
        self.space_h = MAX_HEIGHT
        self.layers = [Layer(self)]
        self.viewports = [ViewPort(self)]
        self.key_pool = []
        self.kyy_dic = {}



# Двухмерные массивы - символьные карты, слои, на которые выводятся доски.
class Layer:
    def __init__(self, control):
        self.w = control.space_w
        self.h = control.space_h
        self.in_view = []
        self.boards = []
        self.control = control



# "Илюминатор", через который пользователь видит часть overlayer-a.
class ViewPort:
    def __init__(self, control):
        self.w = control.space_w
        self.h = control.space_h
        self.control = control



# Доски, на которых расположены смысловые элементы (аналог окон Windows).
class Board:
    def __init__(self, title=None, palette=Palette(), width=None, height=None, pos_x=None, pos_y=None):
        
        self.palette    = palette
        self.margins    = Margins(indent, width, height)
        self.transition = transition
        self.hint_at    = hint_at

        self.framelines = []
        self.hotkeys    = []
        
        self.selected_item_id   = 1
        self.last_selectable_id = 0
        self.current_relline    = 0       # relative line number
        self.el_dic             = {}
        self.loc_dic            = {}
        self.key_dic            = {}



# Горячие клавиши
class HotKey:
    pass

C = Control()
print(C.layers[0].h)
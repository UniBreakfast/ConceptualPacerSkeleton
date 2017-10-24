from cui3toolbox import *
from time import time

class SelfAware:

    def genealogy(self):
        selftype = str(type(self))
        r_apo = selftype.rfind("'")
        dot = selftype.rfind(".", 0, r_apo)
        selftype = selftype[dot+1:r_apo]
        types = eval(selftype).mro()
        types_in_strings = []
        for eachtype in types:
            type_in_string = str(eachtype)
            r_apo_pos = type_in_string.rfind("'")
            l_apo_pos = type_in_string.rfind("'", 0, r_apo_pos)
            dot_pos = type_in_string.rfind(".", 0, r_apo_pos)
            if dot_pos>l_apo_pos: 
                types_in_strings.append(type_in_string[dot_pos+1:r_apo_pos])
            else:
                types_in_strings.append(type_in_string[l_apo_pos+1:r_apo_pos])
        if len(types_in_strings)>4:
            types_in_string = ', descendant of ' + ', '.join(types_in_strings[1:-3])
        else:
            types_in_string = ''
        return selftype + types_in_string

class SA(SelfAware):
    
    def about(self):
        print(self.genealogy()+'\n'+str(self))

########################################################################################

class Rectangle(SA):

    def __init__(self, width, height):
        self.w = width
        self.h = height

    def __repr__(self):
        return str((self.w, self.h))

    def __str__(self):
        return 'width: '+str(self.w)+', height: '+str(self.h)

########################################################################################

class Placeable(SA):
    def __init__(self, position_x=0, position_y=0, limit_x=None, limit_y=None):
        self.pos_x = position_x
        self.pos_y = position_y
        self.lim_x = limit_x
        self.lim_y = limit_y


    def __repr__(self):
        if self.lim_x or self.lim_y:
            return str((self.pos_x, self.pos_y)) +'/'+ str((self.lim_x, self.lim_y))
        else:
            return str((self.pos_x, self.pos_y))

    def __str__(self):
        pos_y = str(self.pos_y) + ('/'+str(self.lim_y))*bool(self.lim_y)
        pos_x = str(self.pos_x) + ('/'+str(self.lim_x))*bool(self.lim_x)
        return 'position: row '+pos_y+', column '+pos_x

########################################################################################

class Drawable(Rectangle):
    curr_frame = None
    prev_frame = None

########################################################################################

class Colorable(Drawable):
    def __init__(self, color_back=B_BLACK, color_fore=F_DIM_WHITE):
        self.col_b = color_back
        self.col_f = color_fore

    def __repr__(self):
        return str((color_dic[self.col_b], color_dic[self.col_f]))

    def __str__(self):
        return 'colored: ' +self.col_b+self.col_f+'   Like THIS   '+RESET_COLORS

########################################################################################

class Changeable(SA):
    pass

########################################################################################

class Movable(Drawable, Placeable):
    prev_move = None
    prev_time = None
    turbo_counter = 0
    
    def up(self, step=1):
        if step == 1:
            cur_time = time()
            if self.prev_move == 'u' and cur_time-self.prev_time<3 and self.turbo_counter > 4:
                step = 2
            if self.prev_move == 'u': self.turbo_counter += 1
            else: self.turbo_counter = 0
            self.prev_time = cur_time
            self.last_move = 'u'
        self.pos_y = self.pos_y-step if self.pos_y-step>=0 else 0


    def down(self, step=1):
        last_move = 'd'
        self.pos_y += step

    def right(self, step=1):
        last_move = 'r'
        self.pos_x += step

    def left(self, step=1):
        last_move = 'l'
        self.pos_x -= step

    def home(self):
        pass

    def end(self):
        pass

    def top(self):
        pass

    def bottom(self):
        pass

    def top_r(self):
        pass

    def top_l(self):
        pass

    def bottom_r(self):
        pass

    def bottom_r(self):
        pass

    def move(self, x, y):
        pass

    def move_h(self, x):
        pass

    def move_v(self, y):
        pass


########################################################################################

class Resizable(Drawable, Changeable):
    pass

########################################################################################

class Selectable(SA):
    pass

class Container(SA):
    def __init__(self, storage=None):
        stor = storage if storage else []


class Selecting(Container):
    def __init__(self, storage=None, applicants=None, subordinate=None):
        super().__init__(storage)
        
        self.subs = []
        
        if applicants:
            if storage:
                if type(storage) is list:
                    self.subs = storage + applicants
                else: self.subs = list(storage) + applicants
            else: self.subs = list(aplicants)
        elif storage: 
            self.subs = storage if type(storage) is list else list(storage)
        
        if subordinate and subordinate not in self.subs:
            self.subs.append(subordinate)
        
        self.subor = subordinate
        
        if self.subor: self.selected = self.subs.index(subordinate)
        else: self.subs[0] if self.subs else None


    def select_next(self):
        pass
        


class Commanding(SA):
    pass

class DoubleCommanding(Commanding):
    pass

class Pressable(Selectable, Commanding):
    pass

class KeyCallable(SA):
    pass

class InputTaking(Selectable):
    pass

class Disposable(SA):
    pass

class Disposing(SA):
    pass

class Justifiable(Drawable):
    pass

class Justifying(SA):
    pass




#class PlaRect(Rectangle, Placeable):
#    def __init__(self, width=1, height=1, pos_x=0, pos_y=0):
#        Rectangle.__init__(self, width, height)
#        Placeable.__init__(self, pos_x, pos_y)
    
#    def __repr__(self):
#        return Rectangle.__repr__(self) +'\n'+ Placeable.__repr__(self)

#    def __str__(self):
#        return Rectangle.__str__(self) +'\n'+ Placeable.__str__(self)


#plobj = PlaRect()
#plobj.about()

from cui3toolbox import *
from time import time

class SelfAware:
    def __init__(self, nametag='unnamed abstraction'):
        self.nametag = nametag

    def genealogy(self, theclass):
        selftype = str(type(self))
        r_apo = selftype.rfind("'")
        dot = selftype.rfind(".", 0, r_apo)
        selftype = selftype[dot+1:r_apo]
        
        try: types = theclass.mro() if theclass else eval(selftype).mro()
        except: return selftype + (" of unclear genealogy \n" +
                                   "(retry with its class as a parameter)")
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
    
    def about(self, theclass=None):
        print(self.nametag+'\n'+self.genealogy(theclass)+'\n'+str(self))

########################################################################################

class Rectangle(SA):

    def __init__(self, width=1, height=1, nametag='unnamed'):
        super().__init__(nametag=nametag)
        self.w = width
        self.h = height

    def __repr__(self):
        return str((self.w, self.h))

    def __str__(self):
        return 'width: '+str(self.w)+', height: '+str(self.h)

########################################################################################

class Placeable(SA):
    def __init__(self, location=None, position_x=0, position_y=0, limit_x=None, limit_y=None, nametag='unnamed'):
        super().__init__(nametag=nametag)
        self.pos_x = position_x
        self.pos_y = position_y
        self.loc = location
        if limit_x: self.lim_x = limit_x
        elif location: self.lim_x = location.w
        else: self.lim_x = None
        if limit_y: self.lim_y = limit_y
        elif location: self.lim_y = location.h
        else: self.lim_y = None


    def __repr__(self):
        if self.lim_x or self.lim_y:
            return str((self.pos_x, self.pos_y)) +'/'+ str((self.lim_x, self.lim_y))
        else:
            return str((self.pos_x, self.pos_y))

    def __str__(self):
        pos_y = str(self.pos_y) + ('/'+str(self.lim_y))*bool(self.lim_y)
        pos_x = str(self.pos_x) + ('/'+str(self.lim_x))*bool(self.lim_x)
        at = ' in '+self.loc.nametag if self.loc else ''
        return 'position: row '+pos_y+', column '+pos_x+at

########################################################################################

class Drawable(Rectangle):
    frame = None


########################################################################################

class Colorable(Drawable):
    def __init__(self, color_back=B_BLACK, color_fore=F_DIM_WHITE, nametag='unnamed'):
        super().__init__(nametag=nametag)
        self.col_b = color_back
        self.col_f = color_fore

    def __repr__(self):
        return str((color_dic[self.col_b], color_dic[self.col_f]))

    def __str__(self):
        return 'colored: ' +self.col_b+self.col_f+'   Like THIS   '+RESET_COLORS

########################################################################################

class Changeable(SA):
    changed = False

########################################################################################

class ReDrawable(Drawable, Changeable):
    curr_frame = None
    prev_frame = None


########################################################################################

class Movable(Drawable, Placeable):
    turbo_counter = 0

    def __init__(self, location=None, width=1, height=1, pos_x=0, pos_y=0, nametag='unnamed'):
        Rectangle.__init__(self, width, height, nametag)
        Placeable.__init__(self, location, pos_x, pos_y)

    def report_move(self):
        pass
    
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

    
    
    def __repr__(self):
        return Rectangle.__repr__(self) +'@'+ Placeable.__repr__(self)

    def __str__(self):
        return Rectangle.__str__(self) +'\n'+ Placeable.__str__(self)



########################################################################################

class Resizable(ReDrawable):
    
    def maximize(self):
        pass

    def minimize(self):
        pass

    def change_w(self, step=1):
        pass

    def change_h(self, step=1):
        pass

    def set_size(self, width, height):
        pass

########################################################################################

class Selectable(SA):
    def __init__(self, master=None, nametag='unnamed'):
        super().__init__(nametag)
        self.master = master
        try: self.number_tag = master.subs.index(self) if master else None
        except: 
            if master: 
                master.subs.append(self)
                self.number_tag = master.subs.index(self)
        if master and (master.subor is self or master.selected == self.number_tag):
            self.chosen = True
        else: self.chosen = False

    def __repr__(self):
        if self.chosen: 
            return "chosen by "+self.master.nametag+', has a #'+str(self.number_tag)
        elif self.master: 
            return "neglected by "+self.master.nametag+', #'+str(self.number_tag)
        else: return "stray"

    def __str__(self):
        if self.chosen: 
            return "chosen by "+self.master.nametag+' among '+str(len(self.master.subs))+', has a #'+str(self.number_tag)
        elif self.master: 
            return "neglected by "+self.master.nametag+' among '+str(len(self.master.subs))+', has a #'+str(self.number_tag)
        else: return "stray, without master"
            

########################################################################################

class Container(SA):
    def __init__(self, storage=None, nametag='unnamed'):
        super().__init__(nametag)
        self.stor = storage if storage else []

    def __repr__(self):
        return str(self.stor)

    def __str__(self):
        return 'contains: '+', '.join(self.stor) if self.stor else 'empty container'

########################################################################################

class Selecting(Container):
    def __init__(self, storage=None, applicants=None, subordinate=None, nametag='unnamed'):
        super().__init__(storage, nametag)
        
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
        else: self.selected = 0 if self.subs else None


    def select_next(self):
        pass

    def select_prev(self):
        pass
        

    def __repr__(self):
        if self.subs == self.stor:
            return str(self.selected)+'/'+str(len(self.subs))
        else:
            return str(self.selected)+'/'+str(len(self.subs)) + ', ' + super().__repr__()

    def __str__(self):
        nametext = ' ('+self.subor.nametag+')' if self.subor else ''
        if self.subs is self.stor:
            return '#'*bool(self.selected)+str(self.selected)+nametext+' is selected among '+str(len(self.subs))+' subordinates'
        else:
            return '#'*bool(self.selected)+str(self.selected)+nametext+' is selected among '+str(len(self.subs))+' subordinates' + '\n' + super().__str__()

########################################################################################

class Commanding(SA):
    pass

########################################################################################

class DoubleCommanding(Commanding):
    pass

########################################################################################

class Pressable(Selectable, Commanding):
    pass

########################################################################################

class KeyCallable(SA):
    def __init__(self, key_dictionary=None, nametag='unnamed'):
        super().__init__(nametag)
        self.key_dic = key_dictionary if key_dictionary else {}

    def __call__(self, key=None):
        if key and key in list(self.key_dic): 
            try: self.key_dic[key][0](self.key_dic[key][1])
            except: print('action for '+key+"isn't worth it!")
        else: pass

    def __repr__(self):
        key_strings = []
        for key in self.key_dic.keys():
            key_string = key+': '+self.key_dic[key][2] if len(self.key_dic[key])==3 else key+': unannounced command'
            key_strings.append(key_string)
        return '{'+',\n '.join(key_strings)+'}'

    def __str__(self):
        key_strings = []
        for key in self.key_dic.keys():
            key_string = key+': '+self.key_dic[key][2] if len(self.key_dic[key])==3 else key+': unannounced command'
            key_strings.append(key_string)
        return 'Ready to act on hotkeys:\n'+';\n'.join(key_strings)

########################################################################################

class KeyRelay(KeyCallable):
    def __init__(self, key_dictionary=None, subs_key_dictionary=None, 
                 key_receiver=None, nametag='unnamed'):
        super().__init__(key_dictionary, nametag)
        self.subs_key_dic = subs_key_dictionary if subs_key_dictionary else []
        
        try: self.pipe = self.subor if not self.pipe else key_receiver
        except: self.pipe = key_receiver

    def __call__(self, key=None):
        if key and key in list(self.key_dic): 
            try: self.key_dic[key][0](self.key_dic[key][1])
            except: print('action for '+key+"isn't worth it!")
        elif key and key in self.subs_key_dic: 
            done = self.pipe(key)
            if not done: return False
        else: return False

    def __repr__(self):
        return super().__repr__()+'\n'+str(self.subs_key_dic)

    def __str__(self):
        
        keys = '\n'+super().__str__() if self.key_dic else ''
        if self.subs_key_dic:
            keys += '\nor send deeper keys:\n'+', '.join(self.subs_key_dic)
        return keys

########################################################################################

class InputTaking(Selectable):
    pass

########################################################################################

class Disposable(SA):
    obsolete = False

########################################################################################

class Disposing(SA):
    
    def trash_obs(self):
        pass

########################################################################################

class Justifiable(Drawable):
    pass

########################################################################################

class Justifying(SA):
    pass

########################################################################################




from time import time

from keychoice     import *
from cui3toolbox import *

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
        SA.__init__(self, nametag)
        self.w = width
        self.h = height

    def __repr__(self):
        return str((self.w, self.h))

    def __str__(self):
        return 'width: '+str(self.w)+', height: '+str(self.h)

########################################################################################

class Placeable(SA):
    def __init__(self, location=None, position_x=0, position_y=0, limit_x=None, limit_y=None, nametag='unnamed'):
        SA.__init__(self, nametag)
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
        SA.__init__(self, nametag)
        self.col_b = color_back
        self.col_f = color_fore

    def __repr__(self):
        return str((color_dic[self.col_b], color_dic[self.col_f]))

    def __str__(self):
        return 'colored: ' +self.col_b+self.col_f+'   Like THIS   '+RESET_COLORS

########################################################################################

class Palettable(Drawable):
    def __init__(self, color_back=B_BLACK, color_fore=F_DIM_WHITE, nametag='unnamed'):
        SA.__init__(self, nametag)
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

    def __init__(self, location=None, width=1, height=1, pos_x=0, pos_y=0, 
                 limit_x=None, limit_y=None, nametag='unnamed'):
        Rectangle.__init__(self, width, height, nametag)
        Placeable.__init__(self, location, pos_x, pos_y, limit_x, limit_y, nametag)

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
        SA.__init__(self, nametag)
        self.master = master
        if master and not master.subs:
            master.subs.append(self)
            master.subor = self
            master.selected = 0
            self.chosen = True
        else: self.chosen = False

    def __repr__(self):
        if self.chosen: 
            return ("chosen by "+self.master.nametag+', has a #'+
                    str(self.master.subs.index(self)) )
        elif self.master: 
            return ("neglected by "+self.master.nametag+', #'+
                    str(self.master.subs.index(self)) )
        else: return "stray"

    def __str__(self):
        if self.chosen: 
            return ("chosen by "+self.master.nametag+' among '+
                    str(len(self.master.subs))+', has a #'+
                    str(self.master.subs.index(self)) )
        elif self.master: 
            return ("neglected by "+self.master.nametag+' among '+
                    str(len(self.master.subs))+', has a #'+
                    str(self.master.subs.index(self)) )
        else: return "stray, without master"
            

########################################################################################

class Container(SA):
    def __init__(self, items=None, nametag='unnamed'):
        SA.__init__(self, nametag)
        self.items = items if items else []

    def __repr__(self):
        return str(self.items)

    def __str__(self):
        return 'contains: '+', '.join(self.items) if self.items else 'empty container'

########################################################################################

class Selecting(SA):
    def __init__(self, applicants=None, subordinate=None, nametag='unnamed'):
        SA.__init__(self, nametag)
        
        self.subs = list(aplicants) if applicants else []
        
        if subordinate and subordinate not in self.subs:
            self.subs.append(subordinate)
                
        self.subor = subordinate if subordinate else None
        
        if self.subor: self.selected = self.subs.index(subordinate)
        elif self.subs: self.selected = 0; self.subor = self.subs[0]
        else: self.selected = None
        
            
    def select_next(self):
        pass

    def select_prev(self):
        pass
        
    def __repr__(self):
        if self.subs: return str(self.selected)+'/'+str(len(self.subs))
        else: return ''

    def __str__(self):
        if self.subs: 
            return ('#'+str(self.selected)+' ('+self.subor.nametag+
                    ') is selected among '+str(len(self.subs))+' subordinates')
        else: return ''

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

class KeyCallable(Selectable):
    def __init__(self, master=None, key_dictionary=None, nametag='unnamed'):
        Selectable.__init__(self, master, nametag)
        self.key_dic = key_dictionary if key_dictionary else {}
        
        self.del_keys = []; self.add_keys = []
        self.key_upd = [self.del_keys, self.add_keys]

    def __call__(self, key=None):
        if key and key in list(self.key_dic): 
            try:  self.key_dic[key][0](self.key_dic[key][1])
            except:  print('action for '+key+"isn't worth it!")
            return True, self.key_upd
        else: return False, self.key_upd

    def __repr__(self):
        key_strings = []
        for key in self.key_dic.keys():
            key_string = key+': '+self.key_dic[key][2] if len(self.key_dic[key])==3 else key+': unannounced command'
            key_strings.append(key_string)
        return Selectable.__repr__(self)+', does\n{'+',\n '.join(key_strings)+'}'

    def __str__(self):
        key_strings = []
        if self.key_dic:
            for key in self.key_dic.keys():
                key_string = key+': '+self.key_dic[key][2] if len(self.key_dic[key])==3 else key+': unannounced command'
                key_strings.append(key_string)
        keys = '\nReady to act on hotkeys:\n'+';\n'.join(key_strings) if self.key_dic else ''
        return Selectable.__str__(self)+keys

########################################################################################

class KeyRelay(KeyCallable, Selecting):
    def __init__(self, applicants=None, subordinate=None, 
                 master=None, key_dictionary=None, nametag='unnamed'):
        Selecting.__init__(self, applicants, subordinate)
        KeyCallable.__init__(self, master, key_dictionary, nametag)

        self.subs_keys = []
        
    def __call__(self, key=None):
        if not key: return
        elif key and key in list(self.key_dic):
            done, key_upd = KeyCallable.__call__(self, key)
            if done: return True, key_upd
        elif key and key in self.subs_keys:
            done, key_upd = self.subor(key)
            self.key_upd[0], self.key_upd[1] = list(key_upd[0]), list(key_upd[1])
            if key_upd[0]:
                for del_key in key_upd[0]:
                    while del_key in self.subs_keys: self.subs_keys.remove(del_key)
                key_upd[0].clear()
            if key_upd[1]:
                for add_key in key_upd[1]: self.subs_keys.append(add_key)
                key_upd[1].clear()
            if not done:
                while key in self.subs_keys: self.subs_keys.remove(key)
                return False, key_upd
        else: return False, self.key_upd

    def __repr__(self):
        return (Selecting.__repr__(self)+'\n'*bool(Selecting.__repr__(self))+
                KeyCallable.__repr__(self)+'\n'+str(self.subs_keys) )

    def __str__(self):
        keys = '\n'+KeyCallable.__str__(self)
        if self.subs_keys:
            subs_keys_str = '\n'+'or send deeper keys:\n'+', '.join(self.subs_keys)
        else: subs_keys_str = ''
        return (Selecting.__str__(self)+'\n'*bool(Selecting.__str__(self))+
                KeyCallable.__str__(self)+subs_keys_str)

########################################################################################

class KeySender(KeyRelay):

    def __call__(self):
        key = key_choice(list(self.key_dic)+self.subs_keys)
        KeyRelay.__call__(self, key)


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





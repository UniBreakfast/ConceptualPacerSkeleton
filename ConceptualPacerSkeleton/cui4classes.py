
from cui4charms    import *
from cui4abstracts import *
from cui4keycatch  import *

class Control(Rectangle, SelfAware): 
    def __init__(self, nametag, height, width):
        Rectangle.__init__(self, height, width)
        SelfAware.__init__(self, nametag)
        self.vps = []
        self.avp = None
        self.own_keys = {}
        self.vp_keys = []

    def __call__(self):
        self.vps.append(ViewPort(self))
        self.avp = self.vps[0]
        while True:
            key = catch_key(list(self.own_keys) + self.vp_keys)
            if key in list(self.own_keys):
                function  = self.own_keys[key][0]
                arguments = self.own_keys[key][1]
                function(arguments)
            else: 
                self.vp_keys = self.avp(key)
            self.avp()

class ViewPort():
    def __init__(self, master):
        Rectangle.__init__(self, H, W, master.h//2-H//2, master.w//2-W//2, master)
        self.con = master

    def __call__(self, key=None):
        if key: self.do(key); return list(self.own_keys) + self.brd_keys
        else:   self.show()







class Layer(): pass

class Board(): pass

class Button(): pass

class Field(): pass

class Label(): pass



from dumstick import *

class MenuScr:

    def __init__(self, header=None, items=None, footer=None):
        if items is None: items = []
        self.header = header
        self.footer = footer
        self.items  = items
        self.button_map = {}


    def __call__(self):
        relative_line_num = 1
        if self.header:       dummy('\n     '+self.header);     relative_line_num += 1
        
        first_item = True
        longestKey = 0
        
        self.items.sort(key=lambda item: item.weight)

        for item in self.items:
            if len(item.keystring)+3 > longestKey and item.in_menu:
               longestKey = len(item.keystring)+3
        
        for num, item in enumerate(self.items):
            if item.in_menu:
                if first_item:
                    dummy()
                    if not len(item.keys):
                        dummy(                 ' '*longestKey   + '  '+item.name)
                        item.pos = num;     self.button_map[num]= []
                    elif type(item.keys[-1]) is int:
                        dummy(item.keystring.rjust(longestKey)  + '. '+item.name)
                        item.pos = num
                    else:
                        dummy(item.keystring.rjust(longestKey-1)+' - '+item.name)
                        item.pos = num
                    first_item = False
                else:
                    if not len(item.keys):
                        dummy(                 ' '*longestKey+   '  ' +item.name)
                        item.pos = num
                    elif type(item.keys[-1]) is int:
                        dummy(item.keystring.rjust(longestKey)+  '. ' +item.name)
                        item.pos = num
                    else:
                        dummy(item.keystring.rjust(longestKey-1)+' - '+item.name)
                        item.pos = num
        
        first_item = True
        for item in self.items:
            if item.w_keybox:
                
                if first_item:
                    dummy('', end='\n  ')
                    if not len(item.keys):
                        dummy(                     item.keybox_name, end='')
                    else:
                        dummy(item.keystring+' - '+item.keybox_name, end='')
                    first_item = False
                
                else:
                    if not len(item.keys):
                        dummy('    '+                     item.keybox_name, end='')
                    else:
                        dummy('    '+item.keystring+' - '+item.keybox_name, end='')
        if self.footer:
            dummy('\n\n '+self.footer)



    def append(self, *items):
        for num, item in enumerate([*items]):
            self.items.append(item)



class MenuItem:

    def __init__(self, command, weight, name, keys=None, 
                 in_menu=True, w_keybox=False, keybox_name=None):
        self.name       = name
        self.weight     = weight
        self.function   = command[0]
        self.arguments  = command[1:]
        
        if keys is None:             keys = []
        if type(keys) is list:  self.keys = keys
        else:                   self.keys = [keys]
        
        if len(self.keys): self.keystring = ' / '.join([str(key) for key in self.keys])
        else:              self.keystring = ''
        
        self.w_keybox   = w_keybox
        self.in_menu    = in_menu
        
        if keybox_name:     self.keybox_name = keybox_name
        else:               self.keybox_name = self.name
        


    def __call__(self, *args):
        
        if    len([*args]):                         self.function(*args)
        elif            not self.arguments[0]:      self.function() 
        else:     [*args] = self.arguments;         self.function(*args)



if __name__ == '__main__':

    main_menu_scr   = MenuScr('MyMenu', footer='this is not my first menu')

    menu_item_1     = MenuItem((print, 'a'), 1,  'Do one thing', 1)
    menu_item_2     = MenuItem((print, 'b'), 2,  'Do another thing', [2, 3, 'Backspace'])
    menu_item_load  = MenuItem((print, 'c'), 40, 'Load file', in_menu=True, w_keybox=True)
    menu_item_save  = MenuItem((print, 'd'), 30, 'Save to file', 'F6', True, True)
    menu_item_exit  = MenuItem((print, 'e'), 99, 'Quit program', 'Esc', True, True, 'Exit')
    menu_item_close = MenuItem((quit, None), 999,'Alt+F4', 'Alt+F4', False)

    main_menu_scr.append(menu_item_1, menu_item_2, menu_item_load, menu_item_save, menu_item_exit, menu_item_close)

    main_menu_scr()

    choice = input()

    try:
        choice = int(choice)
    except:
        pass

    for item in main_menu_scr.items:
        if choice in item.keys:
            item()


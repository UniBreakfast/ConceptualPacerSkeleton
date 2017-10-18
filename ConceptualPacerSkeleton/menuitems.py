from dumstick import *
from keychoice import key_choice
import colorama
colorama.init(autoreset=True)

class MenuScr:

    def __init__(self, header=None, items=None, footer=None):
        if items is None: items = []
        self.header = header
        self.footer = footer
        self.items  = items
        self.button_map = {}
        self.selected_item = None
        self.height = 0


    def __call__(self):
        pass;                             relative_line_num  = 0
        if self.header:                   relative_line_num += 2;       dummy('\n     '+self.header)     
        
        first_item = True
        longestKey = 0
        
        self.items.sort(key=lambda item: item.weight)

        for item in self.items:
            if len(item.keystring)+3 > longestKey and item.in_menu:
               longestKey = len(item.keystring)+3
        
        num=0
        for item in self.items:
            if item.in_menu:
                if first_item:
                    dummy()
                    if not len(item.keys):
                        dummy(                 ' '*longestKey   + '  '+item.name)
                    elif type(item.keys[-1]) is int:
                        dummy(item.keystring.rjust(longestKey)  + '. '+item.name)
                    else:
                        dummy(item.keystring.rjust(longestKey-1)+' - '+item.name)
                    first_item = False
                    item.posV = num;       relative_line_num += 2
                    self.button_map[num]=[relative_line_num, 2+longestKey, 2+longestKey+len(item.name)]
                else:
                    if not len(item.keys):
                        dummy(                 ' '*longestKey+   '  ' +item.name)
                    elif type(item.keys[-1]) is int:
                        dummy(item.keystring.rjust(longestKey)+  '. ' +item.name)
                    else:
                        dummy(item.keystring.rjust(longestKey-1)+' - '+item.name)
                    item.posV = num;       relative_line_num += 1
                    self.button_map[num]=[relative_line_num, 2+longestKey, 2+longestKey+len(item.name)]
                num+=1
        first_item = True
        for item in self.items:
            if item.w_keybox:
                if first_item:
                    dummy('', end='\n  ');
                    if not len(item.keys):
                        dummy(                     item.keybox_name, end='')
                    else:
                        dummy(item.keystring+' - '+item.keybox_name, end='')
                    first_item = False;   relative_line_num += 2
                    item.posH = num
                    if not len(item.keystring):
                        self.button_map[num]=[relative_line_num, 
                                              2+len(item.keystring),
                                              2+len(item.keystring) + len(item.name)]
                    else:
                        self.button_map[num]=[relative_line_num, 
                                              5+len(item.keystring),
                                              5+len(item.keystring) + len(item.name)]
                else:
                    if not len(item.keys):
                        dummy('    '+                     item.keybox_name, end='')
                    else:
                        dummy('    '+item.keystring+' - '+item.keybox_name, end='')
                    item.posH = num
                    if not len(item.keystring):
                        self.button_map[num]=[relative_line_num, 
                                          4+len(item.keystring)+self.button_map[num-1][-1],
                                          4+len(item.keystring)+self.button_map[num-1][-1]+len(item.name)]
                    else:
                        self.button_map[num]=[relative_line_num, 
                                          7+len(item.keystring)+self.button_map[num-1][-1],
                                          7+len(item.keystring)+self.button_map[num-1][-1]+len(item.name)]
                num+=1
        if self.footer:
            dummy('\n\n '+self.footer)
            relative_line_num += 2
            self.height = relative_line_num
            self.selected_item = 0
            

    def append(self, *items):
        for num, item in enumerate([*items]):
            self.items.append(item)

    def find_item(self, num):
        for item in self.items:
            if item.pos == num:     return item

    #def move_cursor(self, direction):
    #    line = self.button_map[self.selected_item][0]
    #    column = self.button_map[self.selected_item][1]
    #    if direction == 'Up':
    #        for rec in self.button_map:
    #            if rec[0] == line-1:    

            

                


    #    elif direction == 'Down':
    #        pass
    #    elif direction == 'Left':
    #        pass
    #    elif direction == 'Right':
    #        pass

    def go(self):
        self.selected_item()




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
        
        self.in_menu    = in_menu
        self.w_keybox   = w_keybox
        
        if keybox_name:     self.keybox_name = keybox_name
        else:               self.keybox_name = self.name

        self.posV = None;          self.posH = None



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

    CURSOR_TO = '\x1b[4;22H'
    B_YELLOW_F_BRIGHT = '\x1b[1;43m'
    print(B_YELLOW_F_BRIGHT+ CURSOR_TO+' '+menu_item_1.name+' ')


    choice = key_choice()




    #dummy(main_menu_scr.button_map)

    
    
    
    #choice = input()

    #try:
    #    choice = int(choice)
    #except:
    #    pass

    #for item in main_menu_scr.items:
    #    if choice in item.keys:
    #        item()


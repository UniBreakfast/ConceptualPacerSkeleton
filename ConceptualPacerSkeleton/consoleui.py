from cuielements import *





class Board:

    def __init__(self, title=None, palette=Palette(), 
                 transition='roll', width=None, height=None, indent=None):
        
        self.palette    = palette
        self.margins    = Margins(indent, width, height)
        self.transition = transition
        
        self.framelines = []
        self.hotkeys    = []
        
        self.selected_item_id   = 1
        self.last_selectable_id = 0
        self.current_relline    = 0       # relative line number
        self.loc_dic            = {}
        self.key_dic            = {}

        if title:
            pass

    def give_ids(self):
        self.selectable_ids = id = 0
        for frameline in self.framelines:
            for element in frameline:
                if type(element) in [MenuItem, Button, Field]:
                    id += 1; element.current_id = id;
                    self.last_selectable_id     = id;
        for hotkey in self.hotkeys:
            id += 1; hotkey.current_id = id

    
    def introspection(self):

        marg = self.margins

        for frameline in self.framelines:
            frameline.introspection()

        marg.height = marg.f_height if marg.f_height else len(self.framelines)
        
        marg.longest_item_key  = 0
        marg.longest_item_name = 0
        for frameline in self.framelines:
            if len(frameline) and type(frameline[0]) is MenuItem:
                if len(str(frameline[0].key)) > marg.longest_item_key:
                    marg.longest_item_key = len(str(frameline[0].key))
                if len(frameline[0].nametext) > marg.longest_item_name:
                    marg.longest_item_name = len(frameline[0].nametext)
        

        if marg.f_width: marg.width = marg.f_width  
        else: 
            marg.width = marg.longest_item_key + marg.longest_item_name + 6
            for frameline in self.framelines:
                if frameline.filled > marg.width:
                    marg.width = frameline.filled
            marg.width += 2
        
        if marg.f_indent: marg.indent = marg.f_indent
        else: marg.indent = (80 - marg.width) // 2
        
        marg.axis = marg.indent + (marg.width - (marg.longest_item_key + marg.longest_item_name + 6)) // 2 + marg.longest_item_key + 4
        
        marg.right_border = marg.indent + marg.width


    def draw(self):
        
        marg = self.margins
        pal  = self.palette
        
        bc  = str(pal.board_colors)
        ind = marg.indent
        wi  = marg.width

        move_cursor(-marg.height)

        relline = 0

        for frameline in self.framelines:

            if not len(frameline): 
                print(r(ind)+bc+' '*wi+RESET_COLORS)
                relline += 1
            else:
                if type(frameline[0]) is MenuItem:

                    bc = str(pal.board_colors)

                    h = frameline[0].hint_colors
                    h = str(h) if h else str(pal.board_colors)
                    
                    b = frameline[0].colors
                    b = str(b) if b else str(pal.button_colors)

                    s = frameline[0].selected_colors
                    s = str(s) if s else str(pal.selected_button_colors)

                    cid = frameline[0].current_id
                    sid = self.selected_item_id

                    b = s if cid == sid else b

                    a = marg.axis
                    l = marg.longest_item_key
                    rb= marg.right_border
                    
                    k = frameline[0].key
                    dl= '. ' if type(k) is int else ' -'
                    p = 1 if cid != sid else 0
                    
                    t = ' '+frameline[0].nametext+' '
                    t = ' '+t+' ' if cid == sid else t
                    
                    print(r(ind)+bc+(a-l-4-ind)*' '+h+str(k).rjust(l)+bc+dl+p*' '+b+t+bc+p*' '+S+bc+(rb-a-len(t)+2-2*p)*' '+RESET_COLORS)

                    self.loc_dic[frameline[0].current_id] = [relline, a-2, a+len(frameline[0].nametext)+2]

                    relline += 1
                
                else:

                    if frameline.justify == 'center':
                        ii = (marg.width - frameline.filled) // 2
                    else: ii = 1
                    iv = 0

                    bc  = str(pal.board_colors)
                    print(end=r(marg.indent)+bc+ii*' ')
                    
                    column = marg.indent+ii
                    
                    for element in frameline:

                        if type(element) is Button:
                            
                            b = element.colors
                            b = str(b) if b else str(pal.button_colors)

                            s = element.selected_colors
                            s = str(s) if s else str(pal.selected_button_colors)

                            cid = element.current_id
                            sid = self.selected_item_id

                            b = s if cid == sid else b
                    
                            k = element.key
                            dl = '. ' if type(k) is int else ' '
                            p = 1 if cid != sid else 0
                    
                            t = ' '+str(k)+dl+element.nametext+' '
                            t = ' '+t+' ' if cid == sid else t
                            
                            print(end=bc+(iv)*' '+p*' '+b+t+bc+p*' '+RESET_COLORS)

                            iv = frameline.interval

                            self.loc_dic[element.current_id] = [
                            relline, column, column+len(t)+2*p]
                            column += len(t)+2*p+iv

                        elif type(element) is Label:
                            
                            l = element.colors
                            l = str(l) if l else str(pal.board_colors)

                            t = element.nametext

                            print(end=bc+(iv)*' '+' '+l+t+bc+' '+RESET_COLORS)

                            iv = frameline.interval
                            column += len(t)+2+iv

                        elif type(element) is Field:
                            
                            f = element.colors
                            f = str(f) if f else str(pal.field_colors)

                            s = element.selected_colors
                            s = str(s) if s else str(pal.selected_field_colors)

                            cid = element.current_id
                            sid = self.selected_item_id

                            f = s if cid == sid else f

                            t = element.nametext+' '

                            print(end=bc+(iv)*' '+' '+f+t+bc+' '+RESET_COLORS)

                            iv = frameline.interval

                            self.loc_dic[element.current_id] = [
                            relline, column, column+len(t)+2]
                            column += len(t)+2+iv

                        elif type(element) is Text:
                            
                            l = element.colors
                            l = str(l) if l else str(pal.board_colors)
                    
                    print(bc+(marg.width - frameline.filled-ii)*' '+S)
                    relline += 1

        for i in range(self.margins.height-len(self.framelines)):
            print(r(ind)+bc+' '*wi+RESET_COLORS)
            


    def __call__(self):
        
        self.introspection()

        if self.transition == 'roll':   move_cursor(self.margins.height)
        self.give_ids()        
        
        marg = self.margins
        pal  = self.palette

        #move_cursor(-marg.height)

        #board_col = self.palette.board_colors.background
            
        #dye_rect(board_col, marg.width, marg.height, marg.indent)
            
        self.draw()




    def empty_framelines_append(self, num=1):
        for i in range(num):    self.framelines.append(FrameLine())

    def empty_framelines_insert(self, index, num=1):
        for i in range(num):    self.framelines.insert(index, FrameLine())

    def element_in_frameline_append(self, element, index_f):
        self.framelines[index_f].append(element)

    def element_in_frameline_insert(self, element, index_f, index_e):
        self.framelines[index_f].insert(index_e, element)

    def element_in_frameline_place(self, element, index_f, pos):
        self.framelines[index_f].justify = 'left'
        self.framelines[index_f].append(element)
        el_pos = len(self.framelines[index_f])-1
        self.framelines[index_f].positions[el_pos] = pos
        
    def element_in_frameline_add(self, element, index_f):

        if type(element) is MenuItem:
            if len(self.framelines[index_f]):
                empty_framelines_insert(index_f)
            self.framelines[index_f].append(element)

        elif type(element) in [Button, Label, Field]:
            if self.framelines[index_f].filled + \
               self.framelines[index_f].interval + len(element.width) < \
               self.margins.width:
                self.framelines[index_f].append(element)
            else:
                empty_framelines_insert(index_f+1)
                self.framelines[index_f+1].append(element)

        elif type(element) is HotKey:
            self.hotkeys.append(element)

        elif type(element) is Text:
            pass
        

    def add_element(self, element):
        if not len(self.framelines):
            self.empty_framelines_append()
        if type(element) is MenuItem:
            index_f = 0
            for i, frameline in enumerate(self.framelines):
                if type(frameline[0]) is MenuItem:
                    index_f = i
            if not index_f:
                if len(self.framelines) >= 2 and \
                   type(self.framelines[0]) is Label and \
                   len(self.framelines[0]) == 1:
                    pass
                    #if 

        elif type(element) is Button:
            pass
        elif type(element) is HotKey:
            pass
        elif type(element) is Label:
            pass
        elif type(element) is Field:
            pass
        elif type(element) is Text:
            pass



    def select_next(self):
        if self.selected_item_id < self.last_selectable_id:
           self.selected_item_id += 1
        else: self.selected_item_id = 1
        self.draw()

    def select_prev(self):
        if self.selected_item_id > 1:
           self.selected_item_id -= 1
        else: self.selected_item_id = self.last_selectable_id
        self.draw()


    def select_up(self):
        pass

    def select_down(self):
        pass

    def select_right(self):
        pass

    def select_left(self):
        pass

    






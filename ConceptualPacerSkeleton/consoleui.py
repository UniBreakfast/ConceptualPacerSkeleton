from cuielements import *





class Board:

    def __init__(self, title=None, palette=Palette(), 
                 transition='roll', width=None, height=None, indent=None):
        
        self.palette    = palette
        self.margins    = Margins(indent, width, height)
        self.transition = transition
        
        self.framelines = []
        self.hotkeys    = []
        
        self.selected_item_id = None
        self.current_relline  = 0       # relative line number
        self.key_dictionary   = {}

        if title:
            pass

    
    
    def introspection(self):

        marg = self.margins

        for frameline in self.framelines:
            frameline.introspection()

        marg.height = marg.f_height if marg.f_height else len(self.framelines)
        
        marg.longest_item_key  = 0
        marg.longest_item_name = 0
        for frameline in self.framelines:
            if len(frameline) and type(frameline[0]) is MenuItem:
                if len(frameline[0].key) > marg.longest_item_key:
                    marg.longest_item_key = len(frameline[0].key)
                if len(frameline[0].nametext) > marg.longest_item_name:
                    marg.longest_item_name = len(frameline[0].nametext)
        
        if marg.f_width: marg.width = marg.f_width  
        else: 
            marg.width = marg.longest_item_key + marg.longest_item_name + 4
            for frameline in self.framelines:
                if frameline.filled > marg.width:
                    marg.width = frameline.filled
            marg.width += 2
        
        if marg.f_indent: marg.indent = marg.f_indent
        else: marg.indent = (80 - marg.width) // 2
        
        marg.axis = marg.indent + (marg.width - (marg.longest_item_key + marg.longest_item_name + 3)) // 2 + marg.longest_item_key + 3
        
        marg.right_border = marg.indent + marg.width



    def draw(self):
        
        marg = self.margins
        pal  = self.palette

        move_cursor(-marg.height)
        
        col = self.palette.board_colors.background
            
        if marg.width == 80:
            print(end=col+'\r'+marg.height*marg.width*' ')
        else:
            print(end=marg.indent*' '+col+
                      marg.height*(marg.width*' '+DOWN+
                      marg.width*LEFT))
            
        move_cursor(-marg.height)
        

        for frameline in self.framelines:

            print('@')
            
            if len(frameline):

                if type(frameline[0]) is MenuItem:

                    

                    marg.longest_item_key
                    marg.axis
                    pal.board_colors
                    pal.button_colors
                    pal.selected_button_colors
                    self.selected_item_id
                    
                    frameline[0].colors
                    frameline[0].selected_colors
                    frameline[0].hint_colors
                    frameline[0].key
                    frameline[0].nametext
                    frameline[0].current_id
                    frameline[0].current_location

                    goto_next_line = None

                else:

                    for element in frameline:

                        frameline.justify
                        frameline.filled
                        frameline.interval
                        
                        element.colors
                        element.selected_colors
                        element.key
                        element.nametext
                        element.current_id
                        element.current_location
                        
                        pal.board_colors
                        pal.button_colors
                        pal.selected_button_colors
                        pal.field_colors
                        pal.selected_field_colors
                        self.selected_item_id
                        
                    goto_next_line = None







    def __call__(self):
        
        if self.transition == 'roll':   move_cursor(self.margins.height)

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






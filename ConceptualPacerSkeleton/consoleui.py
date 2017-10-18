import colorama
colorama.init()

F_WHITE   = '\x1b[37;1m';  F_DIM_WHITE   = '\x1b[37m';  B_DIM_WHITE   = '\x1b[47m'
F_YELLOW  = '\x1b[33;1m';  F_DIM_YELLOW  = '\x1b[33m';  B_DIM_YELLOW  = '\x1b[43m'
F_GREEN   = '\x1b[32;1m';  F_DIM_GREEN   = '\x1b[32m';  B_DIM_GREEN   = '\x1b[42m'
F_CYAN    = '\x1b[36;1m';  F_DIM_CYAN    = '\x1b[36m';  B_DIM_CYAN    = '\x1b[46m'
F_BLUE    = '\x1b[34;1m';  F_DIM_BLUE    = '\x1b[34m';  B_DIM_BLUE    = '\x1b[44m'
F_MAGENTA = '\x1b[35;1m';  F_DIM_MAGENTA = '\x1b[35m';  B_DIM_MAGENTA = '\x1b[45m'
F_RED     = '\x1b[31;1m';  F_DIM_RED     = '\x1b[31m';  B_DIM_RED     = '\x1b[41m'
F_GREY    = '\x1b[30;1m';  F_BLACK       = '\x1b[30m';  B_BLACK       = '\x1b[30m'

UP = '\x1b[1A';     DOWN = '\x1b[1B';      RIGHT = '\x1b[1C';     LEFT = '\x1b[1D'

def move_cursor(y=0, x=0):
    if   y > 0:     print(end=DOWN*y)
    elif y < 0:     print(end=UP* -y)
    if   x > 0:     print(end=RIGHT*x)
    elif x < 0:     print(end=LEFT*-x)

def dye_rect(y=1, x=1):
    print((x*' '+x*LEFT+DOWN)*y)



class ColorPair:

    def __init__(self, background, foreground):
        
        self.background = background
        self.foreground = foreground



class Palette:

    def __init__(self, board_colors           =ColorPair(B_DIM_GREEN,  F_DIM_WHITE),
                       field_colors           =ColorPair(B_BLACK,      F_DIM_WHITE),
                       button_colors          =ColorPair(B_DIM_YELLOW, F_BLACK),
                       selected_field_colors  =ColorPair(B_DIM_BLUE,   F_WHITE),
                       selected_button_colors =ColorPair(B_DIM_RED,    F_YELLOW)):
        
        self.board_colors           = board_colors
        self.field_colors           = field_colors
        self.button_colors          = button_colors
        self.selected_field_colors  = selected_field_colors
        self.selected_button_colors = selected_button_colors



class Margins:

    def __init__(self):
        
        self.left_border            = 7
        self.right_border           = 79
        self.axis                   = 35
        self.longest_key_in_column  = 0
        self.longest_name_in_column = 1
        self.height                 = 3
        self.width                  = 60






class Board:

    def __init__(self, title=None, palette=Palette(), transition='roll'):
        
        self.palette    = palette
        self.margins    = Margins()
        self.transition = transition
        
        self.framelines = []
        
        self.selected_item_id = None
        self.current_relline  = 0       # relative line number
        self.key_dictionary   = {}

        if title:
            pass


    def draw(self):
        
        move_cursor(-self.margins.height)
        
        def board(marg, col):
            
            if marg.width == 80:
                print(col+'\r'+marg.height*marg.width*' ')
            else:
                print(marg.left_border*' '+col+
                      marg.height*(marg.width*' '+DOWN+
                      marg.width*LEFT))
            
            move_cursor(-marg.height)
        
        board(self.margins, self.palette.board_colors.background)

        for frameline in self.framelines:

            if len(frameline):





    def __call__(self):
        
        if self.transition == 'roll':   move_cursor(self.margins.height)

        self.draw()




class FrameLine(list):

    def __init__(self, justify='center'):
        
        self.justify = justify






class Element:

    def __init__(self, type, nametext,  invisible=False,  key =None,
                       command     =None,  default_params     =None,
                       alt_command =None,  alt_default_params =None,
                       color       =None,  selected_color     =None):
        
        self.type               = type
        self.nametext           = nametext
        self.invisible          = invisible
        self.key                = key
        self.command            = command
        self.default_params     = default_params
        self.alt_command        = alt_command
        self.alt_default_params = alt_default_params
        self.color              = color
        self.selected_color     = selected_color
        
        self.lastID        = None
        self.last_location = None



class Label(Element):

    def __init__(self, type, nametext):
        super().__init__(type, nametext)



class Button(Element):

    def __init__(self, type, nametext):
        super().__init__(type, nametext)



class MenuItem(Element):

    def __init__(self, type, nametext):
        super().__init__(type, nametext)



class Field(Element):

    def __init__(self, type, nametext):
        super().__init__(type, nametext)



class Text(Element):

    def __init__(self, type, nametext):
        super().__init__(type, nametext)



class HotKey(Element):

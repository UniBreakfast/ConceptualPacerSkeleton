import colorama; colorama.init()

F_WHITE   = '\x1b[37;1m';  F_DIM_WHITE   = '\x1b[37m';  B_DIM_WHITE   = '\x1b[47m'
F_YELLOW  = '\x1b[33;1m';  F_DIM_YELLOW  = '\x1b[33m';  B_DIM_YELLOW  = '\x1b[43m'
F_GREEN   = '\x1b[32;1m';  F_DIM_GREEN   = '\x1b[32m';  B_DIM_GREEN   = '\x1b[42m'
F_CYAN    = '\x1b[36;1m';  F_DIM_CYAN    = '\x1b[36m';  B_DIM_CYAN    = '\x1b[46m'
F_BLUE    = '\x1b[34;1m';  F_DIM_BLUE    = '\x1b[34m';  B_DIM_BLUE    = '\x1b[44m'
F_MAGENTA = '\x1b[35;1m';  F_DIM_MAGENTA = '\x1b[35m';  B_DIM_MAGENTA = '\x1b[45m'
F_RED     = '\x1b[31;1m';  F_DIM_RED     = '\x1b[31m';  B_DIM_RED     = '\x1b[41m'
F_GREY    = '\x1b[30;1m';  F_BLACK       = '\x1b[30m';  B_BLACK       = '\x1b[40m'

color_dic = {
'\x1b[37;1m' : 'F_WHITE',   '\x1b[37m' : 'F_DIM_WHITE',   '\x1b[47m' : 'B_DIM_WHITE',
'\x1b[33;1m' : 'F_YELLOW',  '\x1b[33m' : 'F_DIM_YELLOW',  '\x1b[43m' : 'B_DIM_YELLOW',
'\x1b[32;1m' : 'F_GREEN',   '\x1b[32m' : 'F_DIM_GREEN',   '\x1b[42m' : 'B_DIM_GREEN',
'\x1b[36;1m' : 'F_CYAN',    '\x1b[36m' : 'F_DIM_CYAN',    '\x1b[46m' : 'B_DIM_CYAN',
'\x1b[34;1m' : 'F_BLUE',    '\x1b[34m' : 'F_DIM_BLUE',    '\x1b[44m' : 'B_DIM_BLUE',
'\x1b[35;1m' : 'F_MAGENTA', '\x1b[35m' : 'F_DIM_MAGENTA', '\x1b[45m' : 'B_DIM_MAGENTA',
'\x1b[31;1m' : 'F_RED',     '\x1b[31m' : 'F_DIM_RED',     '\x1b[41m' : 'B_DIM_RED',
'\x1b[30;1m' : 'F_GREY',    '\x1b[30m' : 'F_BLACK',       '\x1b[40m' : 'B_BLACK'}       

RESET_COLORS = '\x1b[40;37;22m'

UP = '\x1b[1A';     DOWN = '\x1b[1B';      RIGHT = '\x1b[1C';     LEFT = '\x1b[1D'

def move_cursor(y=0, x=0):
    if   y > 0:     print(end=DOWN*y)
    elif y < 0:     print(end=UP* -y)
    if   x > 0:     print(end=RIGHT*x)
    elif x < 0:     print(end=LEFT*-x)

def dye_rect(color, x=1, y=1, indent=0):
    print(indent*RIGHT+color+(x*' '+x*LEFT+DOWN)*(y-1)+RESET_COLORS)



class ColorPair:

    def __init__(self, background, foreground):
        
        self.background = background
        self.foreground = foreground

    def __repr__(self):
        return self.background+self.foreground+ \
    '('+color_dic[self.background]+', '+color_dic[self.foreground]+')'+RESET_COLORS

    def __str__(self):
        return self.background+self.foreground


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

    def __repr__(self):
        return '''{board_colors           : %s,
 field_colors           : %s,
 button_colors          : %s,
 selected_field_colors  : %s,
 selected_button_colors : %s}''' \
                   % (repr(self.board_colors),
                      repr(self.field_colors),
                      repr(self.button_colors),
                      repr(self.selected_field_colors),
                      repr(self.selected_button_colors))


class Margins:

    def __init__(self, f_indent=None, f_width=None, f_height=None ):
        
        self.f_indent               = f_indent
        self.f_width                = f_width
        self.f_height               = f_height

        self.indent                 = 10
        self.height                 = 3
        self.width                  = 60
        self.right_border           = 70
        self.axis                   = 23
        self.longest_item_key       = 3
        self.longest_item_name      = 40

    def __repr__(self):
        return '''{f_indent          : %s,
 f_width           : %s,
 f_height          : %s,
 indent            : %s,
 height            : %s,
 width             : %s,
 right_border      : %s,
 axis              : %s,
 longest_item_key  : %s,
 longest_item_name : %s}''' \
                   % (str(self.f_indent),
                      str(self.f_width),
                      str(self.f_height),
                      str(self.indent),
                      str(self.height),
                      str(self.width),
                      str(self.right_border),
                      str(self.axis),
                      str(self.longest_item_key),
                      str(self.longest_item_name))







class FrameLine(list):

    def __init__(self, justify='center', interval=3):
        
        self.justify  = justify
        self.interval = interval
        self.positions = {}

        self.filled = 0

    def introspection(self):

        for element in self:
            if self.filled: self.filled += self.interval
            self.filled   = self.filled +  element.width
        
    def __repr__(self):
        return ', '.join([str(element) for element in self])





class Element:

    def __init__(self, nametext):
        
        self.nametext = nametext

    def __repr__(self):
        return self.nametext


class Label(Element):

    def __init__(self, nametext, colors=None):
        super().__init__(nametext)

        self.colors = colors
        
        self.width = len(nametext)



class Button(Element):

    def __init__(self, nametext, command, default_params, key=None, 
                 alt_command=None, alt_default_params=None, 
                 colors=None, selected_colors=None):
        
        super().__init__(nametext)
        
        self.key                = key
        self.command            = command
        self.default_params     = default_params
        self.alt_command        = alt_command
        self.alt_default_params = alt_default_params
        self.colors             = colors
        self.selected_colors    = selected_colors

        self.current_id       = None
        self.current_location = None

        self.width = (1+len(key) if key else 0) + 1+len(nametext)+1

    def __repr__(self):
        return self.key+' '+self.nametext
        

class MenuItem(Button):

    def __init__(self, nametext, command, default_params, key=None, 
                 alt_command=None, alt_default_params=None, 
                 colors=None, selected_colors=None, hint_colors=None):
        
        super().__init__(nametext, command, default_params, key, 
                         alt_command, alt_default_params, 
                         colors, selected_colors)

        self.hint_colors = hint_colors

        self.current_id       = None
        self.current_location = None
        
        self.width = (len(key)+2 if key else 0) + 1+len(nametext)+1

    def __repr__(self):
        if type(self.key) is int:
            return self.key+'. '+self.nametext
        else:
            return self.key+' - '+self.nametext



class HotKey(Element):

    def __init__(self, nametext, key, command, default_params):
        super().__init__(nametext)
        
        self.key            = key
        self.command        = command
        self.default_params = default_params

        self.current_id = None


class Field(Element):

    def __init__(self, nametext, width=None, key=None, 
                 colors=None, selected_colors=None):
        super().__init__(nametext)
        
        self.key             = key
        self.colors          = colors
        self.selected_colors = selected_colors

        self.width = width    if width    else 1+len(nametext)+2
        
        self.current_id       = None
        self.current_location = None
        

class Text(Element):

    def __init__(self, nametext, width=None, colors=None):
        super().__init__(nametext)
        
        self.colors = colors

        self.width = 0



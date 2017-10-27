from cui3 import *


pacer = Control(nametag='PACER')
def dl(obj): print('\n'.join(dir(obj)))

#KC = KeyCallable({'a': (print, 'alpha', 'print("alpha")'), 'b': (print, 'beta', 'print("beta")'), 'c': (print, 'cozzy')})
#print(KC)

#self.keys = {'Tab': 'ViewPort: Tab', 'Enter': 'ViewPort: Enter', 
#             'Delete': 'ViewPort: Delete'}
#pacer.key_dic = {'Up': (print, 'Control: Up', "print('Control: Up')"), 
#                 'Down': (print, 'Control: Down', "print('Control: Down')"),
#                 'Right': (print, 'Control: Right', "print('Control: Right')"),
#                 'Left': (print, 'Control: Left', "print('Control: Left')")}
#pacer.subs_keys = ['Tab', 'Enter', 'Delete']

#pacer.subor.key_dic = {'Tab': (print, 'ViewPort: Tab', "print('Control: Tab')"), 
#                       'Enter': (print, 'ViewPort: Enter', "print('Control: Enter')"), 
#                       'Delete': (print, 'ViewPort: Delete', "print('Control: Delete')")}

#pacer.subor.curr_frame = blank_chmp()
#underlay = underlay_chmp()
#write_to_chmp(pacer.subor.curr_frame, 'Are we cool?', 5, 10, (B_DIM_RED, F_RED))
#linear = linear_chmp(topview_chmp(pacer.subor.curr_frame, underlay))
#disredund_chmp(linear)
#show_chmp(linear)
#input()
board1 = Board(pacer.subor, limit_x=pacer.subor.w, limit_y=pacer.subor.h,
               nametag='board1')



print(end='========================================'*2)
pacer.about(Control)
print(end='========================================'*2)
print(repr(pacer))
print(end='========================================'*2)
pacer.subor.about(ViewPort)
print(end='========================================'*2)
print(repr(pacer.subor))
print(end='========================================'*2)
pacer.subor.subor.about(Board)
print(end='========================================'*2)
print(repr(pacer.subor.subor))
print(end='========================================'*2)






#dl(pacer.subor)

pacer()
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
pacer.subor.subor = Board(pacer, pacer.subor, (B_DIM_CYAN, F_CYAN), pacer, 
                          20, 10, 2, 1, nametag='board1')
pacer.subor.subs.append(Board(pacer, pacer.subor, (B_DIM_RED, F_CYAN), pacer, 
                        20, 10, 6, 8, nametag='board2'))
pacer.subor.subs.append(Board(pacer, pacer.subor, (B_DIM_GREEN, F_CYAN), pacer, 
                        80, 40, 0, 5, nametag='board3'))

pacer.subs_keys = ['Tab']
pacer.subor.key_dic = {'Tab': (pacer.subor.select_next, None, 
                              "pacer.subor.select_next()")}


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


#pacer.subor.items.append(Layer(pacer.subor, pacer.subor.subor))
#write_to_chmp(pacer.subor.items[0].chmp, '        ', 4, 8, (B_DIM_GREEN, ''))
#write_to_chmp(pacer.subor.items[0].chmp, '        ', 5, 8, (B_DIM_GREEN, ''))
#write_to_chmp(pacer.subor.items[0].chmp, '        ', 6, 8, (B_DIM_GREEN, ''))
#write_to_chmp(pacer.subor.items[0].chmp, '        ', 7, 8, (B_DIM_GREEN, ''))
#write_to_chmp(pacer.subor.items[0].chmp, '        ', 8, 8, (B_DIM_GREEN, ''))
#write_to_chmp(pacer.subor.items[0].chmp, '        ', 9, 8, (B_DIM_GREEN, ''))
#pacer.subor.items.append(Layer(pacer.subor, pacer.subor.subor))
#write_to_chmp(pacer.subor.items[1].chmp, '                  ', 8, 10, (B_DIM_RED, ''))
#write_to_chmp(pacer.subor.items[1].chmp, '                  ', 9, 10, (B_DIM_RED, ''))
#write_to_chmp(pacer.subor.items[1].chmp, '                  ',10, 10, (B_DIM_RED, ''))
#write_to_chmp(pacer.subor.items[1].chmp, '                  ',11, 10, (B_DIM_RED, ''))
#write_to_chmp(pacer.subor.items[1].chmp, '                  ',12, 10, (B_DIM_RED, ''))
#write_to_chmp(pacer.subor.items[1].chmp, '                  ',13, 10, (B_DIM_RED, ''))
#write_to_chmp(pacer.subor.items[1].chmp, '                  ',14, 10, (B_DIM_RED, ''))
#write_to_chmp(pacer.subor.items[1].chmp, '                  ',15, 10, (B_DIM_RED, ''))




#dl(pacer.subor)

pacer()
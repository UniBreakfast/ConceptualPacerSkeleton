from cui3 import *

pacer = Control('PACER')

def dl(obj): print('\n'.join(dir(obj)))

#KC = KeyCallable({'a': (print, 'alpha', 'print("alpha")'), 'b': (print, 'beta', 'print("beta")'), 'c': (print, 'cozzy')})
#print(KC)

#self.keys = {'Tab': 'ViewPort: Tab', 'Enter': 'ViewPort: Enter', 
#             'Delete': 'ViewPort: Delete'}



print(end='========================================'*2)
pacer.about(Control)
print(end='========================================'*2)
print(repr(pacer))
print(end='========================================'*2)
pacer.subor.about(ViewPort)
print(end='========================================'*2)
print(repr(pacer.subor))
print(end='========================================'*2)
#dl(pacer.subor)

pacer()
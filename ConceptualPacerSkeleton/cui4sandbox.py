
from cui4colors  import *
from cui4cursor  import *
from cui4charms  import *
from cui4classes import *


c = Control('Main', H, W)

#c.key_dic['Enter'] = {'f': print, 'arg': 'you pressed Enter'}
c.key_dic['Enter'] = (print, 'you pressed Enter')



c()


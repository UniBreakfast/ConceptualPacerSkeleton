
from a2 import *
import a2

def func_2(v):
    global var1
    #print(var1)
    var1[0] = var1[0] + 5
    print(var1[0])
    
    global var2
    var2 +=20
    print(var2)

    u.name *= 2
    print(u.name)

    global var3
    #print(var3)
    var3 = False

    print(v is u)

    a2.var4 += 'C'
    
    print(var)

    print(user.a)

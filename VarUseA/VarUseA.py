

print("1", end='aaa')


from a2 import *
from a1 import *
import a2
import a1

#var1 = 0


def func_1():
    global var1
    #print(var1)
    global var2
    var1[0] = var2
    var2 +=20
    print(var2)
    a2.var4 += 'U'
    
    a1.var = "WOW"
    #print(a1)
    #print(type(a1))
    #print(dir(a1))



def func_3():
    #func_3.var = 11111111111
     
    def func_4(varFoo=None):
        
        #print(func_3.var)
        #func_3.var *= 2
        #print(func_3.var)

        global var1

        varFoo

        print(func_4.var)
           
        def func_5():
            print(var1[0])
            u.name *= 2
            print(u.name)
            a2.var4 += 'K'
        
        #var1 -= 1
        var1[0] = var1[0] - 1
        
        func_5()

    func_4.varFoo = print("fuck--------------------")
    func_4.var = "FACEPALM"
    func_4()
    #func_4.varFoo
    print(a2.var4)

u.name = 'Vasya'
print(u.name)

v = u

user.a = 'TTTTTTTTTTTTTTTTTTTTTTT'

global var3
#print(var3)
var3 = False

func_1()
func_2(v)
func_3()
print(var4)

from a2 import *
print(var4)

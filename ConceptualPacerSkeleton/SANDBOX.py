#myVariable = 5
#v = 4
#for v in locals():
#  if id(v) == id("myVariable"):
#    print(v, locals()[v])


#Jack = 5
#Konnie = 15
#Alex = 22
#April = 23
#Dove = 8
##v = None
##for v in locals():
##    if '__' not in v and 'v' != v: print(v)


#print(', '.join([l for l in locals() if '__' not in l]))



#class NamedList(list):

#    def __init__(self):
#        self.name = None


#print(type(y))
#x = NamedList()
#x.append(1)
#x.append(2)
#x.name = 'Joe'
#x += [3,4,5]
#x[1].name = 'Doe'
#print(x)
#print(x[1])
#print(x.name)
#print(type(x))





from consoleui import *
from keychoice import *

main_menu = Board(height=12)

item1 = MenuItem('Go to screen 1', print, (), 1)
item2 = MenuItem('Go to screen 2', print, (), 2)
item3 = MenuItem('Go to screen 3', print, (), 3)
item4 = MenuItem('Show something else', print, (), 'End')

button1 = Field('Do it Do it')
button1 = Button('Do it', print, (), 'F5')
button2 = Button('Just do it', print, (), 'Enter')
button3 = Button('Regret about it', print, (), 'Del')
label1 = Field('Input here')
field2 = Field('... also input here')
label3 = Label('And you can just read this')

main_menu.framelines.append(FrameLine())
main_menu.framelines.append(FrameLine())
main_menu.framelines[1].append(item1)
main_menu.framelines.append(FrameLine())
main_menu.framelines[2].append(item2)
main_menu.framelines.append(FrameLine())
main_menu.framelines[3].append(item3)
main_menu.framelines.append(FrameLine())
main_menu.framelines[4].append(item4)
main_menu.framelines.append(FrameLine())
main_menu.framelines.append(FrameLine('left'))
main_menu.framelines[6].append(button1)
main_menu.framelines[6].append(button2)
main_menu.framelines[6].append(button3)
main_menu.framelines[6].append(label1)
main_menu.framelines.append(FrameLine())
main_menu.framelines.append(FrameLine())
main_menu.framelines.append(FrameLine())
main_menu.framelines.append(FrameLine('left'))
main_menu.framelines[8].append(field2)
main_menu.framelines[10].append(label3)


print(main_menu.palette)

#print(main_menu.margins)

#print(main_menu.framelines[0])
#print(main_menu.framelines[1])
#print(main_menu.framelines[2])

main_menu.introspection()

print(main_menu.margins)

main_menu()
while True:
    choice = key_choice('Tab', 'Ctrl+Tab')
    if   choice == 'Tab'     : main_menu.select_next()
    elif choice == 'Ctrl+Tab': main_menu.select_prev()
    print(main_menu.loc_dic)

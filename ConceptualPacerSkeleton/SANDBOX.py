#myVariable = 5

from consoleui import *
#from keychoice import *

def printhere(*args):
    print(*args, end='')

main_menu = Board(height=12)

item1 = MenuItem('Go to screen 1', print, (), 1)
item2 = MenuItem('Go to screen 2', print, (), 2)
item3 = MenuItem('Go to screen 3', print, (), 3)
item4 = MenuItem('Show something else', print, (), 'End')

button1 = Field('Do it Do it')
button1 = Button('Do it', printhere, ('\a', '\a', '\r'), 'F5', printhere, ('Space Bar DETECTED','\r'))
button2 = Button('Just do it', printhere, '\a', 'Enter')
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
main_menu.framelines.append(FrameLine(justify='left'))
main_menu.framelines[6].append(button1)
main_menu.framelines[6].append(button2)
main_menu.framelines[6].append(button3)
main_menu.framelines[6].append(label1)
main_menu.framelines.append(FrameLine())
main_menu.framelines.append(FrameLine())
main_menu.framelines.append(FrameLine())
main_menu.framelines.append(FrameLine(justify='left'))
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

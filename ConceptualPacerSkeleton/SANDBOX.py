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

main_menu = Board(height=10, indent=7)

item1 = MenuItem('Jeronimo', print, (), 'Escape')
button1 = Button('Jeronimo', print, (), 'Escape')
button2 = Button('Jeronimo', print, (), 'Escape')


main_menu.framelines.append(FrameLine())
main_menu.framelines[0].append(item1)

main_menu.framelines.append(FrameLine())
main_menu.framelines.append(FrameLine())
main_menu.framelines[2].append(button1)
main_menu.framelines[2].append(button2)
main_menu.framelines[2].append(button2)

print(main_menu.palette)

print(main_menu.margins)

print(main_menu.framelines[0])
print(main_menu.framelines[1])
print(main_menu.framelines[2])

main_menu.introspection()

print(main_menu.margins)

main_menu()


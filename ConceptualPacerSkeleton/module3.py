class Selectable:
    selector = Selecting()
    chosen = True or False

class Selecting:
    selection = [Selectable(), Selectable(), Selectable()]
    selected = Selectable()


class Item:
    container = Container()

class Container:
    items = [Item(), Item(), Item()]



class KeyRelay:
    subor = KeyCallable()
    master = KeyRelay()

class KeyCallable:
    master = KeyRelay()






class Control(KeyRelay, Container, Selecting):
    subor = ViewPort()
    
    selection = [ViewPort(), ViewPort(), ViewPort()]
    selected = ViewPort()

    container = [Board(), Board(), Board()]



class ViewPort(KeyRelay, Selectable, Selecting, Container):
    master = Control()
    selector = Control()
    chosen = True

    selection = [Board(), Board(), Board()]
    selected = Board()

    items = [Layer(), Layer(), Layer()]



class Board(KeyCallable, Selectable, Item):
    master = ViewPort()
    selector = ViewPort()
    chosen = True

    container = Control()



class Layer(Item):
    container = ViewPort()



'''
для каждой доски
    рендер доски
    рендер слоя
для каждого слоя до последнего не включительно
    сложить слой со следующим
вырезать вьюпорт из овервью
наложить оверлей на вьюпорт

'''
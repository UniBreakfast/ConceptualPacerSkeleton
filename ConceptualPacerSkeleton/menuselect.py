from msvcrt import getch


def menu_selection(*keyboard_items):
    keyboard_items = [*keyboard_items]
    if len(keyboard_items) == 1 and type(keyboard_items[0]) is list:
        keyboard_items = keyboard_items[0]
    keyboard_items_prefixes = [b'\x00']
    meaning = {b'1': 1, b'2': 2, b'3': 3, b'4': 4, b'5': 5, b'6': 6, b'0': 0, 
                b'`': '`', b'+': '+', b'=': '+', "b'\\x00'b'<'": 'F2', "b'\\x00'b'='": 'F3', 
                b'\x13': 'Ctrl+S', b'\x0c': 'Ctrl+L'}
    firstTry = True
    choice = prechoice = None
                
    while choice not in keyboard_items:
                    
        if choice != None:
            if choice in keyboard_items_prefixes:
                prechoice = choice
            elif prechoice:
                temp = str(prechoice)+str(choice)
                if str(prechoice)+str(choice) in meaning and meaning[str(prechoice)+str(choice)] in keyboard_items:
                    return meaning[str(prechoice)+str(choice)]
                else:
                    prechoice = None
                    print('... такой вариант не предлагается, будьте внимательны...')
                    firstTry = False
            elif choice in meaning and meaning[choice] in keyboard_items:
                return meaning[choice]
            elif firstTry:
                print('... такой вариант не предлагается, будьте внимательны...')
                firstTry = False
                    
        choice = getch()

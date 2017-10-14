from msvcrt import getch


def menu_selection(*keyboard_items):
    keyboard_items = [*keyboard_items]
    if len(keyboard_items) == 1 and type(keyboard_items[0]) is list:
        keyboard_items = keyboard_items[0]
    keyboard_items_prefixes = [b'\x00']
    meaning = {b'1': 1, b'2': 2, b'3': 3, b'4': 4, b'5': 5, 
               b'6': 6, b'7': 7, b'8': 8, b'9': 9, b'0': 0, 
               b'`': '`', b'\xf1': '`', b'~': '`', b'\xf0': '`', b'\x1b': '`', 
               b'+': '+', b'=': '+', "b'\\x00'b'<'": 'F2', "b'\\x00'b'='": 'F3', 
               b'\x13': 'Ctrl+S', b'\x0c': 'Ctrl+L', "b'\\x00'b'k'": 'Alt+F4',
               b'\r': 'Enter', b'\x08': 'Backspace'}
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
                elif meaning[str(prechoice)+str(choice)] == 'Alt+F4': quit()
                else:
                    prechoice = None
                    print('... такой вариант не предлагается, будьте внимательны...')
                    firstTry = False
            elif choice in meaning and meaning[choice] in keyboard_items:
                return meaning[choice]
            elif firstTry:
                if 'silent' != keyboard_items[-1]:
                    print('... такой вариант не предлагается, будьте внимательны...')
                firstTry = False
                    
        choice = getch()


def long_list_selection(*value_items):
    value_items = [*value_items]
    if len(value_items) == 1 and type(value_items[0]) is list:
        value_items = value_items[0]
    tens = {}
    for i in value_items:
        if type(i) is int and len(str(i))==2:
            if int(str(i)[0]) not in tens:
                tens[(int(str(i)[0]))] = [int(str(i)[1])]
            else:
                tens[(int(str(i)[0]))].append(int(str(i)[1]))
    if len(tens) > 0:
        for i in value_items:
            if type(i) is int and len(str(i))==1:
                if 0 not in tens:
                    tens[0] = [int(str(i))]
                else:
                    tens[0].append(int(str(i)))
        firstdigits = tens[0]
        digits = list(range(10))
        lastdigits = tens[len(tens)-1]
        nondigits = [i for i in value_items if type(i) is not int]
    
    if tens=={}:
        return menu_selection(value_items)
    else:
        while True:
            choice = menu_selection([0]+firstdigits+nondigits)
            if choice in tens:
                prechoice = choice
                print(prechoice, end='\r')
                choice = menu_selection(tens[prechoice]+['`', 'Backspace', 'Enter', 'silent'])
                if choice in ['`', 'Backspace']:
                    print('\r ', end='\r')
                    continue
                elif choice == 'Enter':
                    if prechoice == 0:
                        print('\r ', end='\r')
                        continue
                    else:
                        return prechoice
                elif prechoice == 0:
                    return choice
                else:
                    return int(str(prechoice)+str(choice))
            else:
                return choice
                    


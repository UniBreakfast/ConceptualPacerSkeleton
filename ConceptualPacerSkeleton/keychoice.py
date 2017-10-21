from msvcrt import getch


def key_choice(*keyboard_items):
    keyboard_items = [*keyboard_items]
    if len(keyboard_items) == 1 and type(keyboard_items[0]) is list:
        keyboard_items = keyboard_items[0]
    keyboard_items_prefixes = [b'\x00', b'\xe0']
    meaning = {b'1': 1, b'2': 2, b'3': 3, b'4': 4, b'5': 5, 
               b'6': 6, b'7': 7, b'8': 8, b'9': 9, b'0': 0, 
               b'`': '`', b'~': '~', b'\xf0': '`', b'\x1b': 'Esc', 
               b'+': '+', b'=': '=', b' ': 'Space',
               "b'\\x00'b'<'": 'F2', "b'\\x00'b'='": 'F3', 
               "b'\\x00'b'@'": 'F6', "b'\\x00'b'A'": 'F7', "b'\\x00'b'B'": 'F8',
               b'\x13': 'Ctrl+S', b'\x0c': 'Ctrl+L', "b'\\x00'b'k'": 'Alt+F4',
               b'\r': 'Enter', b'\x08': 'Backspace', "b'\\xe0'b'S'": 'Delete',
               b'q': 'q', b'w': 'w', b'e': 'e', b'r': 'r', b't': 't', b'y': 'y', 
               b'u': 'u', b'i': 'i', b'o': 'o', b'p': 'p', b'[': '[', b']': ']', 
               b'a': 'a', b's': 's', b'd': 'd', b'f': 'f', b'g': 'g', b'h': 'h', 
               b'j': 'j', b'k': 'k', b'l': 'l', b';': ';', b"'": "'", b'z': 'z', 
               b'x': 'x', b'c': 'c', b'v': 'v', b'b': 'b', b'n': 'n', b'm': 'm', 
               b',': ',', b'.': '.', b'/': '/', b'Q': 'Q', b'W': 'W', 
               b'E': 'E', b'R': 'R', b'T': 'T', b'Y': 'Y', b'U': 'U', b'I': 'I', 
               b'O': 'O', b'P': 'P', b'{': '{', b'}': '}', b'A': 'A', b'S': 'S', 
               b'D': 'D', b'F': 'F', b'G': 'G', b'H': 'H', b'J': 'J', b'K': 'K', 
               b'L': 'L', b':': ':', b'"': '"', b'Z': 'Z', b'X': 'X', b'C': 'C', 
               b'V': 'V', b'B': 'B', b'N': 'N', b'M': 'M', b'<': '<', b'>': '>', 
               b'?': '?', b'-': '-', b'\\': '\\', b'@': '@', b'#': '#', b'$': '$', 
               b'%': '%', b'^': '^', b'&': '&', b'*': '*', b'(': '(', b')': ')', 
               b'_': '_', b'|': '|', b'\xf1': 'ё', b'\xa9': 'й', b'\xe6': 'ц', 
               b'\xe3': 'у', b'\xaa': 'к', b'\xa5': 'е', b'\xad': 'н', b'\xa3': 'г',
               b'\xe8': 'ш', b'\xe9': 'щ', b'\xa7': 'з', b'\xe5': 'х', b'\xea': 'ъ', 
               b'\xe4': 'ф', b'\xeb': 'ы', b'\xa2': 'в', b'\xa0': 'а', b'\xaf': 'п', 
               b'\t': 'Tab', "b'\\x00'b'\\x94'": 'Ctrl+Tab', "b'\\xe0'b'P'": 'Down',
               "b'\\xe0'b'H'": 'Up', "b'\\xe0'b'K'": 'Left', "b'\\xe0'b'M'": 'Right'}
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
                elif str(prechoice)+str(choice) in meaning and meaning[str(prechoice)+str(choice)] == 'Alt+F4': quit()
                else:
                    prechoice = None
                    if 'silent' != keyboard_items[-1]:
                        print(end='... такой вариант не предлагается, будьте внимательны...\r')
                    firstTry = False
            elif choice in meaning and meaning[choice] in keyboard_items:
                return meaning[choice]
            elif firstTry:
                if 'silent' != keyboard_items[-1]:
                    print(end='... такой вариант не предлагается, будьте внимательны...\r')
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
        return key_choice(value_items)
    else:
        while True:
            choice = key_choice([0]+firstdigits+nondigits)
            if choice in tens:
                prechoice = choice
                print('', end='\r'+str(prechoice))
                choice = key_choice(tens[prechoice]+['`', 'Backspace', 'Enter', 'silent'])
                if choice in ['`', 'Backspace']:
                    print('\r ', end='\r')
                    continue
                elif choice == 'Enter':
                    if prechoice == 0:
                        print('\r ', end='\r')
                        continue
                    else:
                        print('\r ', end='\r')
                        return prechoice
                elif prechoice == 0:
                    print('\r ', end='\r')
                    return choice
                else:
                    print('\r ', end='\r')
                    return int(str(prechoice)+str(choice))
            else:
                return choice
                    


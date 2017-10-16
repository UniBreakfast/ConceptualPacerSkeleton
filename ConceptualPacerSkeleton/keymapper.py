from msvcrt import getch
from msvcrt import getwch

#print('string')
#print('string', end='\n')
#print('string', end='')
#print('Press a key: ', end='')
while True:

    code_dic = {}
    double = False
    while True:
        if not double:
            print('', end="\n Нажми следующую кнопку или комбинацию:  ")
        key = getwch()
        if key in [b'\x00', b'\xe0'] and not double:
            double = True
            prechoice = key
            continue
        elif double:
            double = False
            code = '"'+str(prechoice)+str(key)+'"'
            print(code)
        elif key == b'`':
            print('...\n Как скажешь, хватит так хватит. Итого в словаре у нас:\n',code_dic, '\n')
            print('\n'+'_'*80)
            break
        else:
            code = key
            print(code)

        if code not in code_dic:

            key_name = input(" Как бы ты записал эту комбинацию?  ")


            double = False
            for i in [1,2]:
                if not double:
                    print('', end="\n Повтори кнопку или комбинацию - перепроверим:  ")
                key = getwch()
                if key in [b'\x00', b'\xe0'] and not double:
                    double = True
                    prechoice = key
                    continue
                elif double:
                    double = False
                    code2 = '"'+str(prechoice)+str(key)+'"'
                else:
                    code2 = key
                print(code2)
                if code2 == code:
                    print('', end="\n Да, повторил так же. Значит, так и запишем:  "+str(code2)+'  =  '+ key_name)
                    code_dic[code] = key_name
                    print('\n'+'_'*80)
                    break
                else:
                    print('', end="Ты что-то путаешь, первый раз ты нажимал:  "+str(code))
                    print('\n'+'_'*80)
                    break

        else:
            print(" Такое ты уже нажимал и называл:  %s  =  %s" % (code, code_dic[code]))
            print('\n'+'_'*80)
from time import sleep

from consoleui import *
from dumstick import *
from saveload import *
from keychoice import *
from pacerclasses import *
import dataglobe as u


def main():
    while True:
        identify_user()
        work_with_user()
        user_logout()
        
        dummy('''
        (Pacer returns to identifying process)
        ''')
        sleepif(1)
        

def identify_user():
    
    login_pal = Palette((B_DIM_MAGENTA, F_DIM_WHITE),
                        (B_BLACK,       F_DIM_RED),
                        (B_DIM_BLUE,    F_DIM_WHITE),
                        (B_DIM_RED,     F_YELLOW),
                        (B_DIM_CYAN,    F_WHITE))
    down(10)
    login_brd = Board("Авторизация пользователя", login_pal)
    login_brd.empty_framelines_append(8, 'left')
    login_brd.framelines[4].append(Label("Логин:"))
    login_brd.framelines[5].append(Field('',35))
    login_brd.framelines[6].append(Label("Пароль:"))
    login_brd.framelines[7].append(Field('',35))
    login_brd.framelines[9].justify='center'

    new_user_but = Button('Новый пользователь', print, ())
    exit_but = Button('Выход', quit, (), 'Esc')
    login_brd.elements_in_frameline_append((new_user_but, exit_but), 9)

    login_brd()
    print(login_brd.framelines[7][0].current_location)
    
    dummy('''
    Hello!
    Please SELECT user, introduce yourself by LOGIN or REGISTER new user.
    (user makes his choice and succesfully logges in)
    ''')
    sleepif(1)
    u.name = 'KnownUser2'
    u.storage = 'User2Data.bin'


def work_with_user():
    
    def prepare_to_work_with():
        dummy('''
    (Pacer is preparing to work with current user...)
        ''')
        sleepif(1)
        
        if not storage_exists():
            def create_storage():
                dummy('... for now with default values.')
                
                save_userdata()
            
            dummy('creates userdata_storage...')
            create_storage()
        
        load_userdata()
        
    prepare_to_work_with()

    dummy('''
    (Pacer prepared to work with current user, his data loaded)
    ''')
    sleepif(1)

    #propositions
    def generate_propositions():
        dummy("checking for certain conditions...")

    def show_propositions():
        dummy("... no special conditions met, so no propositions shown")

    generate_propositions()
    show_propositions()
        
    dummy('''
    (user sucessfully uses Pacer to his advantage and joy)
    ''')
    sleepif(1)

    def interactions_of_choice():
        
        while True:

            def work_with_endeavors():
                
                def edit_endeavor(num):
                    num-=1
                    print('''
 {}
                    
    ~ / Esc - Назад       F2 / Enter - Изменить       F8 / Delete - Удалить'''.format(u.endeavors[num]))
                    choice = None
                    while choice in [None, 'Enter', 'F2']:
                        choice = key_choice('Enter', 'F2', 'Esc', '`', 'F8', 'Delete')
                        if choice in ['Enter', 'F2']:
                            dummy(" начнём редактировать это стремление")

                    if choice in ['F8', 'Delete']:
                        dummy(" это стремление удалено")
                        del u.endeavors[num]
                    elif choice in ['Esc', '`']:
                        pass
                
                while True:

                    print("\nНакоплено стремлений: %s" % len(u.endeavors))
                    num_padding = len(str(len(u.endeavors)+1))
                    name_padding = 0
                    for num, endeavor in enumerate(u.endeavors):
                        if len(endeavor.full_name) > name_padding:
                            name_padding = len(endeavor.full_name)
                    for num, endeavor in enumerate(u.endeavors):
                        print('',str(num+1).rjust(num_padding),'', endeavor.full_name.ljust(name_padding), ' с', endeavor.create_date)
                    
                    num_list = list(range(1, len(u.endeavors)+1))
                    choice = long_list_selection(num_list+['`', 'Esc', '+'])
                
                    if choice in num_list:
                        print('откроется пункт', str(choice))
                        edit_endeavor(choice)

                    elif choice == '+':
                        dummy('добавим новый пункт')
                    elif choice == '`':
                        break
                
                for i in range(37):
                    u.endeavors.append(Endeavor("Муляж", "Мул", "Ненастоящее стремление.", "гирька", today()))
                #u.endeavors.append(Endeavor("Выучить английский язык", "Англ", "Знание английского языка откроет передо мною большие возможности по обучению и трудоустройству.", "навык", today(), ["Учиться в Duolingo", "Смотреть фильмы без перевода"]))
                #u.endeavors.append(Endeavor("Разбогатеть", "Богат", "Богатство позволит мне обеспечить родных и близких всем необходимым и желанным", "задача", today(), ["Преподавать йогу"]))
                #new_endeavor()
                #edit_endeavor()
                #del_endeavor()


            def work_with_activities():
                dummy("ok, you chose 2")
            def work_with_quests():
                dummy("ok, you chose 3")
            def work_with_selfesteem():
                dummy("ok, you chose 4")
            def work_with_stats():
                dummy("ok, you chose 5")
            def work_with_report():
                dummy("ok, you chose 6")

            print('''
        1. Стремления
        2. Действия
        3. Квесты
        4. Вера В Себя
        5. Статистика
        6. Отчитаться    F6 / Ctrl+S - Сохранить изменения
    ~ / 0. Выйти         F7 / Ctrl+L - Отменить несохранённые изменения
                  ''')

            choice = None
            while choice in ['F6', 'F7', 'Ctrl+S', 'Ctrl+L', None]:
                choice = key_choice(1, 2, 3, 4, 5, 6, 0, '`', 'Esc', 'F6', 'F7', 'Ctrl+S', 'Ctrl+L')
                
                if choice in ['F6', 'Ctrl+S']:
                    save_userdata()
                elif choice in ['F7', 'Ctrl+L']:
                    load_userdata()
                
            if choice == 1:
                work_with_endeavors()
            elif choice == 2:
                work_with_activities()
            elif choice == 3:
                work_with_quests()
            elif choice == 4:
                work_with_selfesteem()
            elif choice == 5:
                work_with_stats()
            elif choice == 6:
                work_with_report()
            elif choice in [0, '`', 'Esc']:
                dummy("ok, you chose to exit")
                break



    interactions_of_choice()


def user_logout():
    dummy('''
    (user decides to log out and to give place for another user)
    ''')
    sleepif(1)



main()
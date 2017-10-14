from time import sleep

from dumstick import *
from saveload import *
from menuselect import *
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
    (user sucessfully uses Pacer to his avantage and joy)
    ''')
    sleepif(1)

    def interactions_of_choice():
        
        while True:

            def work_with_endeavors():
                
                while True:

                    print("\nНакоплено стремлений: %s" % len(u.endeavors))
                    num_padding = len(str(len(u.endeavors)+1))
                    name_padding = 0
                    for num, endeavor in enumerate(u.endeavors):
                        if len(endeavor.full_name) > name_padding:
                            name_padding = len(endeavor.full_name)
                    for num, endeavor in enumerate(u.endeavors):
                        print('',str(num+1).rjust(num_padding),'', endeavor.full_name.ljust(name_padding), ' с', endeavor.create_date)

                    choice = None
                    numberlist = [1, 2, 3]; tens = []
                    while choice in [None]:
                        choice = menu_selection(numberlist + [0, '`', '+'])
                
                    if choice == 1:
                        edit_endeavor(0)
                    elif choice == 2:
                        edit_endeavor(1)
                    elif choice == 3:
                        edit_endeavor(2)
                    elif choice in [0, '`']:
                        break

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
        6. Отчитаться    F2 / Ctrl+S - Сохранить изменения
    ~ / 0. Выйти         F3 / Ctrl+L - Отменить несохранённые изменения
                  ''')

            choice = None
            while choice in ['F2', 'F3', 'Ctrl+S', 'Ctrl+L', None]:
                choice = menu_selection(1, 2, 3, 4, 5, 6, 0, '`', 'F2', 'F3', 'Ctrl+S', 'Ctrl+L')
                
                if choice in ['F2', 'Ctrl+S']:
                    save_userdata()
                elif choice in ['F3', 'Ctrl+L']:
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
            elif choice in [0, '`']:
                dummy("ok, you chose to exit")
                break



    interactions_of_choice()


def user_logout():
    dummy('''
    (user decides to log out and to give place for another user)
    ''')
    sleepif(1)



main()
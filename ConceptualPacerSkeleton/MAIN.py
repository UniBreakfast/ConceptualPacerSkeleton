from time import sleep
from msvcrt import getch

from dumstick import *
from saveload import *


def main():
    while True:
        username, userdata_storage = identify_user()
        work_with_user(username, userdata_storage)
        user_logout()
        
        dummy('''
        (Pacer returns to identifying process)
        ''')
        sleep(2)
        

def identify_user():
    dummy('''
    Hello!
    Please SELECT user, introduce yourself by LOGIN or REGISTER new user.
    (user makes his choice and succesfully logges in)
    ''')
    sleep(3)
    username = 'KnownUser2'
    userdata_storage = 'User2Data.bin'
    return username, userdata_storage


def work_with_user(username, userdata_storage):
    

    def prepare_to_work_with(username, userdata_storage):
        dummy('''
    (Pacer is preparing to work with current user...)
        ''')
        sleep(2)
        
        if not storage_exists(userdata_storage):
            def create_storage(username, userdata_storage):
                dummy('... for now with default values.')
                endeavors_of_the_user = ['Стремление1', 'Стремление2', 'Стремление3']
                activities_of_the_user = []
                quests_of_the_user = []
                selfesteem_of_the_user = 9001
                userdata = [username, endeavors_of_the_user, activities_of_the_user, 
                            quests_of_the_user, selfesteem_of_the_user]
                save_userdata(userdata, userdata_storage)
            
            dummy('creates userdata_storage...')
            create_storage(username, userdata_storage)
        
        userdata = load_userdata(userdata_storage)
        return userdata
    
    username, user_endeavors, user_activities, user_quests, user_selfesteem = prepare_to_work_with(username, userdata_storage)

    dummy('''
    (Pacer prepared to work with current user, his data loaded)
    ''')
    sleep(2)

    
    def generate_propositions():
        dummy("checking for certain conditions...")

    def show_propositions():
        dummy("... no special conditions met, so no propositions shown")

    generate_propositions()
    show_propositions()
        
    dummy('''
    (user sucessfully uses Pacer to his avantage and joy)
    ''')
    sleep(2)

    def interactions_of_choice():
        
        while True:

            def work_with_endeavors():
                dummy(user_endeavors)
                new_endeavor()
                edit_endeavor()
                del_endeavor()





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


            def menu_selection(keyboard_items):
                keyboard_items_prefixes = []
                meanings = {}
                firstTry = True
                choice = prechoice = None
                
                while choice not in keyboard_items:
                    
                    if choice != None:
                        if choice in keyboard_items_prefixes:
                            prechoice = choice
                        elif prechoice:
                            if meaning[str(prechoice)+str(choice)] in keyboard_items:
                                return meanings[str(prechoice)+str(choice)]
                            else:
                                prechoice = None
                                firstTry = False
                        elif meaning[choice] in keyboard_items:
                            return meaning[choice]
                        elif firstTry:
                            print('... такой вариант не предлагается, будьте внимательны...')
                            firstTry = False
                    
                    choice = getch()


            print('''
        1. Стремления
        2. Действия
        3. Квесты
        4. Вера В Себя
        5. Статистика
        6. Отчитаться      F2 - Сохранить изменения
  ~ или 0. Выйти           F3 - Отменить несохранённые изменения
              ''')

            choice = subchoice = None; firstTry = True
            while choice not in [b'1', b'2', b'3', b'4', b'5', b'6', b'0', b'`']:
                if not choice == None:
                    if choice == b'\x00':
                        subchoice = b'\x00'
                    elif choice == b'<' and subchoice == b'\x00':
                        save_userdata([username, user_endeavors, user_activities, user_quests, user_selfesteem], userdata_storage)
                    elif choice == b'=' and subchoice == b'\x00':
                        load_userdata(userdata_storage)
                    elif firstTry:
                        dummy("incorrect choice, try again")
                        firstTry = False
                        subchoice = None
                choice = getch()

            if choice == b'1':
                work_with_endeavors()
            elif choice == b'2':
                work_with_activities()
            elif choice == b'3':
                work_with_quests()
            elif choice == b'4':
                work_with_selfesteem()
            elif choice == b'5':
                work_with_stats()
            elif choice == b'6':
                work_with_report()
            elif choice in [b'0', b'`']:
                dummy("ok, you chose to exit")
                break



    interactions_of_choice()


def user_logout():
    dummy('\f')
    dummy('''
    (user decides to log out and to give place for another user)
    ''')
    sleep(2)



main()
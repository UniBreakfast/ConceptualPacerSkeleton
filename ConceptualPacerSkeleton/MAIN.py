from time import sleep


def main():
    while True:
        identify_user()
        prepare_to_work_with_this_particular_user()
        work_with_user()
        user_logout()
        
        print('''
        (Pacer returns to identifying process)
        ''')
        sleep(2)
        


def identify_user():
    print('''
    Hello!
    Please SELECT user, introduce yourself by LOGIN or REGISTER new user.
    (user makes his choice and succesfully logges in)
    ''')
    sleep(3)


def prepare_to_work_with_this_particular_user():
    print('''
    (Pacer sucessfully READS existant user_file or CREATES a new one)
    ''')
    sleep(2)


def work_with_user():
    print('''
    (user sucessfully uses Pacer to his avantage and joy)
    ''')
    sleep(7)


def user_logout():
    print('''
    (user decides to log out and to give place for another user)
    ''')
    sleep(2)


main()
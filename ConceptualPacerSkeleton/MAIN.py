from time import sleep


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
    
    def storage_exists(userdata_storage):
        try:
            with open(userdata_storage) as temp:
                flag = True
        except FileNotFoundError:
            flag = False
        return flag
    
    def what_storagetype(userdata_storage):
        if userdata_storage.endswith('.bin'):
            type ='bin-file'
        elif userdata_storage.endswith('.txt'):
            type ='txt-file'
        return type
    
    def load_userdata(userdata_storage):
        
        def load_DB(userdata_storage):
            pass
        
        def load_file_txt(userdata_storage):
            userdata = []
            return userdata

        def load_file_pickle(userdata_storage):
            import pickle
            with open(userdata_storage, 'rb') as pickle_file:
                userdata = pickle.load(pickle_file)
            return userdata

        def load_cloud(userdata_storage):
            pass

        if what_storagetype(userdata_storage) == 'bin-file':
            userdata = load_file_pickle(userdata_storage)

        return userdata

    def save_userdata(userdata, userdata_storage):
        
        def save_file_pickle(userdata, userdata_storage):
            import pickle
            with open(userdata_storage, 'wb') as pickle_file:
                pickle.dump(userdata, pickle_file)

        if what_storagetype(userdata_storage) == 'bin-file':
            save_file_pickle(userdata, userdata_storage)
    
    def prepare_to_work_with(username, userdata_storage):
        dummy('''
    (Pacer sucessfully READS existent user_file or CREATES a new one)
        ''')
        sleep(2)
        
        if not storage_exists(userdata_storage):
            def create_storage(username, userdata_storage):
                endeavors_of_the_user = ['Стремление1', 'Стремление2', 'Стремление3']
                activities_of_the_user = []
                quests_of_the_user = []
                selfesteem_of_the_user = 9001
                userdata = [username, endeavors_of_the_user, activities_of_the_user, 
                            quests_of_the_user, selfesteem_of_the_user]
                save_userdata(userdata, userdata_storage)
            create_storage(username, userdata_storage)
        
        userdata = load_userdata(userdata_storage)
        return userdata
    
    userdata = prepare_to_work_with(username, userdata_storage)

    dummy('''
    (user sucessfully uses Pacer to his avantage and joy)
    ''')
    sleep(7)


def user_logout():
    dummy('''
    (user decides to log out and to give place for another user)
    ''')
    sleep(2)


# This is just a dummy-function instead of using print with text, 
# wich will not be needed anymore when app is further developed.
def dummy(text):
    print(text)
    return

# This is just a dummy-function instead of using input with text, 
# wich will not be needed anymore when app is further developed.
def stick(text):
    hit = input(text)
    return hit



main()
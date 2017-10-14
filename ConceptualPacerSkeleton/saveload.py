from dumstick import *
import dataglobe as u



def storage_exists():
    dummy('checks if userdata_storage exists...')
    if what_storagetype() in ['bin-file', 'txt-file']:
        try:
            with open(u.storage) as temp:
                dummy('... it does.')
                return True
        except FileNotFoundError:
            dummy('... it does not.')
            return False


def what_storagetype():
    if u.storage.endswith('.bin'):
        type ='bin-file'
    elif u.storage.endswith('.txt'):
        type ='txt-file'
    return type


def load_userdata():
        
    def load_DB():
        pass
        
    def load_file_txt():
        pass

    def load_file_pickle():
        import pickle
        with open(u.storage, 'rb') as pickle_file:
            u.name, u.endeavors, u.activities, u.quests, u.selfesteem = pickle.load(pickle_file)
        dummy('loads userdata from binary userdata-file...')

    def load_cloud():
        pass

    if what_storagetype() == 'bin-file':
        load_file_pickle()



def save_userdata():
        
    def save_file_pickle():
        import pickle
        with open(u.storage, 'wb') as pickle_file:
            pickle.dump([u.name, u.endeavors, u.activities, u.quests, u.selfesteem], pickle_file)
        dummy('saves binary userdata-file.')

    if what_storagetype() == 'bin-file':
        save_file_pickle()


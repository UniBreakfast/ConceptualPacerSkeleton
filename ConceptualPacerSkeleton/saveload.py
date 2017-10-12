from dumstick import *



def storage_exists(userdata_storage):
    dummy('checks if userdata_storage exists...')
    if what_storagetype(userdata_storage) in ['bin-file', 'txt-file']:
        try:
            with open(userdata_storage) as temp:
                flag = True
                dummy('... it does.')
        except FileNotFoundError:
            flag = False
            dummy('... it does not.')
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
        dummy('loads userdata from binary userdata-file...')
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
        dummy('saves binary userdata-file.')

    if what_storagetype(userdata_storage) == 'bin-file':
        save_file_pickle(userdata, userdata_storage)


import pyodbc as db
import os

class DictObject:
    def __init__(self, data):
        self.__dict__ = data

def db_connect():
    c = configure()
    print(c)
    connection_string = f'''
        DRIVER={c.driver};
        SERVER={c.server};
        DATABASE={c.database};
        ENCRYPT={c.encrypt};
        TRUSTED_CONNECTION={c.trusted_connection};
    '''
    # print(connection_string)
    return db.connect(connection_string)

def print_dir(obj):
    for x in dir(obj):
        if not x.startswith('__'):
            print(x)

def configure(path='.env'):
    env_dict = {}
    try:
        with open(path, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    print(line,'ln')
                    key, value = line.strip().split('=')
                    os.environ[key.strip()] = value.strip()
                    env_dict[key.strip()] = value.strip()
            print(env_dict)
            return DictObject(env_dict)
    except FileNotFoundError:
        print('File does not exist')
    except Exception as e:
        print(e)
    
def print_data(data):
    if len(data)>0:
        for key in data[0]:
            print(key,end='\t')
        
        print()
        for row in data:
            for key in row:
                print(row[key],end='\t')
        print()
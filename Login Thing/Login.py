import ast
from zipfile import ZipFile


class login:
    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd

userIn = input('Enter Username ')
passwdIn = input('Enter Password ')

user_1 = login(userIn, passwdIn)

def zipCreator():
    lock = input('Would you like to create a zip file? Y or N?')
    if lock == 'Y':
        filePath = input('Where do you want it? (ex C:\Users\Josh\Desktop\zipfile) ') + '.zip'
        with ZipFile(filePath, 'w') as zipObj:
           # password = input('What password do you want on it')
            #files = input('What file names would you like to add into it? ')

def searchUsers(input):
    with open('users', 'r') as f:
        dict = ast.literal_eval(f.read())
        if dict.get(input) == passwdIn:
            return True
    return False


def login():
    if  searchUsers(user_1.user) == True:
        print('welcome')
        zipCreator()
    else:
        print('Incorrect login')
        print('Would you like to create an account?')
        ans = input('Y or N? ')
        if ans == 'Y':
            new_user = input('New Username: ')
            new_passwd = input('New password: ')
            with open('users', 'r') as f:
                content = f.read()
            with open('users', 'w') as f:
                f.write(str(content[:-1]) + ",'" + new_user +"':'" + new_passwd + "'}")
            return login()
        elif ans == 'N':
           exit()
        else:
            print('Unrecognized input')
            login()
login()



# zip file password

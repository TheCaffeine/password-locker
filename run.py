import getpass
import random
import string

from credential import Credential
from user import User


def create_credential(account_name, key: object):
    """
    the function that creates a new credential
    """
    new_credential = Credential(account_name, key)
    return new_credential

def save_credential(credential):
    """
    A function that saves a new credential created
    """
    credential.save_credential()

def display_credentials():
    """
    A function that displays user credentials
    """
    return  Credential.display_credentials()

def erase_credential(credential):
    """
    A function to delete a credential
    """
    credential.erase_credential()

def check_if_user_exists(password):
    """
    A function that checks if the user exists for authentification
    """
    return User.user_exists(password)


# noinspection PyUnusedLocal
def find_account(name, password):
    """
    A function to find an account by specifying a name
    """
    return User.find_account(password)

def create_user(name, password):
    """
    A function that creates a new user
    """
    new_user = User(name, password)
    return new_user

def save_user(user):
    """
    A function to save user
    """
    user.save_user()

def display_users():
    """
    A function that displays all the users
    """
    return User.display_users()


# noinspection PyUnusedLocal
def intro():
    global credential, key
    print('Welcome to Password Manager')
    print('\n')
    print('Sign up for an account')

    while True:
        print(' Use these short codes : cu - Create user, lg - login if user exists, du - display users, q - Quit/ exit the app ')
        print('-'*56)
        print('\n')
        short_code = input().lower()
        print('\n')

        if short_code == 'cu':
            print('New user')
            print('-'*8)

            print('Enter your name')
            name = input()

            print('Enter your password')
            password = input()
            print('\n')

            save_user(create_user(name, password))
            print('\n')
            print('Great! {name} you created an account \n')
            print('\n')

        elif short_code =='lg':
            print('Enter your username')
            account_name = input()
            print('\n')

            auth = getpass.getpass('password:')
            if check_if_user_exists(auth):
                assert isinstance(auth, object)
                search_account: None = find_account(auth)


                while True:
                    print('Welcome {search_account : None = find_account(auth)}, \n')
                    print(' Use cc- To create new credentials, vc- To view all your credentials, ex- To exit the account \n ')
                    print('-'*56)
                    short_code = input().lower()
                    if short_code == 'cc':
                        print('New credential creation')
                        print('-'*8)
                        print('Enter account name')
                        account_name = input()
                        print('Create a password \n')
                        print('To make your own password, press- a, to generate a password press- g \n')
                        print('-'*56)
                        generate = input()
                        print('\n')

                        if generate == 'g':
                            letters = string.ascii_letters + string.digits
                            generatedpassword = ''.join(random.choice(letters) for i in range(9))
                            print('Your new generated pass word is: {generatedpassword} \n')
                            key = generatedpassword

                        elif generate == 'a':
                            print("Enter its password")
                            key = input()
                            print('\n')
                        print('{account_name} has been saved')

                        save_credential(create_credential(account_name,key))

                    elif short_code == 'vc':
                        if display_credentials:
                            print('Well, This is the list of all your accounts and passwords \n')
                            for credential in display_credentials():
                                print('Account name: {credential.account_name} - password: {credential.key}')

                    elif short_code == 'dc':
                        print('Which credential would you like to delete?')
                        erase_account = input()
                        if erase_account == account_name:
                            Credential.credential_list.remove(credential)
                            print('Credential deleted')
                        else:
                            print('Credentials do not match any.')

                    elif short_code == 'ex':
                        print('You have exited your account')
                        break
            else:
                print('The password was incorrect')
                print('\n')
        elif short_code =='du':
            print('List of all the users \n')
            for user in display_users():
                print("{user.name} \n")

        elif short_code == 'q':
            print('You have quit the app')

            break

        else:
            print('Use the specified short codes to access the service')

if __name__ == '__main__':
    intro()
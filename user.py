class User:
    '''
    initialise a class that generates new instance of user accounts
    '''
    user_list = [] 

    def __init__(self,name,password): #creates a user instance
        self.name = name
        self.password = password

    def save_user(self):
        '''
        this is the method that saves a user to the user-list when they create an account
        '''
        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        '''
        the method to display all the users
        '''
        return cls.user_list

    @classmethod
    def user_exists(cls, password):
        '''
        method to check if the user and their credentials exists
        '''
        for user in cls.user_list:
            if user.password == password:
                return True
        return False


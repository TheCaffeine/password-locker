import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class defining test cases for user  class
    '''
    def setUp(self):
        '''
        A set up method which runs before each test case
        '''
        self.new_user = User('TheCaffeine','Andrea857900')

    def test_init(self):
        '''
        Test method that checks if the user object is initialised properly
        '''
        self.assertEqual(self.new_user.name, 'TheCaffeine')
        self.assertEqual(self.new_user.password, 'Andrea857900')

    def test_save_user(self):
        '''
        Test method to test if the user has been saved on the user list
        '''
        self.new_user.save_user() # method to save user
        self.assertEqual(len(User.user_list),2) #expecting 1 !=2 since there is only one contact saved currently

    def test_save_many_users(self):
        '''
        Test case to check if multiple users can be saved
        '''
        self.new_user.save_user() # method to save user
        test_user = User('test','user','any')
        test_user.save_user()
        self.assertEqual(len(User.user_list),4)

    def test_display_users(self):
        '''
        test case to check if users are displayed
        '''
        self.assertEqual(User.display_users(),User.user_list)
    def test_user_exists(self):
        '''
        test case to check if the user exists in the user list
        '''
        self.new_user.save_user()
        test_user = User('test','TheCaffeine','Andrea857900')
        test_user.save_user()
        user_exits = User.user_exists('test')
        self.assertTrue(user_exits)

if __name__ == '__main__':
    unittest.main()

import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    Test class defining test cases for user  class
    """

    def setUp(self):
        """
        A set up # noinspection PyStatementEffect
method which runs before each test case
        """
        self.new_user = User('TheCaffeine', '19xy13!')

    def test_init(self):
        """
        Test method that checks if the user var = object is initialised properly
        """
        self.assertEqual(self.new_user.name, 'TheCaffeine')
        self.assertEqual(self.new_user.password, '19xy13!')

    def test_save_user(self):
        """
        Test method to test if the user has been saved on the user list
        """
        self.new_user.save_user()  # method to save user
        self.assertEqual(len(User.user_list), 2)  # expecting 1 !=2 since there is only one contact saved currently

    def test_save_many_users(self):
        """
        Test case to check if multiple users can be saved
        """
        self.new_user.save_user()  # method to save user
        test_user = User('test', 'user')
        test_user.save_user()
        self.assertEqual(len(User.user_list), 4)
# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

# other test cases here
    def test_save_multiple_users(self):
            '''
            test_save_multiple_user to check if we can save multiple users
            objects to our user_list
            '''
            self.new_user = User('test', 'user').save_user()
            test_user = User('test', 'user')("Test","user","0712345678","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

if __name__ == '__main__':
    unittest.main()
    def test_display_users(self):
        """
        test case to check if users are displayed
        """
        self.assertEqual(User.display_users(), User.user_list)

    def test_user_exists(self):
        """
        test case to check if the user exists in the user list
        """
        self.new_user.save_user()
        test_user = self.new_method()
        test_user.save_user()
        user_exits = User.user_exists('test')
        self.assertTrue(user_exits)

    def new_method(self):
        test_user = User('test', 'name')
        return test_user


if __name__ == '__main__':
    unittest.main()

import unittest
from credential import Credential


class TestUser(unittest.TestCase):
    """
    Test class defining the user credentials
    """

    def setUp(self) -> object:
        """
        Setup method that runs before each test case
        """
        self.new_credential = Credential('random', 'any')

    def test_init(self):
        """
        test method to check if credentials have been initialised properly
        """
        self.assertEqual(self.new_credential.account_name, 'random')
        self.assertEqual(self.new_credential.key, 'any')

    def test_save_credentials(self):
        """
        Test case to check whether credentials have been added to credentials list
        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_display_credentials(self):
        """
        test case for displaying user credentials
        """
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)

    def test_delete_credential(self):
        """
        test case for deleting a user credential
        """
        self.new_credential.save_credentials()
        test_credential = Credential('testing', 'okay')
        test_credential.save_credentials(3)

        self.new_credential.delete_credential(3)
        self.assertEqual(len(Credential.credential_list), 2)

    if __name__ == '__main__':
        unittest.main()

class Credential:
    """
    Class that generates new instances of user credentials
    """
    credential_list = []

    def __init__(self, account_name: object, key: object) -> object:
        """

        @rtype: object
        """
        self.account_name = account_name
        self.key = key

    def save_credentials(self) -> object:
        """
        this method saves the credentials of a user when they create an account
        """
        Credential.credential_list.append(self)

    @classmethod
    def display_credentials(cls):
        """
        the method that returns the credentials
        """
        return cls.credential_list

    @classmethod
    def delete_credential(cls,account):
        """
        method to delete a credential
        """
        for credential in cls.credential_list:
            if credential.account_name == account:
                return credential

    
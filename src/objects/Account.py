#CK

from recources import stringHandler


# | Account() - previously Password()
# |-----------------------------------------------------------------------------------------------------
# | Object for an account. Contains attributes for the account type, username, plaintext password and
# | and encrypted password, and if it's a new or one read from a file. It also contains methods for
# | encrypting and decrypting the password, depending on if the account is new or being re-read.
# |-----------------------------------------------------------------------------------------
class Account:
    def __init__(self, new, type, owner, username, password):
        self.type = type
        self.owner = owner
        self.username = username

        if new:
            self.password = password
            self.encrypted = None
        else:
            self.encrypted = password
            self.password = None

        self.new = new

    # | encrypt()
    # |-------------------------------------------------------------------------------------
    # | Calls the encrypt method from stringHandler on the password's plaintext attribute.
    # |-------------------------------------------------------------------------------
    def encrypt(self, keyword):
        self.encrypted = stringHandler.encrypt(self.password, keyword)

    # | decrypt()
    # |--------------------------------------------------------------------------------------
    # | Calls the decrypt method from stringHandler on the password's encrypted attribute.
    # |--------------------------------------------------------------------------------
    def decrypt(self, keyword):
        self.password = stringHandler.decrypt(self.encrypted, keyword)

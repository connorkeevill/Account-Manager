#CK

import stringHandler

# | Password()
# |------------------------------------------------------------------------------------------------------
# | Object for a password, weather it be a new one entered by the user, or one being read from a file.
# | Contains attributes for the (encrypted) password and plaintext. They will be None if not known
# | yet. The 'cases' attribute' is a list where each item is a 1 or 0 corresponding to all the
# | letters in the plaintext version of the password. 1 means an uppercase character, where
# | 0 means either a lowercase character or a special character; anything not a letter.
# |--------------------------------------------------------------------------------
class Password:
    def __init__(self, known, text, cases = None):
        if known:
            self.password = text
            self.encrypted = None
            self.cases = self.findCases(text)
        else:
            self.encrypted = text
            self.password = None
            self.cases = cases

        self.known = known

    # | findCases()
    # |----------------------------------------------------------------------
    # | Returns a list of either 1's or 0's, representing the cases of the
    # | plaintext version of the password. Uppercase will be 1, where
    # | lowercase or special characters (non-letters) will be a 0.
    # | Note: this method may be dropped due to a possible alternate method of tracking cases.
    # |------------------------------------------------------
    def findCases(self, text):
        cases = []
        for letter in text:
            cases.append(letter.isupper())
        return cases

    # | encrypt()
    # |-------------------------------------------------------------------------------------
    # | Calls the encrypt method from stringHandler on the password's plaintext attribute.
    # |-------------------------------------------------------------------------------
    def encrypt(self, keyword):
        self.encrypted = stringHandler.encrypt(self.password, keyword)
        print(self.encrypted)

    # | decrypt()
    # |--------------------------------------------------------------------------------------
    # | Calls the decrypt method from stringHandler on the password's encrypted attribute.
    # |--------------------------------------------------------------------------------
    def decrypt(self, keyword):
        self.password = stringHandler.decrypt(self.encrypted, keyword)
        print(self.password)

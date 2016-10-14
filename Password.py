#CK

# |------------------------------------------------------------------------------------------------------
# | Object for a password, weather it be a new one entered by the user, or one being read from a file.
# | Contains attributes for the (encrypted) password and plaintext. They will be None if not known
# | yet. The 'cases' attribute' is a list where each item is a 1 or 0 corresponding to all the
# | letters in the plaintext version of the password. 1 means an uppercase character, where
# | 0 means either a lowercase character or a special character; something not a letter.
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

    def findCases(self, text):
        cases = []
        for letter in text:
            if letter.isupper():
                cases.append(1)
            elif letter.islower():
                cases.append(0)
            else:
                cases.append(None)
        return cases


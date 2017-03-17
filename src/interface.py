#CK

import templates, helpers

class CommandLine():
    def __init__(self, file):
        self.file = file

        self.greet()
        self.mainMenu()

    def greet(self):
        print(templates.greeting())

    def mainMenu(self):
        choice = helpers.inputOption(templates.mainMenu(), ['A', 'V', 'Q'])

        if choice == 'A':
            self.addAccount()
        elif choice == 'V':
            self.viewAccounts()
        elif choice == 'Q':
            self.quit()

    def addAccount(self):
        None

    def viewAccounts(self):
        None

    def quit(self):
        None



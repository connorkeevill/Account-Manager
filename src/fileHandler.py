#CK

class fileHandler():

    def __init__(self, fileName=None):

        if fileName == None:
            self.fileName = self.getFileName()
        else:
            self.fileName = fileName

        self.file = None

    def getFileName(self):
        prompt = 'Please enter the directory of the file you\'re using: '

        while True:
            try:
                name = input(prompt)
                newFile = open(name)
                newFile.close()
                break
            except:
                print('FAILED')
                print('Make sure the file you\'re attempting to open exists and that you have the correct file path.')
        return name

    def addWrite(self, message):
        self.file = open(self.fileName, 'a')
        self.write(message)

    def overWrite(self, message):
        self.file = open(self.fileName, 'w')
        self.write(message)

    def write(self, message):
        self.file.write(message)
        self.file.close()

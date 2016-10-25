#CK

import unittest
from fileHandler import fileHandler

class fileIOTests(unittest.TestCase):

    def test_file_overWriting_works(self):
        testFile = fileHandler('test.txt')
        testFile.overWrite('Hi there.')

        file = open('test.txt', 'r')
        self.assertEqual(file.read(), 'Hi there.')

if __name__ == '__main__':
    unittest.main()

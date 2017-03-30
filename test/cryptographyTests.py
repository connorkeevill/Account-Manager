#CK

import unittest

from recources.stringHandler import encrypt, decrypt


class cryptograpyTest(unittest.TestCase):

    def test_simple_encryption(self):
        self.assertEqual(encrypt('computing', '!'), 'dpnqvujoh')

    def test_simple_decryption(self):
        self.assertEqual(decrypt('dpnqvujoh', '!'), 'computing')

    def test_compound_encryption(self):
        self.assertEqual(encrypt('computing', 'key'), 'PVh]\\oVUb')

    def test_compound_decryption(self):
        self.assertEqual(decrypt('PVh]\\oVUb', 'key'), 'computing')

    def test_simple_encryption_with_cases(self):
        self.assertEqual(encrypt('CoMpUtInG', '!'), 'DpNqVuJoH')

    def test_simple_decryption_with_cases(self):
        self.assertEqual(decrypt('DpNqVuJoH', '!'), 'CoMpUtInG')

    def test_compound_encryption_with_cases(self):
        self.assertEqual(encrypt('CoMpUtInG', 'kEy'), '06H]zo65B')

    def test_compound_decryption_with_cases(self):
        self.assertEqual(decrypt('06H]zo65B', 'kEy'), 'CoMpUtInG')

    def test_encryption_can_loop_alphabet(self):
        self.assertEqual(encrypt('computing', '~'), 'computing')

    def test_decryption_can_loop_alphabet(self):
        self.assertEqual(decrypt('computing', '~'), 'computing')

if __name__ == '__main__':
    unittest.main()
import unittest
from  code.vault_validator import *

class TestVaultValidator(unittest.TestCase):

    def setUp(self):
        self.checker = vault_validator.Vault_Validator()

    def test_valid_char_length(self):
        self.assertTrue(self.checker.is_valid_length("njdyu877e7gbhcd"))

if __name__ == "__main__":
    unittest.main()
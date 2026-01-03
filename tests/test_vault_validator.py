import unittest
from sentryvault.vault_validator import Vault_Validator

class TestVaultValidator(unittest.TestCase):

    def setUp(self):
        self.checker = Vault_Validator()

    def test_valid_char_length(self):
        self.assertTrue(self.checker.is_valid_length("njdyu877e7gbhcd"))

if __name__ == "__main__":
    unittest.main()
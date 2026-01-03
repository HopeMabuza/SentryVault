import unittest
from sentryvault.vault_validator import Vault_Validator

class TestVaultValidator(unittest.TestCase):

    def setUp(self):
        self.checker = Vault_Validator()

    def test_valid_char_length(self):
        self.assertTrue(self.checker.is_valid_length("njdyu877e7gbhcd"))

    def test_invalid_char_length(self):
        self.assertFalse(self.checker.is_valid_length("nvbhg"))


    def test_contains_uppercase(self):
        self.assertTrue(self.checker.contains_uppercase("shjhgSGJG"))

    def test_no_uppercase(self):
        self.assertFalse(self.checker.contains_uppercase("njkshkhgiuo8"))


    def test_contains_lowercase(self):
        self.assertTrue(self.checker.contains_lowercase("nkshHIo0489"))

    def test_no_lowercase(self):
        self.assertFalse(self.checker.contains_lowercase("SNJGY6589I00Y"))


    def test_contains_digit(self):
        self.assertTrue(self.checker.contains_digit("njguoytr789u"))

    def test_no_digit(self):
        self.assertFalse(self.checker.contains_digit("nncjhgyuUHHG"))


    def test_contains_special_character(self):
        self.assertTrue(self.checker.contains_special_character("jgyuskl*?"))

    def test_no_special_character(self):
        self.assertFalse(self.checker.contains_special_character("bjgiyutFFFIUK2"))

    def test_valid_password(self):
        self.assertTrue(self.checker.is_valid_password("nkshHIo0489*"))
        self.assertTrue(self.checker.is_valid_password("hope_Mabu67"))
        self.assertTrue(self.checker.is_valid_password("nncjhgyu88+UHHG"))

    def test_invalid_password(self):
        self.assertFalse(self.checker.is_valid_password("njguoytr789u"))
        self.assertFalse(self.checker.is_valid_password("SNJGY6589I00Y"))
        self.assertFalse(self.checker.is_valid_password("nvbhg"))


if __name__ == "__main__":
    unittest.main()
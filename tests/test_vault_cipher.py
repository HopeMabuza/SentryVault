import unittest
from sentryvault.vault_cipher import Vault_Cipher

class TestVaultCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = Vault_Cipher()

    def test_encrypt_message(self):
        self.assertEquals(self.cipher.encrypt("H0p3#well", "Happiness"), "")
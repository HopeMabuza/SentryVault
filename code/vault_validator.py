class Vault_Validator:
    def __init__(self, password):
        self.password = password

    def is_valid_length(self, password):
        #method for checking if the length of the password is equals to or greater than 8
        #parameter -> password
        #returns -> boolean
        return True

    def contains_uppercase(self, password):
        #method for checking if the password contains any uppercase
        #parameter -> password
        #returns -> boolean
        return True

    def contains_lowercase(self, password):
        #method for checking if the password contains any lowercase
        #parameter -> password
        #returns -> boolean
        return True

    def contains_digit(self, password):
        #method for checking if the password contains any digits
        #parameter -> password
        #returns -> boolean
        return True

    def contains_special_character(self, password):
        #method for checking if the password contains any special character
        #parameter -> password
        #returns -> boolean
        return True

    def is_valid_password(self, password):
        #checks if all the above methods are true for the password to be valid
        return True


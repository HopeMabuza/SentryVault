class Vault_Validator:

    def is_valid_length(self, password: str) -> bool:
        #method for checking if the length of the password is equals to or greater than 8
        #parameter -> password
        #returns -> boolean

        return len(password) >= 8


    def contains_uppercase(self, password: str) -> bool:
        #method for checking if the password contains any uppercase
        #parameter -> password
        #returns -> boolean
        for i in password:
            if i.isupper():
                return True
        return False
            

    def contains_lowercase(self, password: str) -> bool:
        #method for checking if the password contains any lowercase
        #parameter -> password
        #returns -> boolean
        for i in password:
            if i.islower():
                return True
        return False


    def contains_digit(self, password: str) -> bool:
        #method for checking if the password contains any digits
        #parameter -> password
        #returns -> boolean
        for i in password:
            if i.isdigit():
                return True
        return False


    def contains_special_character(self, password: str) -> bool:
        #method for checking if the password contains any special character
        #parameter -> password
        #returns -> boolean
        for i in password:
            if not i.isalnum():
                return True
        return False

    def is_valid_password(self, password: str) -> bool:
        #checks if all the above methods are true for the password to be valid
        return ( self.is_valid_length(password) and  
                self.contains_uppercase(password) and 
                self.contains_lowercase(password) and 
                self.contains_digit(password) and 
                self.contains_special_character(password) )

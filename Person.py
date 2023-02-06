class User:
    def __init__(self,Username,Email,password):
        self.Username = Username
        self.Email = Email
        self.Password = self.Encrypt(password)
    def PrintCharacteristics(self):
        print("Username: "+self.Username)
        print("Email: "+self.Email)
        print("Password: "+self.Password)
    def Encrypt(password):
        Encrypted_Password =""
        for n in range(len(password)): 
            character = ord(password[n])+3
            Encrypted_Password+=str(character)
        print(Encrypted_Password)
person_one = User("Username","Email","randomkitty")
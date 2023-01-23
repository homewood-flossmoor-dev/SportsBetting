class User:
    def __init__(self,Username,Email,Password):
        self.Username = Username
        self.Email = Email
        self.Password = Password
    def PrintCharacteristics(self):
        print("Username: "+self.Username)
        print("Email: "+self.Email)

    def Username = str(input("Username: ")) 

person_one = User("Username","Email","Password")

person_one.PrintCharacteristics()


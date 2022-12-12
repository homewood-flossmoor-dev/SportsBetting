class User:
    def __init__(self,Username,Email,Password):
    self.Username = Username
    self.Email = Email
    self.Password = Password
    
    def Username = str(input("Username: "))
    def Email = str(input("Email: "))
    ConfirmEmail = str(input("Confirm Email: "))
    if ConfirmEmail != Email:
        print("Emails do not match!")
    else:
        def Password = str(input("Password: "))
        ConfirmPassword = str(input("Confirm Password: "))
        if ConfirmPassword != Password:
            print("Passwords do not match!")

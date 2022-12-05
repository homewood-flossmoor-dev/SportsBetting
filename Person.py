class User:
    Username = str(input("Username: "))
    Email = str(input("Email: "))
    ConfirmEmail = str(input("Confirm Email: "))
    if ConfirmEmail != Email:
        print("Emails do not match!")
    else:
        Password = str(input("Password: "))
        ConfirmPassword = str(input("Confirm Password: "))
        if ConfirmPassword != Password:
            print("Passwords do not match!")

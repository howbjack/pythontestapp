"""Does a validation of a password to ensure it complies to predefined policy rules"""

def password_length(pswd):
    """Checks if length is a minimum of X characters"""
    print(f"{userid}, the length of your password {'*' * len(pswd)} is : {len(pswd)} characters")


userid = input("Enter the userid: ")
pass_in   = input("Enter the password: ")
password_length(pass_in)

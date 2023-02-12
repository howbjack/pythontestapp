def password_checker(): 

    userid = input("Enter the userid: ")
    pswd   = input("Enter the password: ")

    print(f"{userid}, the length of your password {'*' * len(pswd)} is : {len(pswd)} characters")



password_checker()
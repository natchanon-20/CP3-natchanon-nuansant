usernameInput = input("username  ")
passwordInput = input("password  ")
if usernameInput == "admin" and passwordInput == "1234":
    print("welcome")
    print("1. vat Calculator")
    print("2. product Calculator")
    UserSelected = int(input("number"))
    if UserSelected == 1:
        price = int(input("price THB : "))


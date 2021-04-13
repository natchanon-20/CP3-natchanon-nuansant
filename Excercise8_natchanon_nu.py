usernameInput = input("username  ")
passwordInput = input("password  ")
if usernameInput == "admin" and passwordInput == "1234":
    print("welcome")
    print("1. vat Calculator")
    print("2. product Calculator")
    print("3. speed Calculator")
    UserSelected = int(input("number"))
    if UserSelected == 1:
        price = int(input("price THB : "))
        vat = 7
        result = price + (price * vat/100)
    elif UserSelected == 2 :
        print("price")
        Product1 = int(input("product = "))
        Product2 = int(input("product = "))
        print(Product1+Product2)
    elif UserSelected == 3 :
        km = int(input("speed"))
        t = 20
        print(km / t)



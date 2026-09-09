password = input("Setting your password: ")
if sum(1 for char in password if char.isupper()) >= 1 :
    if sum(1 for char in password if char.islower()) >= 1 :
        if sum(1 for char in password if char.isdigit()) >= 1 :
            if len(password) >= 8 :
                if len(password) <= 16 :
                    print(":-) Your password is correct (-:")
                else:
                    print ("!!!Error!!! The password must not contain more than 16 characters")
            else:
                print ("!!!Error!!! The password must contain at least 8 characters")
        else:
            print ("!!!Error!!! The password must contain at least a number")
    else:
        print ("!!!Error!!! The password must contain at least a lowercase letter")
else:
    print ("!!!Error!!! The password must contain at least a capital letter")
    
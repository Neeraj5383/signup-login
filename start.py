import data
max_attempt, attempt, correctUN, correctPass = data.data()
def login():
    print("//" * 10, "\n")
    print("LOGIN\n")
    print("//" * 10, "\n")
    global attempt, max_attempt
    while attempt < max_attempt:
        user_name : str = input("Enter Username : ")
        pass_ward = input("Enter Passward : ")
        if user_name != correctUN and pass_ward != correctPass:
            print("Wrong Username and Passward")
            attempt += 1
            if attempt < max_attempt:
                print("Try Again!!!!")
            else:
                print("Try Again after 24 hours")
            
        else:
            print("login successfully")
            break
def signup():
    print("//" * 10, "\n")
    print("SIGNUP\n")
    print("//" * 10, "\n")
    global attempt, max_attempt
    while attempt < max_attempt:

        
        new_user = input("Enter username : ")
        new_passward = input("Enter passward : ")
        print(new_user)
        print(new_passward)
        print(f"\nif this user name {new_user} or {new_passward} is not correct")
        print("1 : not correct")
        print("2 : correct")
        checking = input("Enter Option : ")
        if checking == "1":
            attempt +=1
            if attempt < max_attempt:
                print("try again!!!")
            else:
                print("try after 24 hours later")
        else:
            print("Here user name {",new_user, "} and passward {", new_passward,"}")
            break
            
def login():
    i=1
    while i!=0:
        u=input("enter user id")
        v=input("enter password")
        if u==v:
            print("login successful")
            n=0
            break
        else:
            print("login failed")
login()

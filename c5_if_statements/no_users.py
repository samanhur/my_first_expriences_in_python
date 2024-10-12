# usernames = ['saman', 'admin', 'soheyl', 'mina', 'zohreh', 'nazanin']
usernames = []

if usernames:    
    for username in usernames :
        if username == 'admin' :
            print("\n\tHello Admin, How can I help you?\n")
        else:
            print(f"Welcome {username}, thank you for logging in again.")
else:
    print("We need to find some users.")
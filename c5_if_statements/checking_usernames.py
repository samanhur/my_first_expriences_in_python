current_users = ['SamanHur', 'Mehdiyakoza', 'daVood', 'HasanKachal', 'CR7', 
                 'mohaMMad', 'SInA', 'KINGprogrammer']
new_users = ['samanHUR', 'SInA', 'HasanKaChal', "mohsen", "amir", "REZA"]
users = []
for user in current_users :
    users.append(user.lower())
n_users = []
for n_user in new_users :
    n_users.append(n_user.lower())

for user in users :
    if user in n_users:
        print(f"This '{user}' user name already exist. Please pick another one")
    else:
        print(f"You can keep '{user}' as you user name.")
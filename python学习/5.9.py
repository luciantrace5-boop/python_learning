user_name_list = ['admin','tony','lucian','lancer','saber']
print('Welcome to this website!')
if len(user_name_list) == 0:
    print('We need to find some users!')
else:
    for user_name in user_name_list:
        if user_name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user_name}, thank you for logging again.')



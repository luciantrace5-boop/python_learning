#5.8
user_name_list = ['admin','tony','lucian','lancer','saber']
print('Welcome to this website!')
for user_name in user_name_list:
    if user_name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user_name}, thank you for logging again.')

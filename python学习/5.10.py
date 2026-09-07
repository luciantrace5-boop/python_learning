current_users = ['admin','tony','lucian','lancer','saber']
new_users = ['drake','trace','caster','sam','lucian']
current_users_lower = []
for i in current_users:
    current_users_lower.append(i.lower())
# 更简洁的写法 current_users_lower = [i.lower() for i in current_users]
for i in new_users:
    i_lower = i.lower()
    if i_lower in current_users_lower:
        print(i)
        print('Sorry, you need to enter a different username.')
    else:
        print(i)
        print('This username is not taken.')
# current_users = ['admin', 'tony', 'lucian', 'lancer', 'saber']
# new_users = ['drake', 'trace', 'caster', 'sam', 'lucian']
#
# current_users_lower = [user.lower() for user in current_users]
#
# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print(f"{new_user} - Sorry, you need to enter a different username.")
#     else:
#         print(f"{new_user} - This username is not taken.")
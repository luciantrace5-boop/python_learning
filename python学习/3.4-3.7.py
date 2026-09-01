#3.4
invitation_list = ['Jitong Shi','Wenlong Pan','Yifu Guo','Jiahang Hu']
print(f"{invitation_list[0]},Would you like to have dinner with me?")
print(f"{invitation_list[1]},Would you like to have dinner with me?")
print(f"{invitation_list[2]},Would you like to have dinner with me?")
print(f"{invitation_list[3]},Would you like to have dinner with me?")
#3.5
print(f"I have just learned {invitation_list[0]} can not come.")
invitation_list.remove('Jitong Shi')
print(invitation_list)
#3.6
invitation_list.insert(0,'Kangping Leng')
invitation_list.insert(2,'Junyi Su')
invitation_list.append('Jiandong Wang')
print(invitation_list)
#3.7
print("Sorry,I can only invite two persons to come because of some unexpected reasons.")
# poped_invitation_list = invitation_list.pop(0)
# poped_invitation_list = invitation_list.pop(1)
# poped_invitation_list = invitation_list.pop(2)
# poped_invitation_list = invitation_list.pop(2)
# print(invitation_list)
# del invitation_list[0]
# del invitation_list[0]
# print(invitation_list)
del_indices = [0,2,4,5]
new_invitation_list = [elem for i,elem in enumerate(invitation_list) if i not in del_indices]#遍历
print(new_invitation_list)







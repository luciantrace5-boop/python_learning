#5.3#5.4
alien_color = 'green'
if alien_color == 'green':
    print('You would get five points.')
else:
    print('You would get ten points')
#5.5
if alien_color == 'green':
    print('You would get five points.')
elif alien_color == 'red':
    print('You would get ten points.')
else:
    print('You would get fifth points.')
#5.6
age = 71
if age < 2:
    print('The person is a baby.')
elif 2 <= age < 4:
    print('The person is a toddler.')
elif 4 <= age < 13:
    print('The person is a child.')
elif 13 <= age < 18:
    print('The person is a teenager.')
elif 18 <= age < 65:
    print('The person is an adult.')
else:
    print('The person is an old man.')
#5.7
favorite_fruits = ['apple','orange','grape','mongo','banana']
guest = ['apple','peer']
for i in guest:
    if i in favorite_fruits:
        print(f'You really like {i}!')
    else:
        print(f'You do not like {i}.')


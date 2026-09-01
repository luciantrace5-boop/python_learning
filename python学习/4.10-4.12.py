#4.10
numbers = list(range(1,12))
print('The first three items in the list are:')
print(numbers[:3])
print('The middle three items in the list are:')
print(numbers[4:7])
print('The last three items in the list are:')
print(numbers[-3:])
#4.11
pizzas = ['Maegherita Pizza','Pepperoni Pizza','Seafood Pizza']
friend_pizzas = pizzas[:]
friend_pizzas.append('Hawaiian Pizza')
pizzas.append('Vegetarian Pizza')
print('My favorite pizzas are:')
for i in pizzas:
    print(i)
print("My friend's favorite pizzas are:")
for i in friend_pizzas:
    print(i)
#4.12

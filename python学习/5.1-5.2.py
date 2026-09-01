#5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#5.2
str1 = 'Python'
str2 = 'python'
print(str1 == str2)

username_input = 'AdMin'
correct_name = 'admin'
if username_input.lower() == correct_name:
    print('用户名匹配。')
else:
    print('用户名不匹配。')

num1 = 10
num2 = 5
print(num1 == num2)

age = 19
score = 50
if age >= 18 and score >= 80:
    print('成年且优秀')
elif age < 18 or score < 60:
    print('未成年或成绩不及格')
else:
    print('成年且及格。')

fruits = ['apple','banana','orange','grape']
targit_fruit = 'banana'
if targit_fruit in fruits:
    print(f"{targit_fruit.title()} is in the list.")

unwanted_fruit = 'mango'
if unwanted_fruit not in fruits:
    print(f'{unwanted_fruit} is not in fruits.')


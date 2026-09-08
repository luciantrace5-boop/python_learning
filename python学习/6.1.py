person = {'first_name':'Trace','last_name':'Lucian','age':20,'city':'shanghai'}
for key, value in person.items():
    print(f'{key}: {value}')
# 字典的.items()方法会返回一个包含所有 （键, 值） 对的视图，方便你同时获取键和值。
# 如果你只想要键，可以用for key in person:
# 只想要值，用for value in person.values():
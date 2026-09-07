number_list = [i for i in range(1,10)]
for number in number_list:
    if number == 1:
        ordinal = '1st'
    elif number == 2:
        ordinal = '2nd'
    elif number == 3:
        ordinal = '3rd'
    else:
        ordinal = f'{number}th'
    print(ordinal)


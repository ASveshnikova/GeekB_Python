# Task 1. Создать список. Вывести функцией type тип данных из списка.
my_list = ['Harry', 76, 35.78, True, ['a', 'b', 'c', 'd']]
for n in range(len(my_list)):
    print(type(my_list[n]))

# Task 2. Для списка реализовать обмен значений соседних элементов.
# Скажу честно - решение подсматривала в Интернете. Не совсем поняла магию
# со строкой 'user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]'
user_list = list(input('Введите строку произвольных символов без пробелов: '))
if len(user_list) % 2 == 0:
    user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
    print(' '.join([str(i) for i in user_list]))
else:
    e = 0
    while e < len(user_list) - 1:
        user_list[e], user_list[e + 1] = user_list[e + 1], user_list[e]
        e += 2
    print(' '.join([str(e) for e in user_list]))

# Task 3. User вводит месяц целым числом. Определить к какому времени года относиться.
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
month_list = ['winter', 'spring', 'summer', 'autumn']
month_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month == 12 or month == 1 or month == 2:
    print(month_list[0])
    print(month_dict[1])
elif month == 3 or month == 4 or month == 5:
    print(month_list[1])
    print(month_dict[2])
elif month == 6 or month == 7 or month == 8:
    print(month_list[2])
    print(month_dict[3])
elif month == 9 or month == 10 or month == 11:
    print(month_list[3])
    print(month_dict[4])
else:
    print('Вы ввели не верное число. В году 12 месяцев.')

# Task 4. User вводит строку. Вывести каждое слово с новой строки и пронумеровать.
user_text = input('Введите строку из нескольких слов: ')
entry_list = user_text.split()
for i in range(len(entry_list)):
    print(i + 1, ')', entry_list[i])

# Task 5.
user_list_5 = [7, 5, 3, 3, 2]
m = int(input('Введите целое натуральное число: '))
for i in range(len(user_list_5)):
    if user_list_5[i] == m:
        user_list_5.insert(i + 1, m)
        break
    elif user_list_5[0] < m:
        user_list_5.insert(0, m)
    elif user_list_5[-1] > m:
        user_list_5.append(m)
print(user_list_5)















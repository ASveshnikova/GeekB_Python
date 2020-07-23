# Task 1.
line_list = []
while True:
    line = input("Вводите любой текст. Для завершения ввода нажмите Enter: ")
    if line == '':
        print(line_list)
        exit()
    else:
        newline = line + '\n'
        line_list.append(newline)

    with open("text_1.txt", "w", encoding="utf-8") as file:
        file.writelines(line_list)


# Task 2.
str_list = ["See the great big waves\n", "Splashing on the shore\n"]

rw_file = open('text_2.txt', 'a', encoding="utf-8")
rw_file.writelines(str_list)
rw_file.close()

with open("text_2.txt", 'r', encoding="utf-8") as f_obj:
    lines_list = f_obj.readlines()
    lines = len(lines_list)
    w_str = ' '.join(lines_list)
    words = w_str.count(' ') + 1

print(f'Общее количество слов в файле {words}')
print(f'Всего строк в файле {lines}')

# Task 3.
with open('text_3.txt', 'r', encoding="utf-8") as file_3:
    staff = []
    salary = []
    staff_list = file_3.read().split('\n')
    for i in staff_list:
        i = i.split()
        if float(i[1]) < 20000:
            salary.append(i[0])
        staff.append(i[1])
print(f'Оклад меньше 20.000 {salary}, средний оклад {sum(map(float, staff)) / len(staff)}')


# Task 4.
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_4.txt', 'r', encoding="utf-8") as file_4:
    for i in file_4:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('text_4_new.txt', 'w', encoding="utf-8") as file_42:
    file_42.writelines(new_file)


# Task 5.
try:
    with open("text_5.txt", "w+", encoding="utf-8") as file_5:
        num = input('Введите цифры через пробел: ')
        file_5.writelines(num)
        number = num.split()
        print(sum(map(int, number)))
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Ошибка ввода-вывода. Необходимо вводить только цифры.')


# Task 6.

# Task 7.




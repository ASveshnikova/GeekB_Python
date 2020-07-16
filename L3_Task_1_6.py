# Task 1. Функция принимает два числа и выполняет деление.
def my_fun1(num_1, num_2):
    try:
        res = num_1 / num_2
        return res
    except ZeroDivisionError:
        print('Некорректное значение. Делить на ноль нельзя')
    except ValueError:
        print('Необходимо вводить только числа')


print(my_fun1(int(input('Введите первое число: ')), int(input('Введите второе число: '))))


# Task 2. функция принимает несколько параметров. Именованные аргументы.
def my_fun2(name, surname, year_b, city, email, phone):
    print(name, surname, year_b, city, email, phone)


my_fun2(name='Leksa', surname='Sveshnikova', year_b=1982, city='Moscow', email='email@mail.ru', phone='7-903-345-78-90')


# Task 3. Функция принимает три аргумента. Выводит сумму наибольших двух.
def my_fun3(num_1, num_2, num_3):
    res_list = [num_1, num_2, num_3]
    l_min = min(res_list)
    res_list.remove(l_min)
    print(sum(res_list))


my_fun3(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: ')))


# Task 4. Вариант 1. Функция возводит в отрицательную степень.
def my_fun4(x, y):
    z = x ** y
    print(z)


my_fun4(int(input('Введите действительное положительное число: ')), int(input('Введите целое отрицательное число: ')))


# Task 4. Вариант 2. Функция возводит в отрицательную степень.
def my_f4(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print(my_f4(int(input('Введите действительное положительное число: ')), int(input('Введите целое отрицательное число: '))))


# Task 5. Функция запрашивает числа и считает сумму до тех пор, пока не ввели символ для выхода.
def my_fun5():
    sum_res = 0
    n = True
    while n:
        number = input('Введите числа через пробел или Q для выхода: ').split()
        res = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                n = False
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f'Текущая сумма: {sum_res}')
    print(f'Итоговая сумма: {sum_res}')


my_fun5()


# Task 6. Функция меняет первую букву слова на прописную.
def int_func(text):
    print(text.title())


text = input('Введите слово маленькими латинскими буквами: ')
int_func(text)

line = input('Введите строку из слов маленькими латинскими буквами: ')
int_func(line)






# Task_1. Работа с переменными.
name = input('Как вас зовут?: ')
city = input('В каком городе вы живёте?: ')
print(f"Привет, {name} из {city}!")
age = int(input('Сколько вам лет?: '))
period = 15
age_period = age + period
print('Через', period, 'вам будет', age_period)

# Task_2. Переводим секунды в формат чч:мм:сс.
seconds = int(input('Введите время в скундах: '))
minutes = seconds // 60
hours = minutes // 60
print("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))

# Task_3. Вводим число n. Найти сумму n + nn + nnn.
n = int(input('Введите число n: '))
s = str(n)
s1 = s + s
s2 = s + s + s
sum_n = n + int(s1) + int(s2)
print('Сумма равна:', sum_n)

# Task_4. Находим самую большую чифру в числе.
number = int(input('Введите целое положительное число: '))
max_number = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max_number:
        max_number = number % 10

print(max_number)

# Task 5. Считаем прибыль и рентабельность.
revenue = int(input('Введите выручку вашей фирмы: '))
costs = int(input('Введите издержки вашей фирмы: '))
if revenue > costs:
    print('Поздравляю, вы на коне!')
    efficiency = (revenue - costs) / revenue
    print('Рентабельность вашей фирмы', efficiency)
    staff = int(input('Введите количество сотрудников: '))
    staff_rev = (revenue - costs) / staff
    print('Прибыль в расчете на каждого сотрудника: ', staff_rev)
else:
    print('Увы, ваши дела плохи.')

# Task 6. Вычисляем прогресс спортсмена в км.
a = int(input('Сколько км пробежал спортсмен в 1й день?: '))
b = int(input('К какому результату стремится спортсмен, км в день?: '))
days = 1
while a <= b:
    a = a + 0.1 * a
    days += 1

print(f'Спортсмен достигнет результата на {days} день.')


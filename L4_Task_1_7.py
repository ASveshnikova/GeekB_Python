# Task 1.
from sys import argv

name_file, time, rate, bonus = argv

salary = (int(time) * int(rate)) + int(bonus)
print(salary)


# Task 2.
given_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in given_list[1:] if el > given_list[given_list.index(el) - 1]]
print(new_list)

# Task 3.
t = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(t)

# Task 4.
g = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
s = [i for i in g if g.count(i) == 1]
print(s)

# Task 5.
from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


print(my_list)
print(reduce(my_func, my_list))

# Task 6.
from itertools import count

for el in count(3):
    if el > 13:
        break
    else:
        print(el)

from itertools import cycle

a = 0
for el in cycle([5, "five", "cool", 7]):
    if a > 7:
        break
    print(el)
    a += 1

# Task 7. Вариант 1.
from math import factorial


def fact():
    for el in range(1, 9):
        yield factorial(el)


f = fact()
print(list(f))


# Task 7. Вариант 2.
def fact2(n):
    for el in range(1, n + 1):
        yield factorial(el)


for l in fact2(5):
    print(l)

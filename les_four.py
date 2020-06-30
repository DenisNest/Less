print('task 1')
def my_calc():
    hh = float(input('Введите количество оработанных часов: '))
    sum_h = float(input('Введите сумму оплаты труда в час: '))
    prize = float(input('Введите размер премии: '))
    result = hh * sum_h
    return result + prize
print(f' Размер заработной платы составил: {my_calc() }')

print('task 2')
a = [int(i) for i in input('Введите несколько чисел ').split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

print(' task 3')
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

print('task 4')
my_list = [20, 7, 4, 5, 44, 2, 8, 10, 8, 5]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)

print('task 5')
from functools import reduce

def my_func(el1, el):
    return el1 * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(100, 1000) if el % 2 == 0])}')

print('task 6')














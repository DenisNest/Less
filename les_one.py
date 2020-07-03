print('1 task')
var1 = 21
var2 = 'text'
print(var1)
print(var2)
user_answer = input('Введите число: ')
print('Вы ввели число - ', user_answer)

print('2 task')
while True:
    user_answer1 = input('укажите время в секундах: ')

    if user_answer1.isdigit():
        user_answer1 = int(user_answer1)
        break

    print('Введите число')

hour = user_answer1 / 3600
hour = int(hour)
minute = (user_answer1 - hour * 3600) / 60
minute = int(minute)
second = user_answer1 - hour * 3600 - minute * 60
second = int(second)
result = '{}:{}:{}'.format(hour, minute, second)
print(result)

print('3 task')
while True:
    n = input('укажите число: ')

    if n.isdigit():
        n = int(n)
        break

var_1 = n * 11
var_2 = n * 111
result = n + var_1 + var_2
print(result)

print('4 task')
user_answer2 = input('Введите целове положительное число: ')
user_answer2 = int(user_answer2)
r = -1
while user_answer2 > 10:
    d = user_answer2 % 10
    user_answer2 //= 10
    if d > r:
        r = d
print(r)

print('5 task')
while True:
    prof = input('Введите значение прибыли фирмы: ')
    cost = input('Введите значение издержек фирмы: ')

    if prof.isdigit():
        prof = int(prof)
    if cost.isdigit():
        cost = int(cost)
        break

    else:
        print('Введите числовое значение!')

if prof > cost:
    print('Ваша фирма работает в плюс')
    ratio = prof / cost
    print('Рентабильность выручки комании состовляет ', ratio)

else:
    print('Ваша фирма рабоатет в минус')

while True:
    comp_em = input('Укажите количество сотрудников фирмы: ')

    if comp_em.isdigit():
        comp_em = int(comp_em)
        break

    else:
        print('Укажите числовое значение')

prof_em = prof / comp_em
print('Прибыль фирмы в расчете на одного сотрудника состовляет:', prof_em)

print('6 task')

res_1 = input('Введите ваш результат за первый день: ')
res_2 = input('Введите желаемое значение: ')
res_1 = int(res_1)
res_2 = int(res_2)
day = 1
while res_1 <= res_2:
    day += 1
    res_1 = 1.1 * res_1

print('Спортсмену понадобится: ', day, 'дней.')






















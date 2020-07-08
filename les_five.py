print('task 1')
#name = input('ведите название файла: ')
#file = open(name, 'w')
#file.write(input('Введите данные: '))
#file.close()

print('task 2')
file1 = open('Test1.txt', 'w')
file1.write('name1\n')
file1.write('name2 ')
file1.write('name3')
file1.close()
file1 = open('Test1.txt', 'r')
content = file1.readlines()
length = len(content)
print('Строк в файле: ', length)
# !Хотел сделать через цикл, н оне понял как.
#x = 0
#while True:
    #x <= length - 1
    #l = content[x].split()
    #print(len(l))
    #x += 1!
l = content[0].split()
l1 = content[1].split()
print('Слов в первой строке: ', len(l))
print('Слов во второй строке: ', len(l1))
file1.close()

print('task 3')
file2 = open('Test2.txt', 'w', encoding='UTF-8')
#def dataEmpl():
    #i = int(input('Введите количество сотрудников: '))
    #count = 0
    #while count < i:
        #file2.write('Имя сотрудника: ')
        #file2.write(input('Введите имя и фамилию: '))
        #file2.write('. ')
        #file2.write('Размер оклада: ')
        #file2.write(input('Введите размер вашего оклада: '))
        #file2.write('тыс.')
        #file2.write('\n')
        #count += 1
#print(dataEmpl())

nameSal1 = input('Фамиля первого сотрудника и его оклад через пробел: ')
nameSal2 = input('Фамиля второго сотрудника и его оклад через пробел: ')
nameSal3 = input('Фамиля третьего сотрудника и его оклад через пробел: ')
file2.write('Фамили сотрудников и их оклад в тыс.')
file2.write('\n')
file2.write(nameSal1)
file2.write('\n')
file2.write(nameSal2)
file2.write('\n')
file2.write(nameSal3)

with open('sal.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')














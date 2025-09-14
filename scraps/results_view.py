import matplotlib.pyplot as plt
from time import strptime, mktime

towns = {'Люберцы': {},
         'Подольск': {},
         'Одинцово': {},
         'Химки': {}}

'''Заполнение данных в towns из scraps.txt'''
with open('scraps1.txt', 'r', encoding='utf-8') as data:
    for line in data:
        str_line = line.split()
        date_and_time = strptime(f'{str_line[0].replace('-', ' ')} {str_line[1][:-3]}', '%Y %m %d %H:%M')
        towns[str_line[2]][mktime(date_and_time)] = int(str_line[-1])

'''Общий вид графика'''
plt.figure(figsize=(16, 9))
plt.suptitle('Суточное распределение температуры в городах Московской области', fontsize=16)
plt.xlabel('Дата и время', fontsize=13)
plt.xticks(rotation=30)
plt.ylabel('Температура', fontsize=13)
plt.legend(loc='best')

'''Отрисовка графиков'''
for town, data in towns.items():
    plt.plot(data.keys(),
             data.values(),
             label=town)

plt.grid()
plt.show()

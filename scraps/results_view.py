import matplotlib.pyplot as plt
from time import strptime, mktime, ctime

data_files = ['scraps.txt',
              'scraps1.txt',
              'scraps2.txt']


def show_plot(file):
    """Рисует график согласно данным из файла."""

    towns = {'Люберцы': {},
             'Подольск': {},
             'Одинцово': {},
             'Химки': {}}
    '''Заполнение данных в towns из scraps[i].txt'''
    with open(file, 'r', encoding='utf-8') as data:
        for line in data:
            str_line = line.split()
            date_and_time = strptime(f'{str_line[0]} {str_line[1][:-3]}', '%Y-%m-%d %H:%M')
            towns[str_line[2]][mktime(date_and_time)] = int(str_line[-1])

    '''Общий вид графика'''
    plt.figure(figsize=(16, 9))
    plt.tight_layout()
    plt.suptitle('Суточное распределение температуры в городах Московской области', fontsize=16)
    plt.xlabel('Дата и время', fontsize=13, labelpad=0)
    old_ticks = [key for key in towns['Люберцы'].keys()]
    new_ticks = [ctime(key)[4:-8] for key in towns['Люберцы'].keys()]
    plt.xticks(old_ticks, new_ticks, rotation=90)
    plt.gca().tick_params(axis='x', labelsize=8)
    plt.ylabel('Температура', fontsize=13)

    '''Отрисовка графиков'''
    for town, data in towns.items():
        plt.plot(data.keys(),
                 data.values(),
                 label=town)


show_plot(data_files[0])
plt.grid()
plt.legend(loc='best')
plt.show()

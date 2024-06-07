def write_holiday_cities(first_letter):
    # РЕАЛИЗАЦИЯ
    pass












import pprint

###
# Формат CSV == Comma-Separated Values
# - строки делятся переносом строки
# - ячейки делятся запятыми
# - если ячейка содержит запятую или перенос строки, ячейка обрамяляется кавычками
# - если внутри системных кавычек есть кавычки, они пишутся в виде двойных кавычек

# Формат простой и поддерживается многими системами программами по работе с таблицами.


###
# Библиотека csv

import csv
import pprint

# csv.reader() - этот метод создат объект, из которого мы сможем построчно извлечь всю информацию из таблицы.

# inventory_of_stash = []
#
# with open('CSV_files/travel-notes.csv', 'r', newline='', encoding='utf-8') as csv_file:
#     csv_data = csv.reader(csv_file)
#     for row in csv_data:
#         inventory_of_stash.append(row)
#
#     #print(inventory_of_stash)


fieldnames = ['name', 'visited', 'wants_to_visit']

inventory_of_stash = []

with open('CSV_files/travel-notes.csv', 'r', newline='') as csv_file:
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        yy = row[1].split(sep=';')
        print(yy)
        for y in yy:
            y.strip()
        print(yy, ')')

    print(yy[1])



    #
    #
    #
    #
    # for row in csv_data:
    #     inventory_of_stash.append(row)
    #     pprint.pprint(row)
    #

# print(f'Вся информация о таблице: {inventory_of_stash}')
#
# # csv.writer() - метод для создания (или дополнения) csv файла
#
# new_artifact_for_stash = ['Sacred Lingam', '1935', '1']
#
# with open('external_data/Indiana_stash.csv', 'w', newline='') as out_csv:
#     writer = csv.writer(out_csv)  # <_csv.writer object at 0x03B0AD80>
#     writer.writerow(new_artifact_for_stash)

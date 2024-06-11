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

# Have visited:
# Want to visit:
# No one has been to:
# In the end we will go to: Almaty


with open('travel-notes.csv', 'r', newline='') as csv_file_input:
    read_csv = csv.DictReader(csv_file_input, fieldnames=fieldnames)
    have_visited_set = set()
    want_to_visit_set = set()

    for data in read_csv:
        if data['name'][0] == 'a'.upper():
            visited_list = data['visited'].split(sep=';')
            visited_list = [vis.strip() for vis in visited_list]  # на всякий случай удаляем пробелы
            have_visited_set.update(visited_list)

            wants_to_visit_list = data['wants_to_visit'].split(sep=';')
            wants_to_visit_list = [vis.strip() for vis in wants_to_visit_list]  # на всякий случай удаляем пробелы
            want_to_visit_set.update(wants_to_visit_list)

    no_one_has_been_set = want_to_visit_set.difference(have_visited_set)

    have_visited = list(have_visited_set)
    want_to_visit = list(want_to_visit_set)
    no_one_has_been = list(no_one_has_been_set)

    have_visited.sort()
    want_to_visit.sort()
    no_one_has_been.sort()







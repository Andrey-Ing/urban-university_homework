import csv


def write_holiday_cities(first_letter):
    assert len(first_letter) == 1, 'В first_letter должен передаваться один символ'
    with open('travel-notes.csv', 'r', newline='') as csv_file_input:
        read_csv = csv.DictReader(csv_file_input, fieldnames=['name', 'visited', 'wants_to_visit'])

        have_visited_set = set()
        want_to_visit_set = set()

        for data in read_csv:
            if data['name']:
                if data['name'][0] == first_letter:
                    visited_list = data['visited'].split(sep=';')
                    visited_list = [vis.strip() for vis in visited_list]  # на всякий случай удаляем пробелы
                    have_visited_set.update(visited_list)

                    wants_to_visit_list = data['wants_to_visit'].split(sep=';')
                    wants_to_visit_list = [vis.strip() for vis in wants_to_visit_list]  # на всякий случай
                    # удаляем пробелы
                    want_to_visit_set.update(wants_to_visit_list)

        no_one_has_been_set = want_to_visit_set.difference(have_visited_set)

        have_visited = list(have_visited_set)
        want_to_visit = list(want_to_visit_set)
        no_one_has_been = list(no_one_has_been_set)

        have_visited.sort()
        want_to_visit.sort()
        no_one_has_been.sort()

        have_visited.insert(0, 'Have visited:')
        want_to_visit.insert(0, 'Want to visit:')

        will_go_to = ['In the end we will go to:', ]
        if no_one_has_been:
            will_go_to.append(no_one_has_been[0])

        no_one_has_been.insert(0, 'No one has been to:')

        with open('holiday.csv', 'w', newline='') as out_csv:
            writer = csv.writer(out_csv)
            writer.writerows([have_visited, want_to_visit, no_one_has_been, will_go_to])


write_holiday_cities('L')

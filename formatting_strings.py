team1_name = '"Мастера кода"'
team1_num = 7
team1_score = 37
team1_time = 18015.2

team2_name = '"Волшебники данных"'
team2_num = 8
team2_score = 34
team2_time = 17981.7

task_total = team1_score + team2_score
time_avg = (team1_time + team2_time) / task_total


def victory():
    if team1_score > team2_score or team1_score == team2_score and team1_time < team2_time:
        return 'Победа команды ' + team1_name
    elif team1_score < team2_score or team1_score == team2_score and team1_time > team2_time:
        return 'Победа команды ' + team2_name
    else:
        return 'Ничья!'


# Использование %:
print('В команде %s участников %d' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

# Использование format():
print('Команда {} решила задач: {} !'.format(team2_name, team2_score))
print('{} решили задачи за {} с !'.format(team2_name, team2_time))

# Использование f-строк:
print(f'Команды решили {team1_score} и {team2_score} задач.')
print(f'Результат битвы: {victory()}')
print(f'Сегодня было решенно {task_total} задач, в среднем по {time_avg:.1f} секунды на задачу!.')

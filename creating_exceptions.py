class InvalidPowerSupplyException(Exception):
    pass


class InvalidRobotMovingException(Exception):
    def __init__(self, message):
        super().__init__(message)


def robot_movement_system(power, direction):
    if power == 'solar_battery':
        print('Питание от солнечной баттареи')
    elif power == 'internal_battery':
        print('Питание от внутреннего аккумулятора')
    elif power == 'nuclear_reactor':
        print('Питание от реактора')
    else:
        raise InvalidPowerSupplyException

    if direction == 'left':
        print('я поехал на лево')
    elif direction == 'right':
        print('я поехал на право')
    elif direction == 'up':
        print('я поехал вверх')
    elif direction == 'down':
        print('я поехал вниз')
    else:
        raise InvalidRobotMovingException('Не понял, куда ехать?!')


def get_in_touch():
    try:
        robot_movement_system('solar_sail', 'up')
    except Exception as exc:
        print(f'Ошибка при выходе на точку! Не знаю, что с этим делать, передам дальше')
        raise exc


def hide_from_sun():
    try:
        robot_movement_system('nuclear_reactor', 'somewhere')
    except Exception as exc:
        print(f'Ошибка, когда прятался от солнца! Не знаю, что с этим делать, передам дальше')
        raise exc


def robot_life():
    try:
        print('Меня позвали на связь с Землёй')
        get_in_touch()
    except InvalidPowerSupplyException:
        print('Что-то непонятное, включить резервный генератор!')
    except InvalidRobotMovingException as exc:
        print(f'{exc}\nСтою на месте, жду команду с Земли')
    else:
        print('Всё хорошо, жду следующую команду с Земли')
    finally:
        print('Антенну на Землю направил')

    try:
        print('Здесь слишком жарко')
        hide_from_sun()
    except InvalidPowerSupplyException as exc:
        print('Что-то непонятное, включить резервный генератор!')
    except InvalidRobotMovingException as exc:
        print(f'{exc}\nСтою на месте, жду команду с Земли')
    else:
        print('Всё хорошо, жду следующую команду с Земли')
    finally:
        print('Антенну на Землю направил')


robot_life()

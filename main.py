def menu(flights):
    print('Главное меню:\n'
          '1 - ввод рейса\n'
          '2 - вывод всех рейсов\n'
          '3 - поиск рейса по номеру\n'
          '0 - завершение работы\n')
    command = int(input('Введите номер пункта меню: '))
    tusker(command, flights)

def check_len(standard, value):
    if len(value) == len(standard):
        return True
    else:
        return False

def adder(pattern, flight, text):
    print('{0} - {1}: '.format(pattern, text), end='')
    info = input().upper()
    if check_len(pattern, info):
        flight.append(info)
    else:
        while not check_len(pattern, info):
            print('Cтрока "{name}" должно сдержать {amount} символа:'.format(name=text,
                                                                             amount=len(pattern)), end=' ')
            info = input().upper()
        flight.append(info)

def time_check(info,  flight):
    count = 0
    for num in info.split(':'):
        if count == 0:
            if 100 - int(num) >= 77:
                count += 1
        elif count == 1:
            if 100 - int(num) >= 41:
                count += 1
    if count == 2:
        return True

def time(pattern, flight, text):
    print('{0} - {1}: '.format(pattern, text), end='')
    info = input().upper()
    if check_len(pattern, info):
        count = 0
        if time_check(info, flight):
            flight.append(info)
        else:
            print('Ошибка. Некорректно введены данные. Повторите попытку.')
            time(pattern, flight, text)
    else:
        print('Cтрока "{name}" должно сдержать {amount} символа:'.format(name=text,                                                                     amount=len(pattern)), end=' ')
        time(pattern, flight, text)

def cost_check(cost):
    if cost > 0:
        return True
    else:
        return False

def flight_cost(info):
    print('.XX - cтоимость билета:', end=' ')
    cost = float(input())
    if cost_check(cost):
        info.append(str(cost) + "руб.")
    else:
        while not cost_check(cost):
            print('Стоимость билета не может быть меньше 0.'
                  '\nПовторите попытку:', end=' ')
            cost = float(input())
            cost_check(cost)
        info.append(str(cost) + "руб.")

def add_flight(flights_dic):
    flight = []
    requests = {'XXXX': 'номер рейса', 'ДД/ММ/ГГГГ': 'дата рейса',
                'ЧЧ:ММ': 'время вылета', 'XX:XX': 'длительность перелета',
                'XXX': ['аэропорт вылета', 'аэропорт назначения']}

    for pattern, text in requests.items():
        if isinstance(text, list):
            for sym in text:
                adder(pattern, flight, sym)
        elif ':' in pattern:
            time(pattern, flight, text)
        else:
            adder(pattern, flight, text)

    flight_cost(flight)
    flights_dic[flight[0]] = flight[1:]

def total_flights(flights_base):
    if len(flights_base) >= 1:
        print('Доступных рейсов: {0}'.format(len(flights_base)))
        for num_flight, flight_info in flights_base.items():
            print('Информация о рейсе:', end=' ')
            print(num_flight, *flight_info)
    else:
        print('Информация о рейсах отсутствует.')

def search_flight(flights_base):
    user_key = input('Введите номер рейса в формате XXXX: ').upper()
    if flights_base.get(user_key):
        print('Информация о рейса: {0}'.format(user_key), *flights_base.get(user_key))
    else:
        print('Рейс {0} не найден.'.format(user_key))

def tusker(command, flights_base):
    if command == 1:
        add_flight(flights_base)
    elif command == 2:
        total_flights(flights_base)
    elif command == 3:
        search_flight(flights_base)
    elif command == 0:
        print("Работа завершена.")
        return
    else:
        print('Ошибка ввода. Повторите попытку.')
        return menu(flights_base)
    print('\n')
    menu(flights_base)

flights = {}
menu(flights)

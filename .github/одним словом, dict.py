def dicter():
    friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
    friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']
    friends = dict(zip(friends_names, friends_cities))
    m = friends["Лена"]
    print("Лена живет в " + m)


if __name__ == '__main__':
    dicter()

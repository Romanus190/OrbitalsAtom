def generate_electron_configuration_up_to_extended():

    # Буквенные обозначения подуровней (l -> буква)
    sublevel_letters = {
        0: 's', 1: 'p', 2: 'd', 3: 'f',
        4: 'g', 5: 'h', 6: 'i', 7: 'k'
    }

    # Максимальное число электронов на подуровне (2*(2l + 1))
    sublevel_max_e = {l: 2 * (2 * l + 1) for l in sublevel_letters}

    max_sublevel = 15

    # Генерируем все возможные орбитали (n, l) по порядку заполнения
    configurations = []
    for n in range(1, max_sublevel):  # До n=23
        for l in range(0, n):  # l может быть от 0 до n-1
            if l in sublevel_letters:  # Только если подуровень существует
                configurations.append((n, l))

    # Сортируем по правилу Клечковского (n + l, затем n)
    configurations.sort(key=lambda x: (x[0] + x[1], x[0]))

    # Формируем последовательность
    result = []
    for n, l in configurations:
        sublevel_letter = sublevel_letters[l]
        max_e = sublevel_max_e[l]
        result.append(f"{n}{sublevel_letter}{max_e}")

    return result

# Генерируем последовательность
config = generate_electron_configuration_up_to_extended()

print(' '.join(config))

# Записываем в файл
with open('electron_configuration_extended.txt', 'w') as f:
    f.write('\n'.join(config))
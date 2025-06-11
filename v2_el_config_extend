def generate_electron_configuration_up_to_extended():

    # Функция для генерации буквенного обозначения подуровня
    def get_sublevel_letter(l):
        standard_letters = ['s', 'p', 'd', 'f', 'g', 'h', 'i', 'k']
        if l < len(standard_letters):
            return standard_letters[l]
        else:
            # Генерация букв для подуровней, выходящих за стандартные
            # Например: l=8 -> 'l', l=9 -> 'm', и т.д.
            return chr(ord('l') + l - 8)  # Начинаем с 'l', так как 'k' уже занята (l=7)

    # Максимальное число электронов на подуровне (2*(2l + 1))
    def sublevel_max_e(l):
        return 2 * (2 * l + 1)

    # Генерируем все возможные орбитали (n, l) по порядку заполнения
    configurations = []
    n = 1
    while True:  # Бесконечный цикл для генерации всех возможных n
        for l in range(0, n):  # l может быть от 0 до n-1
            configurations.append((n, l))
        n += 1

        # Для демонстрации ограничим n, чтобы избежать бесконечного выполнения
        # На практике можно убрать этот блок, если нужно действительно бесконечное количество
        if n > 100:  # Пример ограничения для демонстрации
            break

    # Сортируем по правилу Клечковского (n + l, затем n)
    configurations.sort(key=lambda x: (x[0] + x[1], x[0]))

    # Формируем последовательность
    result = []
    for n, l in configurations:
        sublevel_letter = get_sublevel_letter(l)
        max_e = sublevel_max_e(l)
        result.append(f"{n}{sublevel_letter}{max_e}")

    return result

# Генерируем последовательность
config = generate_electron_configuration_up_to_extended()

print(' '.join(config[:100]))  # Выводим первые 100 элементов для демонстрации

# Записываем в файл
with open('electron_configuration_extended.txt', 'w') as f:
    f.write('\n'.join(config))

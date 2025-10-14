import string

def generate_electron_configuration_up_to_extended():
    def get_sublevel_letter(l):
        standard_letters = ['s', 'p', 'd', 'f', 'g', 'h', 'i', 'k']

        if l < len(standard_letters):
            return standard_letters[l]
        else:
            # Создаем бесконечную последовательность букв
            letters = []
            l -= 8  # Корректировка после 'k'

            while l >= 0:
                letters.append(string.ascii_lowercase[l % 26])
                l = (l // 26) - 1

            return ''.join(reversed(letters))

    def sublevel_max_e(l):
        return 2 * (2 * l + 1)

    configurations = []
    n = 1

    while True:
        for l in range(0, n):
            configurations.append((n, l))
        n += 1

        # Ограничение для демонстрации
        if n > 190:
            break

    configurations.sort(key=lambda x: (x[0] + x[1], x[0]))

    result = []
    for n, l in configurations:
        sublevel_letter = get_sublevel_letter(l)
        max_e = sublevel_max_e(l)
        result.append(f"{n}{sublevel_letter}{max_e}")

    return result

# Генерируем конфигурацию
config = generate_electron_configuration_up_to_extended()

# Выводим последние 10 элементов для демонстрации
for i in config:
    print(i)

# Сохраняем в файл
with open('electron_config_extended.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(config))

import string


def generate_electron_configuration(max_lvl_q):
    def get_sublevel_letter(level_now):
        standard_letters = ['s', 'p', 'd', 'f', 'g', 'h', 'i', 'k']
        if level_now < len(standard_letters):
            return standard_letters[level_now]
        else:
            letters = []
            level_now -= 8  # Корректировка после 'k'
            while level_now >= 0:
                letters.append(string.ascii_lowercase[level_now % 26])
                level_now = (level_now // 26) - 1
            return ''.join(reversed(letters))

    def sublevel_max_e(lvl):
        return 2 * (2 * lvl + 1)

    configurations = []
    n = 1
    total_electrons = 0

    while True:
        for l in range(0, n):
            configurations.append((n, l))
        n += 1
        if n > max_lvl_q:
            break

    configurations.sort(key=lambda x: (x[0] + x[1], x[0]))

    result = []
    for n, l in configurations:
        sublevel_letter = get_sublevel_letter(l)
        max_e = sublevel_max_e(l)
        total_electrons += max_e
        result.append(f"{n}{sublevel_letter}{max_e} {total_electrons}")

    return result


lvl = 50

for dfe in generate_electron_configuration(lvl):
    print(dfe)

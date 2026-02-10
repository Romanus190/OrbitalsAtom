def read_electron_configuration(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print("Файл не найден")
        return None
    except UnicodeDecodeError:
        print("Ошибка декодирования файла. Попробуйте указать другую кодировку.")
        return None

def parse_orbital(orbital_str):
    # Находим границу между номером и показателем степени
    for i in range(len(orbital_str)-1, 0, -1):
        if orbital_str[i].isdigit() and not orbital_str[i-1].isdigit():
            exponent = int(orbital_str[i:])
            orbital_type = orbital_str[:-len(str(exponent))]
            return orbital_type, exponent
    return orbital_str, 1  # Если не нашли показатель степени

def calculate_electrons(lines):
    total = 0
    results = []

    for line in lines:
        orbital_type, exponent = parse_orbital(line)
        total += exponent
        results.append((line, exponent, total))

    return results

if __name__ == "__main__":
    file_path = 'electron_configuration_extended.txt'
    lines = read_electron_configuration(file_path)

    if lines:
        results = calculate_electrons(lines)
        print("Орбиталь\tКоличество электронов\tНакопительная сумма")
        print("-" * 60)
        for line, exponent, total in results:
            print(f"{line}\t\t{exponent}\t\t{total}")

def name_file(names_list: list):
    result = []
    max_len = 0

    # Удаление повторяющихся символов
    for name in names_list:
        name = ''.join(
            [
                char
                for idx, char in enumerate(str(name))
                if char not in str(name)[:idx]
            ]
        )
        max_len = max_len if max_len >= len(name) else len(name)
        result.append(name)

    return [f'{name}{"_" * (max_len - len(name))}' for name in result]



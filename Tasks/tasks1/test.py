from typing import List


def service_center(data: List[tuple]):
    result = {}
    for info in data:
        key = f'{info[2]} {info[3]}'
        value = f'{info[0]} - {info[1]}'
        if result.get(key):
            result[key] += f'; {value}'
        else:
            result[key] = value

    return '\n'.join(f'{key}: {value}' for key, value in result.items())

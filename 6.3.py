def find_max(a, b, c=None):
    if c is not None:
        # Если есть третий аргумент, сравниваем все три числа
        return max(a, b, c)
    else:
        # Если третьего аргумента нет, сравниваем только первые два
        return max(a, b)


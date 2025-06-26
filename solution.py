def add(a: int, b: int) -> int:
    """Возвращает сумму двух чисел."""
    return a + b 

def bochka_word(n: int) -> str:
    """
    Возвращает строку с числом и правильным окончанием слова 'бочка'.
    Примеры: 1 бочка, 2 бочки, 5 бочек
    """
    n_abs = abs(n)
    if n_abs % 10 == 1 and n_abs % 100 != 11:
        word = 'бочка'
    elif 2 <= n_abs % 10 <= 4 and not (12 <= n_abs % 100 <= 14):
        word = 'бочки'
    else:
        word = 'бочек'
    return f"{n} {word}" 
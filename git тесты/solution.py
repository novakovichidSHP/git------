import logging

logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s %(message)s')

def add(a: int, b: int) -> int:
    """Возвращает сумму двух чисел."""
    result = a + b
    logging.info(f"add({a}, {b}) = {result}")
    return result 
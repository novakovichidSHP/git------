import os
import pytest
from solution import add
import logging

def test_add():
    # Очистка лога перед тестом
    if os.path.exists('logs.txt'):
        os.remove('logs.txt')
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    # Гарантируем запись логов на диск
    logging.shutdown()
    # Проверка, что лог-файл создан и содержит записи
    assert os.path.exists('logs.txt')
    with open('logs.txt', 'r', encoding='utf-8') as f:
        log_content = f.read()
    assert 'add(2, 3) = 5' in log_content
    assert 'add(-1, 1) = 0' in log_content
    assert 'add(0, 0) = 0' in log_content 
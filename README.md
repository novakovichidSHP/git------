![CI](https://github.com/novakovichidSHP/git------/actions/workflows/python-app.yml/badge.svg)

# Пример проекта на Python

## 1. Решение задачи

В файле `solution.py` реализована функция, которая возвращает строку с числом и правильным окончанием слова "бочка":
```python
from solution import bochka_word
print(bochka_word(1))   # 1 бочка
print(bochka_word(2))   # 2 бочки
print(bochka_word(5))   # 5 бочек
print(bochka_word(21))  # 21 бочка
```

## 2. Автотесты

Для запуска автотестов используйте:
```bash
pytest
```

## 3. GitHub Actions

Автотесты автоматически запускаются при каждом push или pull request в ветку `main` с помощью GitHub Actions (`.github/workflows/python-app.yml`).

## 4. Требования
- Python 3.11+
- pytest

## Быстрый старт
1. Установите зависимости:
   ```bash
   pip install pytest
   ```
2. Запустите тесты:
   ```bash
   pytest
   ``` 
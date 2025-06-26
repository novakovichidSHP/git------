import pytest
from solution import add
from solution import bochka_word

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_bochka_word():
    assert bochka_word(1) == '1 бочка'
    assert bochka_word(2) == '2 бочки'
    assert bochka_word(5) == '5 бочек'
    assert bochka_word(11) == '11 бочек'
    assert bochka_word(21) == '21 бочка'
    assert bochka_word(22) == '22 бочки'
    assert bochka_word(25) == '25 бочек'
    assert bochka_word(101) == '101 бочка'
    assert bochka_word(112) == '112 бочек'
    assert bochka_word(0) == '0 бочек'
    assert bochka_word(-1) == '-1 бочка'
    assert bochka_word(-2) == '-2 бочки'
    assert bochka_word(-5) == '-5 бочек' 
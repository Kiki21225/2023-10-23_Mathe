import pytest

from basic_calculations import addieren, subtrahieren, multiplizieren, dividieren

def test_addieren_success():
    ergebnis = addieren(3, 3)
    assert ergebnis == 6

def test_addieren_with_float_numbers():
    ergebnis = addieren(69.69, 3)
    assert ergebnis == 72.69

def test_addieren_pass_character_and_number():
    ergebnis = addieren("3", 3)
    assert ergebnis == 6

def test_addieren_pass_characters():
    ergebnis = addieren("65", "4")
    assert ergebnis == 69

def test_addieren_wrong_characters():
    with pytest.raises(ValueError) as err:
        addieren("a", 69)

def test_subtrahieren():
    ergebnis = subtrahieren(3, 1)
    assert ergebnis == 2


def test_subtrahieren_characters():
    with pytest.raises(ValueError) as err:
        subtrahieren("a", 7)

def test_multiplizieren_characters():
    with pytest.raises(ValueError) as err:
        multiplizieren("b", "C")


def test_dividieren_characters():
    with pytest.raises(ValueError) as err:
        dividieren("m", "123")

def test_multiplizieren_success():
    ergebnis = multiplizieren(23, 3)
    assert ergebnis == 69

def test_dividieren():
    ergebnis = dividieren(8, 4)
    assert ergebnis == 2

def test_dividieren_durch_null():
    with pytest.raises(ZeroDivisionError) as err:
        dividieren(69, 0)




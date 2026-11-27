
import pytest

from app.outils.math import factorielle


def test_factorielle_de_5():
    assert factorielle(5) == 120


def test_factorielle_de_0():
    assert factorielle(0) == 1


def test_factorielle_negative():
    with pytest.raises(ValueError):
        factorielle(-1)

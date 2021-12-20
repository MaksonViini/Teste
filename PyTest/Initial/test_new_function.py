from function import Matematica
import pytest

mat = Matematica()

def test_divisao():
    assert mat.divisao(2, 2) == 1
from function import Matematica
import pytest

mat = Matematica()

def test_soma():
    assert mat.soma(1, 2) == 3

def test_subtracao():
    assert mat.subtracao(2, 1) == 1

def test_multiplicacao():
    assert mat.multiplicacao(2, 2) == 4

def test_divisao():
    assert mat.divisao(2, 2) == 1
import sys
import pytest


@pytest.mark.skipif(sys.version_info < (3, 3), reason="requires python3.3")
def test_function():
    assert 1 == 1


@pytest.mark.xfail(reason="1 is not 2")
def test_fail():
    assert 1 == 2


@pytest.mark.parametrize("input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.mark.xfail(("6*9", 42)),
])
def test_eval(input, expected):
    assert eval(input) == expected

# marcar parametro falhando
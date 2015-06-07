import pytest


@pytest.mark.slow
def test_slow():
    assert 1 == 1


@pytest.mark.fast
def test_fast():
    assert 1 == 1


@pytest.mark.slow
def test_very_slow():
    assert 1 == 1

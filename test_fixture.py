import pytest


@pytest.fixture()
def answer():
    return 42


def test_the_ultimate_question_about_life_the_universe_and_everything(answer):
    assert answer == 42

import os

import pytest


@pytest.fixture()
def move_dir():
    os.chdir("/home/renato/pytest/")


def test_count_files(move_dir):
    assert len(os.listdir(".")) == 4

import pytest
import random

numbers_list = [1, 2, 3]


@pytest.mark.ui
def test_1():
    assert 1 == 1


@pytest.mark.api
@pytest.mark.smoke
def test_2():
    assert 1 == random.choice(numbers_list)


@pytest.mark.api
def test_3():
    assert 1 == 1

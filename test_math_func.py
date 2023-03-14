import math_func
import pytest

@pytest.mark.parametrize('x, y, res',
                           [
                               (5, 4, 9),
                               ('Hi', ' Hello', 'Hi Hello'),
                               (2.5, 3.5, 6)
                           ]
                         )
def test_add(x, y, res):
    assert math_func.add(x, y) == res
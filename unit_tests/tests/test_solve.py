from square_solver import solve
import pytest

@pytest.mark.parametrize("a, b, c, expected_result", [
                                                      (1, 0, 1,  []),
                                                      (1, 0, -1, [1, -1]),
                                                      (1, 2, 1,  [-1])
                                                      ])
def test_solve(a, b, c, expected_result):
    assert solve(a, b, c) == expected_result


def test_zero_a_exception():
    with pytest.raises(AttributeError):
        solve(0, 1, 2)


def test_attribute_type_exeption():
    with pytest.raises(AttributeError):
        solve(float('nan'), 1, 2)

    with pytest.raises(AttributeError):
        solve(1, float('nan'), 2)

    with pytest.raises(AttributeError):
        solve(1, 1, float('nan'))
import pytest

import q2


@pytest.fixture
def example_data() -> list[int]:
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_windowed_sums__with_example__has_correct_number_of_sums(
    example_data: list[int],
):
    assert len(q2.windowed_sums(example_data, 3)) == 8


def test_windowed_sums__with_example__has_correct_sum_A(example_data: list[int]):
    assert q2.windowed_sums(example_data, 3)[0] == 607


def test_windowed_sums__with_example__has_correct_sum_B(example_data: list[int]):
    assert q2.windowed_sums(example_data, 3)[1] == 618


def test_windowed_sums__length_less_than_window_size__raises_error():
    with pytest.raises(ValueError):
        q2.windowed_sums([1, 1, 1], 4)


def test_windowed_sums__length_equal_window_size__returns_one_sum():
    assert q2.windowed_sums([1, 2, 3], 3) == [6]

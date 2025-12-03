from aoc.daythree import max_voltage, max_voltage_two, sum_voltages, sum_voltages_two


def test_max_voltage():
    assert max_voltage("987654321111111") == 98
    assert max_voltage("811111111111119") == 89
    assert max_voltage("234234234234278") == 78
    assert max_voltage("818181911112111") == 92


def test_max_voltage_two():
    assert max_voltage_two("987654321111111") == 987654321111
    assert max_voltage_two("811111111111119") == 811111111119
    assert max_voltage_two("234234234234278") == 434234234278
    assert max_voltage_two("818181911112111") == 888911112111


def test_sum_voltages():
    assert (
        sum_voltages(
            ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
        )
        == 357
    )


def test_sum_voltages_two():
    assert (
        sum_voltages_two(
            ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
        )
        == 3121910778619
    )

from aoc.dayone import rotate, calculate, parse_step, calculate_part_two


def test_rotate():
    assert rotate(0, "L", 1) == 99
    assert rotate(0, "L", 100) == 0
    assert rotate(0, "L", 200) == 0
    assert rotate(0, "L", 600) == 0
    assert rotate(0, "R", 503) == 3
    assert rotate(99, "R", 1) == 0
    assert rotate(50, "L", 50) == 0
    assert rotate(50, "R", 50) == 0
    assert rotate(50, "L", 68) == 82
    assert rotate(82, "L", 30) == 52
    assert rotate(52, "R", 48) == 0
    assert rotate(0, "L", 5) == 95
    assert rotate(95, "R", 60) == 55
    assert rotate(55, "L", 55) == 0
    assert rotate(0, "L", 1) == 99
    assert rotate(99, "L", 99) == 0
    assert rotate(0, "R", 14) == 14
    assert rotate(14, "L", 82) == 32


def test_count():
    steps = [
        ["L", 68],
        ["L", 30],
        ["R", 48],
        ["L", 5],
        ["R", 60],
        ["L", 55],
        ["L", 1],
        ["L", 99],
        ["R", 14],
        ["L", 82],
    ]

    assert calculate(steps) == 3


def test_count_part_two():
    steps = [
        ["L", 68],
        ["L", 30],
        ["R", 48],
        ["L", 5],
        ["R", 60],
        ["L", 55],
        ["L", 1],
        ["L", 99],
        ["R", 14],
        ["L", 82],
        ["R", 300],
    ]

    assert calculate_part_two(steps) == 9


def test_parse_step():
    assert parse_step("L68") == ["L", 68]
    assert parse_step("R48") == ["R", 48]
    assert parse_step("L1") == ["L", 1]

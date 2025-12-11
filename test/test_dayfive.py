from aoc.dayfive import create_fresh_range


def test_create_fresh_range():
    assert create_fresh_range(["3-5", "10-14"]) == [[3, 5], [10, 14]]

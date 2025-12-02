from aoc.daytwo import invalid_ids_in_range, invalid_ids_in_range_two


def test_sum_invalid_ids_in_range():
    assert invalid_ids_in_range(11, 22) == [11, 22]
    assert invalid_ids_in_range(95, 115) == [99]
    assert invalid_ids_in_range(998, 1010) == [1010]
    assert invalid_ids_in_range(1188511880, 1188511890) == [1188511885]
    assert invalid_ids_in_range(222220, 222224) == [222222]
    assert invalid_ids_in_range(1698522, 1698528) == []
    assert invalid_ids_in_range(446443, 446449) == [446446]
    assert invalid_ids_in_range(38593856, 38593862) == [38593859]


def test_sum_invalid_ids_in_range_two():
    assert invalid_ids_in_range_two(11, 22) == [11, 22]
    assert invalid_ids_in_range_two(95, 115) == [99, 111]
    assert invalid_ids_in_range_two(998, 1010) == [999, 1010]
    assert invalid_ids_in_range_two(1188511880, 1188511890) == [1188511885]
    assert invalid_ids_in_range_two(222220, 222224) == [222222]
    assert invalid_ids_in_range_two(1698522, 1698528) == []
    assert invalid_ids_in_range_two(446443, 446449) == [446446]
    assert invalid_ids_in_range_two(38593856, 38593862) == [38593859]
    assert invalid_ids_in_range_two(565653, 565659) == [565656]
    assert invalid_ids_in_range_two(824824821, 824824827) == [824824824]
    assert invalid_ids_in_range_two(2121212118, 2121212124) == [2121212121]

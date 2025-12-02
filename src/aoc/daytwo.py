import re


def part_one():
    with open("inputs/daytwo.txt") as input:
        steps = [(line.rstrip()) for line in input]
        ranges = [parse_range(r) for r in steps[0].split(",")]

        count = 0

        for r in ranges:
            invalid = invalid_ids_in_range(r[0], r[1])
            count += sum(invalid)

        return count


def part_two():
    with open("inputs/daytwo.txt") as input:
        steps = [(line.rstrip()) for line in input]
        ranges = [parse_range(r) for r in steps[0].split(",")]

        count = 0

        for r in ranges:
            invalid = invalid_ids_in_range_two(r[0], r[1])
            count += sum(invalid)

        return count


def parse_range(line):
    parts = line.split("-")
    return [int(parts[0]), int(parts[1])]


def invalid_ids_in_range(start, end):
    total = []

    for i in range(start, end + 1):
        as_str = str(i)

        # Only even lengths can repeat
        if len(as_str) % 2 != 0:
            pass

        midpoint = len(as_str) // 2
        if as_str[:midpoint] == as_str[midpoint:]:
            total.append(i)

    return total


def invalid_ids_in_range_two(start, end):
    total = []

    # Any sequence made up of a repeating subsequence
    pattern = r"^(\d+)\1+$"

    for i in range(start, end + 1):
        as_str = str(i)

        if re.match(pattern, as_str):
            total.append(i)

    return total

def part_one():
    with open("inputs/daythree.txt") as input:
        banks = [(line.rstrip()) for line in input]
        return sum_voltages(banks)


def part_two():
    with open("inputs/daythree.txt") as input:
        banks = [(line.rstrip()) for line in input]
        return sum_voltages_two(banks)


def sum_voltages(input):
    return sum([max_voltage(bank) for bank in input])


def sum_voltages_two(input):
    return sum([max_voltage_two(bank) for bank in input])


def max_voltage(bank):
    to_digits = [int(x) for x in list(bank)]

    # Find the highest first digit before the end
    first = max(to_digits[: len(to_digits) - 1])
    first_index = to_digits.index(first)

    # Find the next highest digit after that one
    second = max(to_digits[first_index + 1 :])

    return int(f"{first}{second}")


def max_voltage_two(bank):
    digits = [int(x) for x in list(bank)]
    picks = []

    while len(picks) < 12:
        remaining = 11 - len(picks)
        current = max(digits[: len(digits) - remaining])
        current_index = digits.index(current)

        picks.append(current)
        digits = digits[current_index + 1 :]

    picks_str = [f"{x}" for x in picks]
    return int(f"{''.join(picks_str)}")

def part_one():
    with open("inputs/dayone.txt") as input:
        steps = [parse_step(line.rstrip()) for line in input]
        return calculate(steps)


def part_two():
    with open("inputs/dayone.txt") as input:
        steps = [parse_step(line.rstrip()) for line in input]
        return calculate_part_two(steps)


def parse_step(line):
    return [line[0], int(line[1:])]


def calculate(steps):
    position = 50
    count = 0

    for step in steps:
        new_position = rotate(position, step[0], step[1])
        if new_position == 0:
            count = count + 1

        position = new_position

    return count


def calculate_part_two(steps):
    position = 50
    count = 0

    for step in steps:
        new_position = rotate(position, step[0], step[1])
        step_count = step[1]

        # If we made over 100 steps, we passed zero at least once
        if step_count > 100:
            count += step_count // 100
            step_count = step_count % 100

        if position != 0 and step[0] == "L" and (position - step_count) < 0:
            count += 1

        if position != 0 and step[0] == "R" and (position + step_count) > 100:
            count += 1

        if new_position == 0:
            count = count + 1

        position = new_position

    return count


def rotate(current, direction, steps):
    if steps > 100:
        steps = steps % 100

    if direction == "R":
        if current + steps >= 100:
            return (current + steps) - 100
        else:
            return current + steps
    else:
        if steps > current:
            return 100 - abs(steps - current)
        else:
            return abs(steps - current)

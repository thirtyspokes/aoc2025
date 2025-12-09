def part_one():
    with open("inputs/dayfour.txt") as input:
        matrix = [list(line.rstrip()) for line in input]
        return accesible_rolls(matrix)


def part_two():
    with open("inputs/dayfour.txt") as input:
        matrix = [list(line.rstrip()) for line in input]
        return accessible_roll_remove(matrix)


def accessible_roll_remove(matrix):
    removed = 0
    rolls_were_removed = True

    while rolls_were_removed:
        # Set to false before we start this iteration
        rolls_were_removed = False

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == "@" and adjacent_rolls(matrix, x, y) < 4:
                    matrix[y][x] = "."
                    removed += 1
                    # Removed at least one, so set this to true
                    rolls_were_removed = True

    return removed


def accesible_rolls(matrix):
    count = 0

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "@" and adjacent_rolls(matrix, x, y) < 4:
                count += 1

    return count


def adjacent_rolls(matrix, x, y):
    height = len(matrix)
    width = len(matrix[0])
    count = 0

    # If the target is at least y = 1, count the preceding row
    if y > 0:
        # Check the left side
        if x > 0:
            if matrix[y - 1][x - 1] == "@":
                count += 1
        # The middle
        if matrix[y - 1][x] == "@":
            count += 1
        # Right side
        if x < width - 1:
            if matrix[y - 1][x + 1] == "@":
                count += 1

    # This row
    # Check the left side
    if x > 0:
        if matrix[y][x - 1] == "@":
            count += 1
    # Right side
    if x < width - 1:
        if matrix[y][x + 1] == "@":
            count += 1

    # Next row
    if y < height - 1:
        # Check the left side
        if x > 0:
            if matrix[y + 1][x - 1] == "@":
                count += 1
        # The middle
        if matrix[y + 1][x] == "@":
            count += 1
        # Right side
        if x < width - 1:
            if matrix[y + 1][x + 1] == "@":
                count += 1

    return count

def part_one():
    with open("inputs/dayfive.txt") as input:
        halves = input.read().split("\n\n")
        ranges = halves[0].split("\n")

        count = 0

        fresh = create_fresh_range(ranges)
        ingredients = halves[1].split("\n")

        for i in ingredients:
            for fresh_range in fresh:
                if int(i) >= fresh_range[0] and int(i) <= fresh_range[1]:
                    count += 1
                    break

        return count


def part_two():
    with open("inputs/dayfive.txt") as input:
        halves = input.read().split("\n\n")
        ranges = halves[0].split("\n")

        fresh = create_fresh_range(ranges)
        sorted_ranges = sorted(fresh)
        merged = [sorted_ranges[0]]

        for start, end in sorted_ranges[1:]:
            last_start, last_end = merged[-1]

            if start <= last_end + 1:
                merged[-1] = [last_start, max(last_end, end)]
            else:
                # No overlap
                merged.append([start, end])

        total = sum(end - start + 1 for start, end in merged)
        return total


def create_fresh_range(ranges):
    allowed = []
    for x in ranges:
        parsed = x.split("-")
        allowed.append([int(parsed[0]), int(parsed[1])])

    return allowed

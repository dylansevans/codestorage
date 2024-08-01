import math

total = 1000000

def main(total_cubes):
    count = 0

    max_half_width = math.ceil(total_cubes / 4)

    for i in range(1, max_half_width + 2):
        for x in range(i - 2, 0, -2):
            if i * i - x * x <= total:
                count += 1

    return count

print(main(total))
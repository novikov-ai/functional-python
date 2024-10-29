from functools import reduce

numbers = [4, 1, 8, 7, 5, 8]

first_max, second_max = reduce(
    lambda acc, x: (x, acc[0]) if x > acc[0] else (acc[0], x) if acc[0] > x > acc[1] else acc,
    numbers,
    (float('-inf'), float('-inf'))
)

print(second_max)  # Output: 7

num = int(input())

longest_intersection = []

for i in range(num):
    ranges = input().split("-")
    first = ranges[0].split(",")
    second = ranges[1].split(",")
    first_start = int(first[0])
    first_end = int(first[1])
    second_start = int(second[0])
    second_end = int(second[1])
    first_set = set()
    second_set = set()
    for digit in range(first_start, first_end + 1):
        first_set.add(digit)
    for digit in range(second_start, second_end + 1):
        second_set.add(digit)
    intersection = first_set.intersection(second_set)
    if len(longest_intersection) < len(intersection):
        longest_intersection = list(intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
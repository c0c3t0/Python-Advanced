numbers = [float(el) for el in input().split()]

counter = {}

for num in numbers:
    if num not in counter:
        counter[num] = numbers.count(num)

for key, value in counter.items():
    print(f"{key} - {value} times")
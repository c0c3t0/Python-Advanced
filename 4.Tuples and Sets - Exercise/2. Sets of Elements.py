n, m = [int(el) for el in input().split()]

first_set = set()
second_set = set()

for first in range(n):
    first_set.add(input())
for second in range(m):
    second_set.add(input())

print('\n'.join(first_set.intersection(second_set)))

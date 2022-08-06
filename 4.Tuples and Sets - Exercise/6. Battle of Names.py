num = int(input())


even_set = set()
odd_set = set()

for i in range(1, num + 1):
    ascii_sum = 0
    result = 0
    name = input()
    for letter in name:
        ascii_sum += ord(letter)
        result = ascii_sum // i
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

if sum(even_set) == sum(odd_set):
    answer = odd_set.union(even_set)
elif sum(even_set) > sum(odd_set):
    answer = odd_set.symmetric_difference(even_set)
elif sum(even_set) < sum(odd_set):
    answer = odd_set.difference(even_set)

print(', '.join([str(el) for el in answer]))

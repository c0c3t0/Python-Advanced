n = int(input())

chemical_elements = set()
for i in range(n):
    compounds = input().split()
    for el in compounds:
        chemical_elements.add(el)

print('\n'.join(chemical_elements))

num = int(input())

names = set()
for i in range(num):
    names.add(input())

print('\n'.join(names))
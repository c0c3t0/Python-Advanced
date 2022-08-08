from collections import deque

boxes = [int(el) for el in input().split()]
level_magic = deque([int(el) for el in input().split()])

presents = {'Doll': 150, 'Wooden train': 250, 'Teddy bear': 300, 'Bicycle': 400}
crafted = []

while boxes and level_magic:
    box = boxes.pop()
    magic = level_magic.popleft()
    result = box * magic

    if box == 0 and magic == 0:
        continue
    if box == 0:
        level_magic.appendleft(magic)
        continue
    if magic == 0:
        boxes.append(box)
        continue

    if result < 0:
        boxes.append(box + magic)
    elif result in presents.values():
        value = list(presents.values()).index(result)
        key = list(presents.keys())
        crafted.append(key[value])
    else:
        boxes.append(box + 15)


if ('Doll' in crafted and 'Wooden train' in crafted) or ('Teddy bear' in crafted and 'Bicycle' in crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    print(f"Materials left: {', '.join([str(x) for x in boxes[::-1]])}")
if level_magic:
    print(f"Magic left: {', '.join([str(x) for x in level_magic])}")

sorted_list = sorted(set(crafted))
for item in sorted_list:
    print(f"{item}: {crafted.count(item)}")

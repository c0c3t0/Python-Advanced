from collections import deque

quantity = int(input())
queue = deque(int(el) for el in input().split())

print(max(queue))
while queue:
    if quantity >= queue[0]:
        quantity -= queue.popleft()
    else:
        break

if not queue:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(el) for el in queue])}")

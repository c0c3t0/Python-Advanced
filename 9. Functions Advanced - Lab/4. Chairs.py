def chairs(names, chair, pairs=[]):
    if len(pairs) == chair:
        print(', '.join(pairs))
        return

    for i in range(len(names)):
        pairs.append(names[i])
        chairs(names[i + 1:], chair, pairs)
        pairs.pop()


names = input().split(", ")
chair = int(input())
chairs(names, chair)

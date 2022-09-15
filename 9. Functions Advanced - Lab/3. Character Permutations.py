def permutation(index, values):
    if index >= len(values):
        print(''.join(values))
        return
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permutation(index + 1, values)
        values[index], values[i] = values[i], values[index]


seq = list(input())
index = 0
permutation(index, seq)

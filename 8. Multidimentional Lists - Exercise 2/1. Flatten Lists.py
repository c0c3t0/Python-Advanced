matrix = []
text = list(input().split("|"))

for i in range(len(text)-1, -1, -1):
    sub_lists = text[i].split()
    matrix += sub_lists

print(' '.join(matrix))
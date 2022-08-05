box = [int(el) for el in input().split()]
capacity = int(input())

sum_clothes = 0
rack = 1
while box:
    if sum_clothes + box[-1] > capacity:
        rack += 1
        sum_clothes = 0
    elif sum_clothes + box[-1] == capacity:
        sum_clothes += box.pop()
        if not rack == 1:
            sum_clothes = 0
            rack += 1
    else:
        sum_clothes += box.pop()

print(rack)

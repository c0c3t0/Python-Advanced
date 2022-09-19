seq = [int(el) for el in input().split()]

positives = sum(filter(lambda a: a > 0, seq))
negatives = sum(filter(lambda a: a < 0, seq))

print(negatives)
print(positives)

if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
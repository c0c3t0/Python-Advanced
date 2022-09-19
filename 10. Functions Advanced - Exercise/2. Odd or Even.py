command = input()
numbers = [int(el) for el in input().split()]


odd = sum(filter(lambda a: a % 2 != 0, numbers))
even = sum(filter(lambda a: a % 2 == 0, numbers))

if command == "Odd":
    print(odd * len(numbers))
else:
    print(even * len(numbers))
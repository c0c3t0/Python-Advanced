command = input()
numbers = [int(el) for el in input().split()]

odd = sum(filter(lambda a: a % 2 != 0, numbers))
even = sum(filter(lambda a: a % 2 == 0, numbers))

print(odd * len(numbers)) if command == "Odd" else print(even * len(numbers))

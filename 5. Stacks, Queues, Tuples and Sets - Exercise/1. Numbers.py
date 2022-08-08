first = set([int(el) for el in input().split()])
second = set([int(el) for el in input().split()])
number = int(input())

for line in range(number):
    command = input().split()
    if command[0] == "Check":
        print(second.issubset(first))
    else:
        for num in range(2, len(command)):
            if command[0] == "Add":
                if command[1] == "First":
                    first.add(int(command[num]))

                elif command[1] == "Second":
                    second.add(int(command[num]))

            elif command[0] == "Remove":
                if command[1] == "First":
                    if int(command[num]) in first:
                        first.remove(int(command[num]))

                elif command[1] == "Second":
                    if int(command[num]) in second:
                        second.remove(int(command[num]))
sorted_f = sorted(first)
sorted_s = sorted(second)
print(f"{', '.join([str(x) for x in sorted_f])}")
print(f"{', '.join([str(x) for x in sorted_s])}")

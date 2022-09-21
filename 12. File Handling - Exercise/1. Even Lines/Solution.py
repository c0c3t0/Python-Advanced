symbols = {"-", ",", ".", "!", "?"}

with open("text.txt", "r") as file:
    index = 0
    for line in file:
        if not line:
            break
        if index % 2 == 0:
            for el in line:
                if el in symbols:
                    line = line.replace(el, "@")
            print(' '.join(line.split()[::-1]))
        index += 1

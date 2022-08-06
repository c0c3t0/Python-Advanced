text = input()

counter = {}
for char in text:
    if char not in counter:
        counter[char] = text.count(char)

sorted_counter = sorted(counter.items(), key=lambda x: x[0])
for key, value in sorted_counter:
    print(f"{key}: {value} time/s")

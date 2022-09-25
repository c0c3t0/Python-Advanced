jobs = [int(el) for el in input().split(", ")]
job_index = int(input())

values = {}
clock_cycles = 0
for index in range(len(jobs)):
    values[index] = jobs[index]

while True:
    min_value = min(values.values())
    clock_cycles += min_value
    for k, v in values.items():
        if v == min_value:
            values.pop(k)
            break
    if job_index not in values.keys():
        break

print(clock_cycles)
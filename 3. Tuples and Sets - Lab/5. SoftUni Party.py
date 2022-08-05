n = int(input())
all_guests = set()

for _ in range(n):
    all_guests.add(input())

ticket = input()

arrived = set()
while not ticket == "END":
    arrived.add(ticket)
    ticket = input()

didnt_arrived = all_guests - arrived
print(len(all_guests.difference(arrived)))
print('\n'.join(sorted(didnt_arrived)))
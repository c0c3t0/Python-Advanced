from string import ascii_letters

rows, cols = map(int, input().split())

for row in range(rows):
    palindromes = []
    for col in range(cols):
        r = ascii_letters[row]
        c = ascii_letters[row + col]
        palindrome = r + c + r
        palindromes.append(palindrome)
    print(*palindromes, end=" ")
    print()
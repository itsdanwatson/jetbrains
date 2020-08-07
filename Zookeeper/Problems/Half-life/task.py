N = int(input())
R = int(input())

atoms = N
days = 0
while atoms > R:
    atoms = atoms // 2
    days += 1
print(days * 12)

print("s = 1 + 2 + 3 + 4 + 5 +.... + n")
s = 0
n = int(input("Enter n: "))
for x in range(1, n + 1):
    s += x
    print(s)
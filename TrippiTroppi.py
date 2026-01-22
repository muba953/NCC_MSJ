k = int(input())

for _ in range(k):
    a, b, c = input().split()

    if len(a) < 10 and len(b) < 10 and len(c) < 10:
        print(a[0]+ b[0] + c[0])
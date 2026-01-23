t = int(input())

for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))

    even = 0
    odd = 0

    for x in m:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1

    if even == n and odd == n:
        print("Yes")
    else:
        print("No")
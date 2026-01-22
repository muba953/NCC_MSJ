m= int(input())

for _ in range(m):
    a, b, c = map(int, input().split())
    
    if a > b:
        print("First")
    elif a < b:
        print("Second")
    else:  # a == b
        if c % 2 == 1:
            print("First")
        else:
            print("Second")
    
km= int(input())

for i in range(km):
    a, b= map(int, input().split())
    print(min(a,b),max(a,b))
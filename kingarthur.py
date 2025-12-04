d=float(input())  
w=float(input())
n=int(input())
import math
B=d*math.pi
H=w*n
if B>=H:
    print("YES")
else:    
  print("NO")
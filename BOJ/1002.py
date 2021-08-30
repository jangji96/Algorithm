import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
  x1,y1,r1,x2,y2,r2 = map(int,input().split())
  r = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
  arr = [r,r1,r2]
  maxR = max(arr)
  arr.remove(maxR)
  if(r == 0 and r1 == r2 ) :
    print(-1)
  elif r1+r2 == r or maxR == sum(arr) :
    print(1)
  elif maxR > sum(arr) :
    print(0)
  else :
    print(2)
import sys
input = sys.stdin.readline

n, r, c = map(int,input().split())

width = 2**n
num = 0

for _ in range(n) :
  if r < width//2 and c < width//2 :
    num = num + width * width//4 * 0
  elif r < width//2 and c >= width//2 :
    num = num + width * width//4 * 1
    c = c - width//2
  elif r >= width//2 and c < width//2 :
    num = num + width * width//4 * 2
    r = r -width//2
  elif r >= width//2 and c >= width//2 :
    num = num + width * width//4 * 3
    c=c-width//2
    r=r-width//2
  
  width = width//2

print(num)
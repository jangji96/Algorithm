import sys
input = sys.stdin.readline

n, m = map(int, input().split())
count = 1

while True :
  if m%10 == 1 and m>10:
    m = m // 10
    count = count + 1
  elif m%2 == 0 :
    m = m // 2
    count = count + 1
  if m==n :
    break
  if (m%2 != 0 and m%10 != 1) or m<n:
    count = -1
    break
  
print(count)
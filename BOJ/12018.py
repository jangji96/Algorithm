import sys
input = sys.stdin.readline

n, m = map(int,input().split())
sign = []
for i in range(n) :
  p, l = map(int,input().split())
  arr=list(map(int,input().split()))
  arr.sort(reverse=True)
  if p>=l :
    sign.append(arr[l-1])
  else :
    sign.append(1)

sign.sort()
count = 0
sp = 0

for i in sign :
  count+=1
  m -= i
  if m < 0 :
    print(count-1)
    break;
if m>0:
  print(count)
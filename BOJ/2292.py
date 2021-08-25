import sys
input = sys.stdin.readline

n = int(input())
count = 0
a = 1
while True :
  count += 1
  a += 6*(count-1)
  if(a>=n) :
    print(count)
    break
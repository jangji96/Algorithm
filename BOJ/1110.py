import sys
input = sys.stdin.readline

a = int(input())
new = a
cnt = 0

while True :
  cnt += 1
  new = (new%10)*10 + (new//10 + new%10)%10
  if new == a :
    print(cnt)
    break

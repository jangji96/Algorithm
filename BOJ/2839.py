import sys
input = sys.stdin.readline

a = int(input())
count = 0

while True :
  if a % 5 == 0 :
    count += a // 5
    break
  elif a >= 3 :
    a -= 3
    count += 1
  else :
    count = -1
    break

print(count)
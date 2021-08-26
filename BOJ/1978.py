import sys
input = sys.stdin.readline

a=int(input())
arr = list(map(int, input().split()))
count = 0

for i in arr :
  TF = 0
  if i == 0 :
    continue
  for j in range(2,i+1) :
    if i % j == 0 :
      TF += 1
  if TF == 1 :
    count += 1
  

print(count)
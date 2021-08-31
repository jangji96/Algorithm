import sys
input = sys.stdin.readline

t=int(input())
arr = []
rank = [1 for _ in range(t)]

for _ in range(t) :
  arr.append(list(map(int,input().split())))

for i in range(t) :
  for j in range(t) :
    if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
      rank[i] += 1

for i in rank :
  print(i,end=' ')
print()
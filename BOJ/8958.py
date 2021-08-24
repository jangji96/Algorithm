import sys
input = sys.stdin.readline

a = int(input())
arr = []
score=0;
combo = 0;
for _ in range(a) :
  arr.append(list(input().strip()))

for i in range(a) :
  for ox in arr[i] :
    if ox == 'O' :
      score += 1 + combo
      combo += 1
    else :
      combo = 0
  print(score)
  score = 0
  combo = 0

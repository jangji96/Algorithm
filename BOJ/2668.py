import sys
input = sys.stdin.readline

n = int(input())
ranArr = [0]

for i in range(n):
  ranArr.append(int(input()))

visit = [False for _ in range(len(ranArr))]

for j in range(1,len(ranArr)) :
  if visit[j] == True :
    continue
  
  temp = j
  tempVisit = [False for _ in range(len(ranArr))]

  while visit[temp] == False and tempVisit[temp] == False:
    tempVisit[temp] = True
    temp = ranArr[temp]
  
  check = temp == j
  for i in range(1, len(ranArr)):
    if visit[i] == True and tempVisit[i] == True:
      check = False
      break

  if check:
    for i in range(len(ranArr)):
      visit[i] = visit[i] or tempVisit[i]

print(visit.count(True))
for i in range(1, len(ranArr)):
  if visit[i]:
    print(i)
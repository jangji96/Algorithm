import sys
input = sys.stdin.readline

n = int(input())
selArr = [1]
num = 0
ranArr = []
visit=[]

for i in range(n):
  ranArr.append(int(input()))
  visit.append(False)
visit[0]=True
for j in range(n) :
  if visit[j] == True :
    continue
  print(j)
  while True :
    print(visit,selArr,num)
    selArr.append(ranArr[num])
    if ranArr[ranArr[num]-1]-1 == j or visit[num] == True:
      visit[ranArr[num]-1]=True
      break
    else :
      visit[ranArr[num]-1]=True
      num = ranArr[num]-1
print(selArr)